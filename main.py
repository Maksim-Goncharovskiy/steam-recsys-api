import sys
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api import router
from config import load_config


def setup_logging():
    """Выполняет настройку логгирования"""

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)

    # Настройка логгера
    logging.basicConfig(
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            handler,
        ]
    )
    
    return logging.getLogger(__name__)


logger = setup_logging()



if __name__ == "__main__":
    logger.info("Загрузка конфига...")
    config = load_config()

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router=router)

    logger.info("Приложение сформировано, выполняется запуск...")
    uvicorn.run(app=app, host=config.host, port=config.port)
