FROM python:3.10-slim AS builder

WORKDIR /app

# Копируем файлы для установки зависимостей
COPY requirements.txt requirements.txt

# Устанавливаем Python-зависимости
RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip && \
    apt-get purge -y --auto-remove gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Этап 2: Создание финального образа
FROM python:3.10-slim

WORKDIR /app

# Копируем зависимости и исходный код из первого этапа
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/

COPY . .

ENV API_HOST=0.0.0.0
ENV API_PORT=8000
EXPOSE 8000

ENTRYPOINT ["python", "main.py"]