'''
@app.on_message(filters.command(["stopmeet"]))
def start(client, message):
    client.send_message(chat_id=message.chat.id,text=f"Hi {message.from_user.first_name}")
    client.send_message(chat_id = message.chat.id, text = "where are you from")

@app.on_message(filters.text)
def echo(client, message):
    place=message.text
    client.send_message(chat_id = message.chat.id, text = "you are from"+place)

app.run()
'''