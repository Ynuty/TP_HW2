import pytest

from recipes import Ingredient, Recipe, ShoppingList


#  2.1 Ingredient 


def test_ingredient_create(): #Правильная инициальзация названий
    ingr = Ingredient("Мука", 500, "г")
    assert ingr.name == "Мука"
    assert ingr.quantity == 500.0
    assert ingr.unit == "г"


def test_ingredient_str(): #Правильный вывод
    ingr = Ingredient("Мука", 500, "г")
    assert str(ingr) == "Мука: 500.0 г"


def test_ingredient_eq_same_name_and_unit(): #Равные ингридиенты и unit
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Мука", 1, "г")
    assert a == b


def test_ingredient_eq_different_name(): #Разные ингридиенты
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Сахар", 500, "г")
    assert a != b


def test_ingredient_eq_different_unit(): #Разные unit
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Мука", 500, "кг")
    assert a != b


#  2.2 Recipe 


def test_recipe_create(): #Правильная инициальзация названий
    ingr = Ingredient("Мука", 100, "г")
    recipe = Recipe("Пицца", [ingr])
    assert recipe.title == "Пицца"
    assert recipe.ingredients == [ingr]


def test_recipe_add_new_ingredient(): #Новый ингридиент успешно добавляется в рецепт
    recipe = Recipe("Пицца", [])
    recipe.add_ingredient(Ingredient("Мука", 100, "г"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 100


def test_recipe_add_merge_same_ingredient():#Если добавляется ингредиент, который уже есть (совпадают `name` и `unit`), его количество суммируется с существующим, а не создается дубликат
    recipe = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    recipe.add_ingredient(Ingredient("Мука", 50, "г"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 150


def test_recipe_scale_new_object():#Возвращается новый объект `Recipe`, а не изменяется исходный
    recipe = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    scaled = recipe.scale(2)
    assert scaled is not recipe
    assert isinstance(scaled, Recipe)
    assert recipe.ingredients[0].quantity == 100


def test_recipe_scale_multiplies():#Количество каждого ингредиента умножается на переданный коэффициент
    recipe = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    scaled = recipe.scale(2)
    assert scaled.ingredients[0].quantity == 200


def test_recipe_scale_bad_ratio():#При передаче `ratio` <= 0 выбрасывается исключение `ValueError`
    recipe = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    with pytest.raises(ValueError):
        recipe.scale(0)


def test_recipe_len():#Возвращается количество уникальных ингредиентов в рецепте
    recipe = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    recipe.add_ingredient(Ingredient("Сыр", 200, "г"))
    recipe.add_ingredient(Ingredient("Мука", 50, "г"))
    assert len(recipe) == 2



#  2.3 ShoppingList 


def test_shopping_list_add_recipe():#Рецепт успешно добавляется в список покупок
    recipe = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    shop = ShoppingList()
    shop.add_recipe(recipe, 2)
    assert len(shop._items) == 1
    assert shop._items[0][1] == "Пицца"
    assert shop._items[0][0].quantity == 200


def test_shopping_list_add_recipe_bad_portions():#При передаче `portions` <= 0 выбрасывается исключение `ValueError`
    recipe = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    shop = ShoppingList()
    with pytest.raises(ValueError):
        shop.add_recipe(recipe, 0)


def test_shopping_list_remove_recipe():#Удаляются все ингредиенты, относящиеся к рецепту с указанным названием
    r1 = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    r2 = Recipe("Паста", [Ingredient("Сыр", 50, "г")])
    shop = ShoppingList()
    shop.add_recipe(r1, 1)
    shop.add_recipe(r2, 1)
    shop.remove_recipe("Пицца")
    assert len(shop._items) == 1
    assert shop._items[0][1] == "Паста"


def test_shopping_list_remove_recipe_not_found():#Если рецепта с таким названием нет, ничего не происходит
    recipe = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    shop = ShoppingList()
    shop.add_recipe(recipe, 1)
    shop.remove_recipe("Суп")
    assert len(shop._items) == 1


def test_shopping_list_get_list_sum():#Одинаковые ингредиенты из разных рецептов суммируются
    r1 = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    r2 = Recipe("Паста", [Ingredient("Мука", 50, "г")])
    shop = ShoppingList()
    shop.add_recipe(r1, 1)
    shop.add_recipe(r2, 1)
    result = shop.get_list()
    assert result[0].name == "Мука"
    assert result[0].quantity == 150


def test_shopping_list_get_list_sorted():#Возвращаемый список отсортирован по названию ингредиента
    r1 = Recipe("A", [Ingredient("Яйца", 2, "шт")])
    r2 = Recipe("B", [Ingredient("Мука", 100, "г")])
    shop = ShoppingList()
    shop.add_recipe(r1, 1)
    shop.add_recipe(r2, 1)
    result = shop.get_list()
    assert result[0].name == "Мука"
    assert result[1].name == "Яйца"


def test_shopping_list_add_operator():#Два списка покупок корректно объединяются в новый список
    r1 = Recipe("Пицца", [Ingredient("Мука", 100, "г")])
    r2 = Recipe("Паста", [Ingredient("Сыр", 50, "г")])
    a = ShoppingList()
    b = ShoppingList()
    a.add_recipe(r1, 1)
    b.add_recipe(r2, 1)
    count_a = len(a._items)
    count_b = len(b._items)
    total = a + b
    assert len(total._items) == count_a + count_b
    assert len(a._items) == count_a
    assert len(b._items) == count_b


