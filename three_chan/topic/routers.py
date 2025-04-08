from fastapi import APIRouter

from three_chan.topic.schemas import CreateTopicSchema, TopicSchema

topics_router = APIRouter(
    prefix="/topics",
    tags=["Темы"],
)


@topics_router.post("")
async def create_topic(
    schema: CreateTopicSchema,
) -> TopicSchema:
    return TopicSchema(
        id=1,
        name="Baba",
        creator_user_id=1,
    )


@topics_router.get("")
async def get_topics_list() -> list[TopicSchema]:
    return [
        TopicSchema(
            id=1,
            name="Baba",
            creator_user_id=1,
        ),
    ]
