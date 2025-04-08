from fastapi import APIRouter

from three_chan.common.dependencies import SessionDep, UserServiceDep
from three_chan.users.schemas import RegisterUserSchema, UserSchema

users_router = APIRouter(prefix="/users", tags=["Пользователи"])


@users_router.post("")
async def register_user(
    schema: RegisterUserSchema,
    service: UserServiceDep,
    session: SessionDep,
) -> UserSchema:
    user = await service.create(schema, session)
    return UserSchema.model_validate(user)


@users_router.get("/{id}")
async def get_user_by_id(
    id: int,
    service: UserServiceDep,
    session: SessionDep,
) -> UserSchema:
    user = await service.find_by_id(id, session)
    return UserSchema.model_validate(user)
