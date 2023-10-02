# Тестовое задание для HardCode.
Простое API на Django Rest Framework + Django для вывода информации о продуктах, уроках и статистике просмотра уроков пользователями.
# Установка
* Копируем репозиторий
* Создаем виртуальное окружение `python -m venv .venv`
* Устанавливаем зависимости `pip install -r requirements.txt`
# Доступные endpoint API
* `/user/<int:user_id>/lessons/` - вывод списка всех уроков по всем продуктам пользователя
* `/user/<int:user_id>/product/<int:product_id>/` - вывод списка всех уроков по выбранному продукту пользователя
* `/statistics/` - вывод статистики по продуктам
# ТЗ:
[Тестовое задание Стажер Python](https://docs.google.com/document/d/1xiQCpPiek2nH47yT3WU4jkpQ-b8aX9ZbFkcxOQCBLb4/edit)
