import asyncio
from aiohttp import web
from bot.webhook import setup_webhook

async def on_startup(app):
    await setup_webhook()

async def index(request):
    return web.Response(text="Bot is running (kind of).")

def start():
    app = web.Application()
    app.router.add_get("/", index)
    app.on_startup.append(on_startup)
    return app

if __name__ == "__main__":
    web.run_app(start(), host="0.0.0.0", port=8000)
