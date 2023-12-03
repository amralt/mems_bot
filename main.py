import telebot
from telebot import types

from photo_redact import create_classic_mem, create_gigachad_mem, create_user_mem


# добавь библиотеку profanity-filter

# спрячь токен
token='6250744722:AAHpPDqy93oe9W0UmLPOezr_Mb8tsVHPhsE'
bot=telebot.TeleBot(token)

# TODO вывести класс в другой файл
class Mem():
    memsWithPhoto = {
        'Гигачад' : False,
        'Классика' : True,
        'Свой мем' : True,
    }

    def __init__(self, mem_type, isUserPhoto: bool, text, path) -> None:
        self.mem_type = mem_type
        self.isUserPhoto = isUserPhoto
        self.PhotoPath = path
        self.text = text
    
    def create_mem(self):
        choose_mem = {
            'Гигачад' : create_gigachad_mem(self.text),
            'Классика' : create_classic_mem(self.text, self.PhotoPath),
            'Свой мем' : create_user_mem(self.text, self.PhotoPath),
        }
        print(self.PhotoPath)
        choose_mem[self.mem_type]

mems = dict()
user_mem_type = dict()
# TODO сделать словарь с типами мемов для каждого пользователя

def download_photo(fileID, chat_id):
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f"pics\\{chat_id}_img.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    return f"pics\{chat_id}_img.jpg"

def create_choose_type():
    markup = types.ReplyKeyboardMarkup(True)
    button_0 = types.KeyboardButton("/Классика")
    button_1 = types.KeyboardButton("/Гигачад")
    button_2 = types.KeyboardButton("/Свой_мем")

    markup.add(button_0, button_1, button_2)

    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = create_choose_type()
    bot.send_message(message.chat.id, 'Добро пожаловать. Я бот для создания мемов. Выберите тип мема, отправьте фото с подписью. А взамен получите созданный мною мем', reply_markup = markup)
    

@bot.message_handler(commands = ['Свой_мем'])
def users_mem(message):
    user_mem_type[message.chat.id] = 'Свой мем'
    bot.send_message(message.chat.id, 'отправьте фото и подпись')

@bot.message_handler(commands = ['Классика'])
def users_mem(message):
    user_mem_type[message.chat.id] = 'Классика'
    bot.send_message(message.chat.id, 'отправьте фото и подпись')

@bot.message_handler(commands = ['Гигачад'])
def users_mem(message):
    user_mem_type[message.chat.id] = 'Гигачад'
    bot.send_message(message.chat.id, 'отправьте подпись')

@bot.message_handler(commands=['создать'])
def text_hand(message):
    if message.chat.id not in user_mem_type.keys():
        bot.send_message(message.chat.id, "ERROR: Вы не выбрали тип мема",)
        return 
    
    mem = mems[message.chat.id]
    mem.create_mem()

    with open('pics\\new.jpg', 'rb') as mem:
        bot.send_document(message.chat.id, document = mem)

    print(message.from_user.first_name)
    markup = create_choose_type()
    bot.send_message(message.chat.id, 'Выберите слудеющий тип мема', markup)




@bot.message_handler(content_types = ['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    path = download_photo(fileID, message.chat.id)

    if message.chat.id not in user_mem_type.keys():
        bot.send_message(message.chat.id, "ERROR: Вы не выбрали тип мема",)
        return 

    if Mem.memsWithPhoto[user_mem_type.get(message.chat.id)] == False:
        bot.send_message(message.chat.id, "ERROR: ВЫбранный тип мема не подходит",)
        return
    
    user_mem = Mem(user_mem_type[message.chat.id], True, message.text, path)
    mems[message.chat.id] = user_mem

    markup = types.ReplyKeyboardMarkup(True).add(types.KeyboardButton('/создать'))
    bot.send_message(message.chat.id, "Мем готов к созданию", reply_markup = markup)
 
#  TODO сделать проверку на выбранный тип мема. Сделать хендлер на просто текст и тип мема - гигачад
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text[0] =='/': return

    current_mem = mems.get(message.chat.id)
    if current_mem.isUserPhoto: 
        current_mem.text = message.text
        bot.send_message(chat_id= message.chat.id, text='текст изменен')
    

    
bot.infinity_polling()