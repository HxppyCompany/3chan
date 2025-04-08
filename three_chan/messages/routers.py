from fastapi import APIRouter

from three_chan.messages.schemas import CreateMessageSchema, MessageSchema

message_router = APIRouter(
    tags=["Сообщения"],
)


@message_router.post("/topics/{topic_id}/messages")
async def create_message(
    topic_id: int,
    schema: CreateMessageSchema,
) -> MessageSchema:
    return MessageSchema(
        id=1,
        text="aba",
        creator_user_id=1,
    )


@message_router.get("/topics/{topic_id}/messages")
async def get_messages(
    topic_id: int,
) -> list[MessageSchema]:
    return [
        MessageSchema(
            id=1,
            text="aba",
            creator_user_id=1,
        ),
    ]
