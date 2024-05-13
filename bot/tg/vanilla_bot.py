import os
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

# take environment variables from .env.
success = load_dotenv(dotenv_path='./../../.env')
print("Environment file loaded:", success)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.reply_text(update.message.text)


def main() -> None:
    application = Application.builder().token(os.getenv('TG_BOT_TOKEN')).build()

    # Handlers define how to respond to specific events
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until you press Ctrl-C
    application.run_polling()


if __name__ == '__main__':
    main()
