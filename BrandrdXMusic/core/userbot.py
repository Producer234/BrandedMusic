from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

# Original groups for all assistants
GROUPS_TO_JOIN = [
    "PR_ALL_BOT_SUPPORT",
    "MAIN_CHANNEL_PR",
    "PR_ALL_BOT",
    "HARAM_RELAM_MAIN_CHANNEL",
]


class Userbot:
    def __init__(self):
        # Initialize all five assistants with new names
        self.one = Client(
            "BrandXBot1",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            "BrandXBot2",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            "BrandXBot3",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            "BrandXBot4",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            "BrandXBot5",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start_assistant(self, client: Client, index: int, string_attr: str):
        if not string_attr:
            return

        try:
            await client.start()

            # Each assistant joins all the correct groups
            for group in GROUPS_TO_JOIN:
                try:
                    await client.join_chat(group)
                except Exception:
                    pass

            assistants.append(index)

            # Notify log group
            try:
                await client.send_message(
                    config.LOGGER_ID, f"BrandX Assistant {index} Started"
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant {index} cannot access the log group. Check permissions!"
                )
                exit()

            # Get assistant info
            me = await client.get_me()
            client.id, client.name, client.username = me.id, me.first_name, me.username
            assistantids.append(me.id)

            LOGGER(__name__).info(f"Assistant {index} Started as {client.name}")

        except Exception as e:
            LOGGER(__name__).error(f"Failed to start Assistant {index}: {e}")

    async def start(self):
        LOGGER(__name__).info("Starting BrandX Assistants...")
        await self.start_assistant(self.one, 1, config.STRING1)
        await self.start_assistant(self.two, 2, config.STRING2)
        await self.start_assistant(self.three, 3, config.STRING3)
        await self.start_assistant(self.four, 4, config.STRING4)
        await self.start_assistant(self.five, 5, config.STRING5)

    async def stop(self):
        LOGGER(__name__).info("Stopping BrandX Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except Exception as e:
            LOGGER(__name__).error(f"Error while stopping assistants: {e}")