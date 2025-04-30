from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

api_id = 23246373
api_hash = 'daa39e9d5b1bc1261b0c3e27853205fc'

keywords = ['монтаж', 'монтажер', 'монтажёр', 'монтажёр']
exclude_words = ['вакансия', 'ищу', 'ищем', 'резюме']
target_chat_id = -4734945370

client = TelegramClient('my_session', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    message_text = event.raw_text.lower()
    if any(word in message_text for word in keywords) and not any(exclude in message_text for exclude in exclude_words):
        await client.send_message(target_chat_id, f'Сообщение из {event.chat.title}:')

{event.raw_text}')

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        phone = input("Введите номер телефона (в формате +7...): ")
        await client.send_code_request(phone)
        code = input("Введите код из Telegram: ")
        try:
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            password = input("🔐 Введите пароль от двухфакторной авторизации: ")
            await client.sign_in(password=password)

    print("✅ Бот запущен. Ожидаем сообщения...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
