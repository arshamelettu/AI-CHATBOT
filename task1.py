from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your AI bot. Send me any message!!")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"User said: {user_message}")
    await update.message.reply_text(f"You said: {user_message}")
def main():
    TOKEN = "8121814836:AAHqx3Qnb7Ne_Kat85xT-drSJaIQCddbWKM"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is running! Send messages to your bot on Telegram.")
    application.run_polling()
if __name__ == "__main__":
    main()
