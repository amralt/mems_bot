from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
font = ImageFont.truetype("fonts\\TimesNewRomanRegular.ttf", size=72)



def create_lines(messsage: str):
    drawing_str = ''
    return_list = ['']

    max_len = 30
    len_line = 0
    index = 0
    for word in messsage.split():
        if len_line + len(word) + 1 <= max_len:
            len_line += len(word) + 1

            drawing_str = return_list[index]
            return_list[index] = drawing_str + ' ' + word

        else: 
            index += 1
            return_list.append('')

            len_line = 0    
    
    return return_list

def find_font_size(width: int):
    cont_chars = 30
    # 0.5 - кол-во пикселей на один пункт
    size = (width*2/cont_chars)
    return size




def create_classic_mem(text = 'зачем?', path = 'pics\\gigachad.jpg'):
    if text == None: text = 'ddddd'
    image = Image.open(path)
    image_back = Image.open('pics\\back.jpg')

    image = image.resize((545, 360))
    image_back.paste(image, (55, 55))
    # вставляю черный прямоугольник вместо букв
    clear_text_block = Image.new('RGB', (655,190), color=('#000000'))
    
    draw_text = ImageDraw.Draw(clear_text_block)
    draw_text.text((100, 100),text, font = font, fill = '#FFFFFF')
    image_back.paste(clear_text_block, (0,423))

    image_back.save('pics\\new.jpg', optimize = True, quality=90)

def create_gigachad_mem(text = 'потому что'):
    if text == None: text = ''
    giga_image = Image.open('pics\\gigachad.jpg')
    draw_text = ImageDraw.Draw(giga_image)
    draw_text.text((100, 800),text, font = font, fill='#FFFFFF')
    giga_image.save('pics\\new.jpg',optimize=True, quality=90)


def create_user_mem(text = 'дадададада', path = 'pics\\gigachad.jpg'):
    if text == None: text = ''
    image = Image.open(path)
    image.convert('RGB')
    font = ImageFont.truetype("fonts\\TimesNewRomanRegular.ttf", size=find_font_size(image.width))

    x, y = image.size

    # можно было бы написать функции для получения цвета целого участка
    r, g, b = image.getpixel((x*0.1, y*0.7))
    if 0.299 * r + 0.587 * g + 0.114 * b > 127.5:
        font_color = '#1C1C1C'
    else:
        font_color = '#FFFFFF'
    
    text_lines = create_lines(text)
    print(text_lines )

    text_y = y - 60 
    for line in text_lines[::-1]:
        draw_text = ImageDraw.Draw(image)
        draw_text.text((x*0.03, text_y), text = line, font = font, fill = font_color)

        text_y -= 60

    image.save('pics\\new.jpg', optimize=True, quality=90)
