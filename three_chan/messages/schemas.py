from typing import Annotated

from pydantic import BaseModel, StringConstraints


class MessageSchema(BaseModel):
    id: int
    text: str
    creator_user_id: int


class CreateMessageSchema(BaseModel):
    text: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=1,
        ),
    ]
