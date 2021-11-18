from sys import argv
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser


api_id = "Get yours here:"
api_hash = "https://my.telegram.org/apps"

client = TelegramClient("sesh", api_id, api_hash)


async def main():
    if len(argv) != 2:
        print('Usage:\n    purge-my-msg.py "Fancy Group Name"')
        exit(1)

    chat = None

    try:
        chat = await client.get_input_entity(argv[1])
    except:
        await client.get_dialogs()  # populates cache
        chat = argv[1]  # will resolve automatically anyways

    me = PeerUser((await client.get_me(input_peer=True)).user_id)

    messages = []

    async for message in client.iter_messages(chat):
        if message.from_id == me:
            messages.append(message)

    await client.delete_messages(chat, messages)

    print(len(messages), "messages deleted.")


with client:
    client.loop.run_until_complete(main())
