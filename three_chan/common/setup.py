import logging
import logging.config

from contextlib import asynccontextmanager
from typing import cast

import yaml

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from three_chan.common.db import DatabaseManager
from three_chan.common.exceptions import AppException, app_exception_handler
from three_chan.common.settings import AppSettings
from three_chan.messages.routers import message_router
from three_chan.topic.routers import topics_router
from three_chan.users.repositories import UserRepository
from three_chan.users.routers import users_router
from three_chan.users.services import UserService

logger = logging.getLogger(__name__)

def setup_app():
    with open("config.yaml") as config:
        c: dict = yaml.load(config, yaml.FullLoader)
        logging.config.dictConfig(c)

    app = FastAPI(
        title="3chan",
        lifespan=app_lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    app.include_router(users_router)
    app.include_router(topics_router)
    app.include_router(message_router)

    app.add_exception_handler(AppException, app_exception_handler)

    settings = AppSettings()
    app.state.db_manager = DatabaseManager(settings.db_url)

    app.state.user_repository = UserRepository()
    app.state.user_service = UserService(
        app.state.user_repository,
    )

    return app


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    db_manager = cast(DatabaseManager, app.state.db_manager)
    
    logger.info("Starting")

    await db_manager.initialize()
    logger.info("Started!")
    
    yield
    logging.info("Stopping app")
    await db_manager.dispose()
    logging.info("Stopped.")
