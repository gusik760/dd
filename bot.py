import telebot

API_TOKEN = '8132196258:AAGRDvK4rJgSac8yyNkmUEYKfekyw2egda4'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if message.reply_to_message: 
    chat_id = message.chat.id 
    user_id = message.reply_to_message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status 
if user_status == 'administrator' or user_status == 'creator':
    bot.reply_to(message, "Невозможно забанить администратора.")
    bot.ban_chat_member(chat_id, user_id)
bot.infinity_polling()

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.ff) 

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)