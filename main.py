import telebot
from telebot import types
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from photo_redact import create_classic_mem, create_gigachad_mem

# спрячь токен
token='6250744722:AAHpPDqy93oe9W0UmLPOezr_Mb8tsVHPhsE'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(True)
    button_0 = types.KeyboardButton("Классика")
    button_1 = types.KeyboardButton("Гигачад")
    button_2 = types.KeyboardButton("Свой мем")

    markup.add(button_0, button_1, button_2)
    bot.send_message(message.chat.id, 'Добро пожаловать. Я бот для создания мемов. Отправьте фото и подпись, а я создам мем', reply_markup = markup)
    
@bot.message_handler(content_types = ['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("pics\\user_img.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    if mem_type == 'classic':
        if message.caption != None:create_classic_mem(message.caption)
        else:create_classic_mem()
    # bot.send_photo(message.chat.id, photo='pics\\new.jpg')
    with open('pics\\new.jpg', 'rb') as f:
        bot.send_document(message.chat.id,document=f)

# создай нормальные действия на кнопки, а не обработку текста
@bot.message_handler(content_types=['text'])
def text_hand(message):
    print(message.from_user.first_name)
    global mem_type
    if message.text == 'Классический мем':
        mem_type = 'classic'
    elif message.text == 'Гигачад':
        # вот тут возникает проблема с тем, что данный тип мемов не имеет привязанной картинки
        mem_type = 'gigachad'
    else:
        if mem_type == 'gigachad':
            create_gigachad_mem(message.text)
            with open('pics\\new.jpg', 'rb') as f:
                bot.send_document(message.chat.id,document=f)
            # bot.send_photo(message.chat.id, 'pics\\new.jpg')

bot.infinity_polling()