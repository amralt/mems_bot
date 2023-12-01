from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
def create_classic_mem(text = 'зачем?'):
    # 655*613 - размеры фоновой картинки 55 - отступ внутренней картинки
    image = Image.open("pics\\user_img.jpg")
    image_back = Image.open('pics\\back.jpg')
    #new_size = (512, 512*height//width)
    image = image.resize((545, 360))
    image_back.paste(image, (55, 55))
    # вставляю черный прямоугольник вместо букв
    clear_text_block = Image.new('RGB', (655,190), color=('#000000'))
    # создание объекта шрифта 
    # можно в будущем добавить возможность выбора шрифта
    font = ImageFont.truetype("fonts\TimesNewRomanRegular.ttf", size=72)
    draw_text = ImageDraw.Draw(clear_text_block)
    draw_text.text((100, 100),text,font=font,fill='#FFFFFF')
    image_back.paste(clear_text_block, (0,423))
    # Сохраняем изображение
    image_back.save('pics\\new.jpg',optimize=True, quality=90)

def create_gigachad_mem(text = 'потому что'):
    giga_image = Image.open('pics\\gigachad.jpg')
    draw_text = ImageDraw.Draw(giga_image)
    font = ImageFont.truetype("fonts\TimesNewRomanRegular.ttf", size=72)
    draw_text.text((100, 800),text,font=font,fill='#FFFFFF')
    giga_image.save('pics\\new.jpg',optimize=True, quality=90)