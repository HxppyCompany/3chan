from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from three_chan.topic.models import Topic


class TopicRepository:
    async def find_all(self, session: AsyncSession):
        s = await session.execute(
            select(Topic).order_by(Topic.id.asc()),
        )
        return s.scalars().all()
