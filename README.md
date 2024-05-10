# Cat classification bot 🐱🤖🧠

<p align="center">
      <img src="https://i.ibb.co/1K7DDsf/logo.webp" alt="Project Logo" width="228">
</p>

## О проекте 📖

Cat classification bot - <a href="https://t.me/CatBreedDetectorBot">бот</a> (@CatBreedDetectorBot) для Telegram <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/2048px-Telegram_logo.svg.png" width="15" style="padding-right:10px; vertical-align:bottom;">, который позволяет определить породу кота по фотографии, а также вывести
краткую информацию о ней. В процессе описания была дообучена модель ResNet50, используя PyTorch <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/PyTorch_logo_icon.svg/1200px-PyTorch_logo_icon.svg.png" width="15" style="padding-right:10px; vertical-align:bottom;"> и алгоритмы Transfer Learning на сборном датасете, находящемся в папке `Cats_lapkins`. Затем была написана логика бота, используя aiogram, а также было добавлено хранение данных, используя PostgreSQL <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/993px-Postgresql_elephant.svg.png" width="15" style="padding-right:10px; vertical-align:bottom;">. Для удобства использования и деплоя все было обернуто в Docker <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Docker_%28container_engine%29_logo_%28cropped%29.png" width="25" style="padding-right:10px; vertical-align:bottom;"> контейнер.

## Описание 📝

-  **`Cats_lapkins`** - датасет
-  **`cats_models.ipynb`** - ноутбук с дообучением модели
-  **`complete_model2_00001.pth`** - файл с дообученной моделью, к которой обращется бот
-  **`data.csv`** - файл с данными, использующимися для описаний пород
-  **`main.py`** - основной файл, в котором запускается бот и описана работа с PostgreSQL
-  **`Dockerfile`**, **`docker-compose.yaml`** и **`requirements.txt`**- файлы для создания и запуска контейнера

## Деплой 🚀
1. Создайте своего бота в BotFather <a href="https://t.me/BotFather">BotFather</a>.
2. Загрузите файлы `main.py`, `Dockerfile`, `docker-compose.yaml`, `requirements.txt` и `complete_model2_00001.pth`, после чего создайте в той же директории файл `ttoken.py`, в который нужно ввести 
```python
token = YOUR_TOKEN #токен вашего бота
user = 'postgres'
password = 'postgres'
db_name = 'postgres'
```
3. Установите Docker Desktop <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Docker_%28container_engine%29_logo_%28cropped%29.png" width="25" style="padding-right:10px; vertical-align:bottom;">
4. Напишите в консоли в данной папке
```bash
docker-compose build
```
```bash
docker-compose up
```
5. Все работает!

## Примеры работы 🖼️

<p align="center">
      <img src="https://i.ibb.co/P9jkZ4v/image.png" alt="Project Logo">
</p>
