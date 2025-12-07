import sys
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api import router


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
    app = FastAPI()
    app.include_router(router=router)
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
