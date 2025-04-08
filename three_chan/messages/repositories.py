from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from three_chan.messages.models import Message


class MessageRepository:
    async def find_all_by_topic_id(
        self,
        topic_id: int,
        session: AsyncSession,
    ):
        s = await session.execute(
            select(Message)
            .where(
                Message.topic_id == topic_id,
            )
            .order_by(Message.id.desc()),
        )
        return s.scalars().all()
