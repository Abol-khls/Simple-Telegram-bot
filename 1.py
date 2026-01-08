import logging
from bs4 import BeautifulSoup
from lxml import etree
import requests
from telegram import ForceReply,Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def wam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"You are {user.mention_html()}!",
        
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text(
            "❗ Please enter a coin name.\n\n"
            "Correct format:\n"
            "/price <coin-name>\n\n"
            "Examples:\n"
            "/price bitcoin\n"
            "/price solana"
        )
        return


    coin = context.args[0].lower()
    url = f"https://coinmarketcap.com/currencies/{coin}/"

    response = requests.get(url)

    if response.status_code == 404:
        await update.message.reply_text("page not found!")
        return

    soup = BeautifulSoup(response.content, "lxml")
    dom = etree.HTML(str(soup))

    try:
        price = dom.xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div/section/div/div[2]/span[1]/text()')[0]
    except:
        await update.message.reply_text("cant find price!")
        return

    await update.message.reply_html(
        f"<b>price{coin.capitalize()}</b>: {price}"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

    
def main() -> None:
    application = Application.builder().token("8331706805:AAHhD1Cm9DwjKJN8dQ6iw34sLIbEwPKutQQ").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("who_am_i", wam))

    application.add_handler(CommandHandler("price", price))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()