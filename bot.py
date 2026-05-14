import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8754129984:AAF8OGD1odlxGJSJDTsePdudREpAQW44y_Y"

PRODUCTS = {
    "dress001": {
        "message": "✨ Korean Floral Dress\n\n💰 Price: ₹999\n\n🛍 Shop Now 👇\nhttps://your-affiliate-link.com"
    },

    "top001": {
        "message": "✨ Korean White Top\n\n💰 Price: ₹799\n\n🛍 Shop Now 👇\nhttps://your-affiliate-link.com"
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    code = "default"

    if context.args:
        code = context.args[0]

    product = PRODUCTS.get(code)

    if product:
        await update.message.reply_text(product["message"])
    else:
        await update.message.reply_text("Product not found.")

async def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Running...")

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
