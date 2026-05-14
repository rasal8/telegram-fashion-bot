from telegram.ext import Updater, CommandHandler

BOT_TOKEN = "8754129984:AAF8OGD1odlxGJSJDTsePdudREpAQW44y_Y"

PRODUCTS = {
    "dress001": "✨ Korean Floral Dress\n\n💰 Price: ₹999\n\n🛍 Shop Now 👇\nhttps://fktr.in/YtcWjZB",

    "top001": "✨ Korean White Top\n\n💰 Price: ₹799\n\n🛍 Shop Now 👇\nhttps://your-affiliate-link.com"
}

def start(update, context):

    code = "default"

    if context.args:
        code = context.args[0]

    product = PRODUCTS.get(code)

    if product:
        update.message.reply_text(product)
    else:
        update.message.reply_text("Product not found.")

updater = Updater(BOT_TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

print("Bot Running...")

updater.start_polling()
updater.idle()
