import openai
import telebot
from telebot import TeleBot

openai.api_key = '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'
bot: TeleBot = telebot.TeleBot('5628648630:AAEhx8TpSipwoIIH4tdUDqlMTVlx-RFV8Zg')


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(message.from_user.id, text=response['choices'][0]['text'])


#print(response)


# text=response['choices'][0]['text'])


bot.polling()
