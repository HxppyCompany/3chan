import typing

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from three_chan.common.db import Base

if typing.TYPE_CHECKING:
    from three_chan.topic.models import Topic
    from three_chan.users.models import User


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    topic_id: Mapped[int] = mapped_column(
        ForeignKey("topics.id"),
    )
    owner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    topic: Mapped["Topic"] = relationship(
        cascade="save-update, merge",
        back_populates="messages",
    )
    owner: Mapped["User"] = relationship(
        cascade="save-update, merge",
        back_populates="messages",
    )
