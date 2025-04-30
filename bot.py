from telethon import TelegramClient, events
import logging
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)

api_id = 23246373
api_hash = 'daa39e9d5b1bc1261b0c3e27853205fc'
session_name = os.getenv("SESSION_NAME", "railway_session")  # можно задавать через переменные окружения
client = TelegramClient(session_name, api_id, api_hash)

keywords = ['монтаж', 'монтажер', 'монтажёр', 'екб', 'екатеринбург', 'екб', 'магнитогорск', 'мгн']
excluded_words = ['помогу', 'ищуработу', 'ютубшортс', 'рилс', 'вертикальные', 'шортсы', 'рилсы']
target_chat_id = -4734945370  # ID чата, куда пересылаем сообщения

@client.on(events.NewMessage)
async def handler(event):
    try:
        # Исключаем пересылку из целевого чата
        if event.chat_id == target_chat_id:
            return

        text = event.raw_text.lower()

        # Проверяем ключевые и исключающие слова
        if any(word in text for word in keywords) and not any(bad in text for bad in excluded_words):
            await client.send_message(target_chat_id, f'📥 Сообщение из {event.chat.title}:\n\n{text}')
            logging.info(f"Сообщение переслано из {event.chat.title}")
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения: {e}")

client.start()
client.run_until_disconnected()
