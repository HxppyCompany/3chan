import typing

from sqlalchemy.orm import Mapped, mapped_column, relationship

from three_chan.common.db import Base

if typing.TYPE_CHECKING:
    from three_chan.messages.models import Message
    from three_chan.topic.models import Topic


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    topics: Mapped[list["Topic"]] = relationship(
        cascade="save-update, delete, delete-orphan",
        back_populates="owner",
    )
    messages: Mapped[list["Message"]] = relationship(
        cascade="save-update, delete, delete-orphan",
        back_populates="owner",
    )
