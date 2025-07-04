from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Cześć! Jestem Twoim botem Telegram.')

async def main():
    token = 'TWÓJ_TOKEN_TUTAJ'
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
