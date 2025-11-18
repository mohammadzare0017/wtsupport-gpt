import os
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.webhook import Webhook

BOT_TOKEN = "توکن رباتت"
WEBHOOK_URL = "https://yourdomain.com/path/webhook"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def setup_webhook():
    webhook = Webhook(bot=bot, url=WEBHOOK_URL)
    await webhook.delete()
    await webhook.set()

def register_handlers():
    @dp.message()
    async def all_messages(message):
        await message.answer("سلام، من زنده‌ام!")

async def setup(app):
    register_handlers()
    SimpleRequestHandler(dp, bot).register(app, path="/path/webhook")
    setup_application(app, dp, bot)
