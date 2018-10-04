import keyboard
from telegram.ext import Updater, CommandHandler

# Record events until 'esc' is pressed.
# recorded = keyboard.record(until='esc')
# Then replay back at three times the speed.
# print(recorded[0].to_json)

def getKey(event):
    if event.event_type is "down":
        print(event)
        print(type(event))
        print(event.name)
        print(event.event_type)


# keyboard.hook(getKey,suppress=False)

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('612595129:AAEbSDNaQfep09oiN7-sYdRXQBoFzgCzN5w')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()


# keyboard.wait() 