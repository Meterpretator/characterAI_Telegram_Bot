from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
from handlers import router
import config

async def main():
    # Объект бота
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    # Диспетчер
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
