import asyncio

from client import AgentClient
from core import settings
from schema import ChatMessage
from schema.models import AliModelName, OpenAIModelName


async def amain() -> None:
    #### ASYNC ####
    client = AgentClient(settings.BASE_URL)

    print("智能体信息:")
    print(client.info)

    print("聊天示例:")
    response = await client.ainvoke("给我简短地说个笑话？中文回答", model=AliModelName.Qwen2)
    response.pretty_print()

    print("\nStream example:")
    async for message in client.astream("Share a quick fun fact?"):
        if isinstance(message, str):
            print(message, flush=True, end="")
        elif isinstance(message, ChatMessage):
            print("\n", flush=True)
            message.pretty_print()
        else:
            print(f"ERROR: Unknown type - {type(message)}")


def main() -> None:
    #### SYNC ####
    client = AgentClient(settings.BASE_URL)

    print("Agent info:")
    print(client.info)

    print("Chat example:")
    response = client.invoke("Tell me a brief joke?", model=AliModelName.Qwen2)
    response.pretty_print()

    print("\nStream example:")
    for message in client.stream("Share a quick fun fact?"):
        if isinstance(message, str):
            print(message, flush=True, end="")
        elif isinstance(message, ChatMessage):
            print("\n", flush=True)
            message.pretty_print()
        else:
            print(f"ERROR: Unknown type - {type(message)}")


if __name__ == "__main__":
    print("Running in sync mode")
    main()
    print("\n\n\n\n\n")
    print("Running in async mode")
    asyncio.run(amain())
