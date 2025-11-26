from pyrogram import Client, filters
import asyncio
from os import getenv
from dotenv import load_dotenv
from strings.__init__ import LOGGERS
from ..logging import LOGGER

load_dotenv()
import config

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")

assistants = []
assistantids = []

ASSISTANT1_USERNAME = "@PR_MUSIC_ASSISTANT"  # valid username

# All assistants will join these chats
NEW_CHATS = [
    "PR_ALL_BOT_SUPPORT",
    "ALL_ONGOING_ANIME_IN_HINDI",
    "PR_ALL_BOT",
    "MAIN_CHANNEL_PR"
]

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="BrandrdXMusic1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
            ipv6=False,
        )
        self.two = Client(
            name="BrandrdXMusic2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
            ipv6=False,
        )
        self.three = Client(
            name="BrandrdXMusic3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
            ipv6=False,
        )
        self.four = Client(
            name="BrandrdXMusic4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
            ipv6=False,
        )
        self.five = Client(
            name="BrandrdXMusic5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
            ipv6=False,
        )

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        clients = [self.one, self.two, self.three, self.four, self.five]
        strings = [
            config.STRING1,
            config.STRING2,
            config.STRING3,
            config.STRING4,
            config.STRING5
        ]
        for idx, (client, string_session) in enumerate(zip(clients, strings), start=1):
            if string_session:
                await client.start()
                try:
                    for chat in NEW_CHATS:
                        await client.join_chat(chat)
                except:
                    pass

                assistants.append(idx)
                try:
                    await client.send_message(config.LOGGER_ID, f"Assistant {idx} Started!")
                except:
                    LOGGER(__name__).error(
                        f"Assistant {idx} failed to access the log group. Make sure it is added and admin!"
                    )

                client.id = client.me.id
                if idx == 1:
                    client.username = ASSISTANT1_USERNAME
                else:
                    client.username = client.me.username or f"@Assistant{idx}"
                assistantids.append(client.id)
                LOGGER(__name__).info(f"Assistant {idx} Started as {client.username}")

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        for client in [self.one, self.two, self.three, self.four, self.five]:
            try:
                if client:
                    await client.stop()
            except:
                pass