from typing import Annotated

from pydantic import BaseModel, StringConstraints


class TopicSchema(BaseModel):
    id: int
    name: str
    creator_user_id: int


class CreateTopicSchema(BaseModel):
    name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=1,
        ),
    ]
