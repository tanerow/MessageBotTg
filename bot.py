from telethon import TelegramClient, events

api_id = 23246373
api_hash = 'daa39e9d5b1bc1261b0c3e27853205fc'
client = TelegramClient('my_session', api_id, api_hash)

keywords = ['монтаж', 'монтажер', 'монтажёр', 'екб', 'Екатеринбург', 'Екб', 'магнитогорск', 'мгн']
excluded_words = ['помогу', 'ищуработу', 'ютубшортс', 'рилс', 'вертикальные', 'шортсы', 'рилсы']
target_chat_id = -4734945370

@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text.lower()
    if any(word in text for word in keywords) and not any(bad in text for bad in excluded_words):
        await client.send_message(target_chat_id, f'📥 Сообщение из {event.chat.title}:\n\n{text}')

client.start()
client.run_until_disconnected()
