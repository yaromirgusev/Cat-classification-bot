from PIL import Image
import torchvision.transforms as transforms
import timm
import torch
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
import ttoken
print(ttoken.token)


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
names = ['Абиссинская кошка',
 'Американская короткошерстная кошка',
 'Американский бобтейл',
 'Американский керл',
 'Балинезийская кошка',
 'Бамбино',
 'Бенгальская кошка',
 'Бирманская кошка',
 'Бомбейская кошка',
 'Британская длинношерстная кошка',
 'Британская короткошерстная кошка',
 'Бурманская кошка',
 'Бурмилла',
 'Гавана браун',
 'Гималайская кошка',
 'Девон-рекс',
 'Донской сфинкс',
 'Европейская короткошерстная кошка',
 'Египетская мау',
 'Канадский сфинкс',
 'Корат',
 'Корниш-рекс',
 'Курильский бобтейл',
 'Лаперм',
 'Манчкин',
 'Мейн-кун',
 'Меконгский бобтейл',
 'Мэнкс',
 'Невская маскарадная кошка',
 'Немецкий рекс',
 'Нибелунг',
 'Норвежская лесная кошка',
 'Ориентальная кошка',
 'Оцикет',
 'Персидская кошка',
 'Петерболд',
 'Пиксибоб',
 'Рагамаффин',
 'Русская голубая кошка',
 'Рэгдолл',
 'Саванна (Ашера)',
 'Селкирк-рекс',
 'Сиамская кошка',
 'Сибирская кошка',
 'Сингапурская кошка',
 'Скукум',
 'Сноу-шу',
 'Сококе',
 'Сомалийская кошка',
 'Тайская кошка',
 'Тойгер',
 'Тонкинская кошка',
 'Турецкая ангора',
 'Турецкий ван',
 'Чаузи',
 'Шантильи-тиффани',
 'Шартрез',
 'Шотландская вислоухая кошка',
 'Шотландская прямоухая кошка',
 'Экзотическая кошка',
 'Эльф',
 'Японский бобтейл']


def predict_image(image_path, model, device):
    image = Image.open(image_path)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image_tensor = transform(image).unsqueeze(0)

    image_tensor = image_tensor.to(device)

    with torch.no_grad():
        output = model(image_tensor)
        prediction = output.argmax()

    return prediction


model2 = torch.load('complete_model2_00001.pth', map_location=device)
model2.eval()

image_path = 'test.jpg'
prediction = predict_image(image_path, model2, device)
print(f'Predicted class index: {prediction}')
print(names[int(prediction)])