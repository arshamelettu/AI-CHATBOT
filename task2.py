from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from transformers import pipeline
llm_model = pipeline("text-generation", model="distilgpt2")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your AI assistant. Ask me anything!")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"User said: {user_message}")
    await update.message.reply_text(f"You said: {user_message}")
# Generate a response using the LLM (DistilGPT-2)
async def generate_ai_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"User said: {user_message}")
    response = llm_model(user_message, max_length=100, num_return_sequences=1)
    await update.message.reply_text(response[0]['generated_text'])
def main():
    TOKEN = "8121814836:AAHqx3Qnb7Ne_Kat85xT-drSJaIQCddbWKM"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_ai_response))
    print("Bot is running! Send messages to your bot on Telegram.")
    application.run_polling()
if __name__ == "__main__":
    main()

