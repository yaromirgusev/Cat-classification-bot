import torch
from aiogram import Bot, Dispatcher
from config.ttoken import token
import logging


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model2 = torch.load('models/complete_model2_00001.pth', map_location=device)
model2.eval()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("bot.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)



bot = Bot(token=token)
dp = Dispatcher()

user_results = {}