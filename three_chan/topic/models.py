import typing

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from three_chan.common.db import Base

if typing.TYPE_CHECKING:
    from three_chan.messages.models import Message
    from three_chan.users.models import User


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    owner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    owner: Mapped["User"] = relationship(
        cascade="save-update, merge",
        back_populates="topics",
    )
    messages: Mapped[list["Message"]] = relationship(
        cascade="save-update, merge, delete, delete-orphan",
        back_populates="topic",
    )
