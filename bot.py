from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel, PeerChat
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

api_id = 23246373  # Ваш api_id
api_hash = 'daa39e9d5b1bc1261b0c3e27853205fc'  # Ваш api_hash
client = TelegramClient('my_session', api_id, api_hash)

# Ключевые слова и исключения
keywords = ['монтаж', 'монтажер', 'монтажёр', 'екб', 'екатеринбург', 'магнитогорск', 'мгн']
excluded_words = ['помогу', 'ищуработу', 'ютубшортс', 'рилс', 'вертикальные', 'шортсы', 'рилсы']

# Чат для пересылки сообщений
target_chat_id = -4734945370  # Замените на свой ID

@client.on(events.NewMessage)
async def handler(event):
    try:
        # Получаем ID чата, откуда пришло сообщение
        sender = event.message.to_id
        sender_id = None

        if isinstance(sender, PeerChannel):
            sender_id = -sender.channel_id  # каналы/супергруппы: отрицательный ID
        elif isinstance(sender, PeerChat):
            sender_id = sender.chat_id  # обычные чаты: положительный ID

        # Игнорируем сообщения из целевого чата, куда мы отправляем
        if sender_id == target_chat_id:
            return

        # Обработка текста
        text = event.raw_text.lower()
        if any(word in text for word in keywords) and not any(bad in text for bad in excluded_words):
            await client.send_message(
                target_chat_id,
                f'📥 Сообщение из {event.chat.title or "неизвестного чата"}:\n\n{text}'
            )
            logging.info(f"Сообщение переслано из {event.chat.title}")
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения: {e}")

# Запуск клиента
client.start()
client.run_until_disconnected()
