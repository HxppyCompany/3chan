from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from three_chan.users.models import User


class UserRepository:
    async def find_by_name(self, name: str, session: AsyncSession):
        s = await session.execute(
            select(User).where(User.name == name),
        )
        return s.scalar_one_or_none()

    async def find_by_id(self, id: int, session: AsyncSession):
        return await session.get(User, id)
