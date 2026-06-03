# Система управления рецептами

Позволяет хранить ингредиенты и рецепты, масштабировать порции, собирать список покупок из нескольких блюд и работать с диетическими рецептами.

## Установка

Клонируйте репозиторий и установите зависимости:

```bash
git clone https://github.com/Ynuty/TP_HW2
cd C:\Users\msoko\.vscode\projects\TP_HW2
pip install -r requirements.txt
```

Рекомендуется использовать виртуальное окружение:

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Использование

### Запуск тестов

Из корня проекта:

```bash
pytest
```

Если команда `pytest` не находится, укажите Python из окружения:

```bash
python -m pytest
```

**Windows (без активации venv):**

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Подробный вывод:

```bash
python -m pytest -v
```

Все тесты лежат в файле `test_recipes.py`.

### Модули проекта

Основной код — в `recipes.py`:

- `Ingredient` — продукт с количеством и единицей измерения;
- `Recipe` — рецепт блюда;
- `ShoppingList` — список покупок по нескольким рецептам;
- `DietaryRecipe` — рецепт с диетической меткой.


## Структура проекта

```
TP_HW2/
├── recipes.py              # Классы Ingredient, Recipe, ShoppingList, DietaryRecipe
├── test_recipes.py         # Тесты pytest
├── requirements.txt        # Зависимости
├── README.md
├── .gitignore
└── data/
    └── HW_2_OOP_Testing_Git.ipynb   # Условие задания 

```


## Автор

ФИО: Соколов Михаил Алексеевич 
Группа: ББИ2501
