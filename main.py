from aiogram import Bot, Dispatcher, types
import os
import asyncio
from dotenv import load_dotenv
from handlers.user_handlers import router as router_user_handlers
# import logging

async def main() -> None:
    """
    ENTRY POIT
    """
    load_dotenv('.env')
    token = os.getenv("TOKEN_API")

    bot = Bot(token)
    dp = Dispatcher()

    dp.include_router(router_user_handlers)

    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(_ex)


if __name__ == '__main__':
    asyncio.run(main())