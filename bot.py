import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

PRODUCTS = {
    "dress001": {
        "message": "✨ Korean Floral Dress\n\n💰 Price: ₹999\n\n🛍 Shop Now 👇\nhttps://your-affiliate-link.com"
    },

    "top001": {
        "message": "✨ Korean White Top\n\n💰 Price: ₹799\n\n🛍 Shop Now 👇\nhttps://your-affiliate-link.com"
    },

    "summer001": {
        "message": "✨ Summer Korean Outfit\n\n💰 Price: ₹1199\n\n🛍 Shop Now 👇\nhttps://your-affiliate-link.com"
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
        await update.message.reply_text(
            "✨ Welcome to Fashion Outfit Bot\n\nSend a valid Pinterest product link."
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Running...")
app.run_polling()
