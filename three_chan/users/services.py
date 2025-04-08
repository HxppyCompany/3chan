from sqlalchemy.ext.asyncio import AsyncSession

from three_chan.common.exceptions import EntityAlreadyExistException, NotFoundException
from three_chan.users.models import User
from three_chan.users.repositories import UserRepository
from three_chan.users.schemas import RegisterUserSchema


class UserService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    async def create(self, schema: RegisterUserSchema, session: AsyncSession):
        user = await self.__repository.find_by_name(schema.name, session)
        if user is not None:
            raise EntityAlreadyExistException(f"User with name={schema.name} already exists")

        user = User(
            name=schema.name,
            password=schema.password,
        )

        session.add(user)
        await session.commit()

        return user

    async def find_by_id(self, id: int, session: AsyncSession):
        user = await self.__repository.find_by_id(id, session)
        if user is None:
            raise NotFoundException(f"User with {id=} does not exist")

        return user
