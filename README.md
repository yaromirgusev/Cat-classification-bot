# Cat classification bot 🐱🤖🧠

<p align="center">
      <img src="/src/logo.webp" alt="Project Logo" width="228">
</p>

## О проекте 📖

Cat classification bot - <a href="https://t.me/CatBreedDetectorBot">Telegram-бот</a> (@CatBreedDetectorBot) <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/2048px-Telegram_logo.svg.png" width="15" style="padding-right:10px; vertical-align:bottom;"> на Python <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Python_logo_51.svg/1200px-Python_logo_51.svg.png" width="15" style="padding-right:10px; vertical-align:bottom;">, который позволяет определить породу кота по фотографии, а также вывести
краткую информацию о ней. В процессе описания была дообучена модель ResNet50, используя PyTorch <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/PyTorch_logo_icon.svg/1200px-PyTorch_logo_icon.svg.png" width="15" style="padding-right:10px; vertical-align:bottom;"> и алгоритмы Transfer Learning на сборном датасете, находящемся в директории `Cats_lapkins`. Затем была написана логика бота, используя aiogram, а также было добавлено хранение данных, используя PostgreSQL <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/993px-Postgresql_elephant.svg.png" width="15" style="padding-right:10px; vertical-align:bottom;">. Для удобства использования и деплоя все было завернуто в Docker-контейнер <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Docker_%28container_engine%29_logo_%28cropped%29.png" width="25" style="padding-right:10px; vertical-align:bottom;">.

## Структура проекта 🗂️

-  **`Cats_lapkins`** - датасет
-  **`data.csv`** - файл с данными, использующимися для описаний пород
-  **`models`** - директория с обучением модели и самой моделью
-  **`handlers`** - директория с объявлением хэндлеров
-  **`config`** - директория с конфиг файлами (там должен быть ваш токен)
-  **`utils`** - директория с различными функциями, использующимися в логике бота
-  **`core`** - директория с загрузкой модели и созданием инстанса бота и диспетчера
-  **`main.py`** - основной файл, в котором запускается бот
-  **`Dockerfile`**, **`docker-compose.yaml`** и **`requirements.txt`**- файлы для создания и запуска контейнера

## Деплой 🚀
1. Создайте своего бота в <a href="https://t.me/BotFather">BotFather</a>.
2. Клонируйте репозиторий, после чего создайте директории `config` файл `ttoken.py`, в который нужно ввести 
```python
token = YOUR_TOKEN # токен вашего бота
host = 'db' if os.getenv("DOCKER", False) else '127.0.0.1'
user = 'postgres'
password = 'postgres'
db_name = 'postgres'
```
3. Установите <a href="https://www.docker.com/products/docker-desktop/">Docker Desktop</a> <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Docker_%28container_engine%29_logo_%28cropped%29.png" width="25" style="padding-right:10px; vertical-align:bottom;">
4. Напишите в консоли в данной директории
```bash
docker-compose build
```

```bash
docker-compose up
```

5. Все работает!

## Зависимости 💻
Если запускаете без Docker:
```bash
pip install -r requirements.txt
```

## Пример работы 🖼️

<p align="center">
<img src="https://github.com/yaromirgusev/Cat-classification-bot/assets/131535027/6e5ffa35-ac7a-43a1-850c-ae6f970ea5c9" width="600">
</p>
