# SantehFast
## В демонстративных целях в проекте оставлены такие файлы и директории, как db.sqlite3, static, staticfiles, media
### Инструкция по запуску приложения:
```
git clone https://github.com/Cotang01/SantehFast.git
```
```
cd SantehFast
```
#### Настройка виртуального окружения для Windows (уже должен быть предустановлен python версии 3.11)
```
python -m venv venv
call venv/Scripts/activate
```
#### Настройка виртуального окружения для Linux (уже должен быть предустановлен python версии 3.11)
```
python3 -m venv venv
source venv/bin/activate
```
```
cd SantehFast
```
#### Установка зависимостей через pip
```
pip install -r requirements.txt
```
#### Установка зависимостей через poetry
```
pip install poetry
poetry install
```
```
python manage.py runserver
```
