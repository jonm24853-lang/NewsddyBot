import os
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

SOURCE_CHANNEL = "https://t.me/AjaNews"


def get_news():
    url = "https://t.me/s/AjaNews"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.text


def main():
    if not BOT_TOKEN or not CHANNEL_ID:
        raise ValueError("BOT_TOKEN أو CHANNEL_ID غير موجود")

    bot = Bot(token=BOT_TOKEN)

    print("Daily News Bot is running...")
    print(f"Source: {SOURCE_CHANNEL}")
    print(f"Target: {CHANNEL_ID}")

    news = get_news()

    print(f"تم جلب الأخبار من {SOURCE_CHANNEL}")
    print(f"حجم البيانات: {len(news)}")


if __name__ == "__main__":
    main()
