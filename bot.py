# ECHO BOT
import aiogram 
import config 

from aiogram import Bot, Dispatcher, executor, types

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# echo
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# run long-polling
if __name__ == '__main__': 
    executor.start_polling(dp, skip_updates=True)


