from PIL import Image
import torchvision.transforms as transforms
import timm
import torch
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import ttoken
from aiogram import F
from aiogram.types import Message
from aiogram.enums import ParseMode
import os
import pandas as pd

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
data = pd.read_csv('data.csv', encoding='windows-1251')

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
        top1=-10000
        top2=-10000
        top3=-10000
        top1_i = 0
        top2_i = 0
        top3_i = 0
        for i, j in enumerate(output[0]):
            if j > top1:
                top1=j
                top1_i = i
            elif j > top2 and j < top1 :
                top2 = j
                top2_i = i
            elif j > top3 and j < top2:
                top3 = j
                top3_i = i

    return top1_i, top2_i, top3_i

model2 = torch.load('complete_model2_00001.pth', map_location=device)
model2.eval()

# image_path = 'test.jpg'
# prediction = predict_image(image_path, model2, device)
# print(f'Predicted class index: {prediction}')
# print(names[int(prediction)])

logging.basicConfig(level=logging.INFO)
bot = Bot(token=ttoken.token)
dp = Dispatcher()

@dp.message(F.photo)
async def download_photo(message: types.Message, bot: Bot):
    temp_dir = '/tmp' if os.name != 'nt' else 'C:\\temp'
    os.makedirs(temp_dir, exist_ok=True)  
    destination = os.path.join(temp_dir, f"{message.photo[-1].file_id}.jpg")
    
    await bot.download(message.photo[-1], destination=destination)
    
    if os.path.exists(destination):
        prediction = predict_image(destination, model2, device)
        top1 = data['names'][prediction[0]].lower()
        top2 = data['names'][prediction[1]].lower()
        top3 = data['names'][prediction[2]].lower()
        await message.answer(f'Вероятнее всего, это <b>{top1}</b> или <b>{top2}</b> или <b>{top3}</b>',
                             parse_mode=ParseMode.HTML)
    else:
        await message.answer("Не удалось загрузить изображение.")

    os.remove(destination)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())