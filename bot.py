from telethon import TelegramClient, events
import logging

# Настройка логирования для отслеживания ошибок
logging.basicConfig(level=logging.INFO)

api_id = 23246373  # Ваш api_id
api_hash = 'daa39e9d5b1bc1261b0c3e27853205fc'  # Ваш api_hash
client = TelegramClient('my_session', api_id, api_hash)

keywords = ['монтаж', 'монтажер', 'монтажёр', 'екб', 'екатеринбург', 'екб', 'магнитогорск', 'мгн']
excluded_words = ['помогу', 'ищуработу', 'ютубшортс', 'рилс', 'вертикальные', 'шортсы', 'рилсы']
target_chat_id = -4734945370  # замените на нужный ID чата, куда будут пересылаться сообщения

@client.on(events.NewMessage)
async def handler(event):
    try:
        text = event.raw_text.lower()
        # Проверяем, содержится ли одно из ключевых слов, и нет ли исключённых слов
        if any(word in text for word in keywords) and not any(bad in text for bad in excluded_words):
            # Пересылаем сообщение в целевой чат
            await client.send_message(target_chat_id, f'📥 Сообщение из {event.chat.title}:\n\n{text}')
            logging.info(f"Сообщение переслано из {event.chat.title}")
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения: {e}")

client.start()
client.run_until_disconnected()
