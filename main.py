import asyncio
from core.bot import dp, bot
from utils.bd_creation import bd_creation

from handlers import photo, callback, commands

bd_creation()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
