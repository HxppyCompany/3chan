from typing import Annotated, cast

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from three_chan.common.db import DatabaseManager
from three_chan.users.services import UserService


async def session(request: Request):
    db_manager = cast(
        DatabaseManager,
        request.app.state.db_manager,
    )
    async with db_manager.get_session() as session:
        yield session


def user_service(request: Request):
    return cast(
        UserService,
        request.app.state.user_service,
    )


SessionDep = Annotated[
    AsyncSession,
    Depends(session),
]
UserServiceDep = Annotated[
    UserService,
    Depends(user_service),
]
