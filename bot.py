# bot.py
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import os

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
keywords = ['монтаж', 'монтажер', 'монтажёр', 'екб', 'Екатеринбург', 'Екб', 'магнитогорск', 'мгн']
exclude_words = ['помогу', 'ищуработу', 'ютубшортс', 'рилс', 'вертикальные', 'шортсы', 'рилсы']
target_chat_id = int(os.environ['TARGET_CHAT_ID'])

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    message_text = event.raw_text.lower()
    if any(word in message_text for word in keywords):
        if not any(excl in message_text for excl in exclude_words):
            await client.send_message(target_chat_id, f'Сообщение из {event.chat.title}:\n\n{event.raw_text}')

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        phone = os.environ['PHONE']
        await client.send_code_request(phone)
        code = input("Введите код из Telegram: ")
        try:
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            password = os.environ['TWOFACTOR_PASSWORD']
            await client.sign_in(password=password)

    print("✅ Бот запущен")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())