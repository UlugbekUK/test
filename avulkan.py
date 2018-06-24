from telethon import TelegramClient, events

api_id = 217790
api_hash = 'b69bd04d4eb99526c6ca18157273dd01'
phone_number = '+998935770488'
client = TelegramClient('modem11', api_id, api_hash, update_workers=10, spawn_read_thread=False)
assert client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    myself = client.sign_in(phone_number, input('Enter code: '))


client.start()

@client.on(events.NewMessage)
def my_event_handler(event):
    if 'ping' in event.raw_text:
        event.reply('pong!')
