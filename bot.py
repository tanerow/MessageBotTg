from telethon import TelegramClient, events
import logging

logging.basicConfig(level=logging.INFO)

api_id = 23246373
api_hash = 'daa39e9d5b1bc1261b0c3e27853205fc'
client = TelegramClient('my_session', api_id, api_hash)

keywords = ['монтаж', 'монтажер', 'монтажёр', 'екб', 'екатеринбург', 'магнитогорск', 'мгн']
excluded_words = ['помогу', 'ищуработу', 'ютубшортс', 'рилс', 'вертикальные', 'шортсы', 'рилсы']

target_chat_id = -4734945370
ignored_chat_ids = {target_chat_id}

@client.on(events.NewMessage)
async def handler(event):
    try:
        chat = await event.get_chat()
        chat_id = event.chat_id

        # Пропускаем сообщения из чата-получателя
        if chat_id in ignored_chat_ids:
            return

        text = event.raw_text.lower()

        # Пропускаем сообщения, уже помеченные как пересланные ботом
        if text.startswith("📥 сообщение из") or text.startswith("📥 сообщение от"):
            return

        if any(word in text for word in keywords) and not any(bad in text for bad in excluded_words):
            title = getattr(chat, "title", "личных сообщений")
            await client.send_message(
                target_chat_id,
                f'📥 Сообщение из {title}:\n\n{text}'
            )
            logging.info(f"Переслано сообщение из {title}")
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения: {e}")

client.start()
client.run_until_disconnected()
