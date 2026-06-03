class Ingredient: ## 1.1 из ТЗ

    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}" # Мука: 500.0 г

    def __repr__(self):
        return f"Ingredient({self.name!r}, {self.quantity}, {self.unit!r})" # Ingredient('Мука', 500.0, 'г') !r для кавычек

    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name and self.unit == other.unit
        return False


class Recipe:
    
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        for item in self.ingredients:
            if item == ingredient:
                item.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)


    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0


    def scale(self, ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        
        new_ingredients = []
        for ingredient in self.ingredients:
            new_ingredients.append(
                Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)
            )
        return Recipe(self.title, new_ingredients)



    def __len__(self):
        return len(self.ingredients)


    def __str__(self):
        return f"Ingredients for {self.title}: {' '.join(str(ingredient) for ingredient in self.ingredients)}"


class ShoppingList:

    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")

        scaled_recipe = recipe.scale(portions)
        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))


    def remove_recipe(self, title):
        new_items = []
        for item in self._items:
            if item[1] != title:
                new_items.append(item)
        self._items = new_items


    def get_list(self):
        total_dict_to_buy = {}

        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in total_dict_to_buy:
                total_dict_to_buy[key] = total_dict_to_buy[key] + ingredient.quantity
            else:
                total_dict_to_buy[key] = ingredient.quantity


        result = []
        for key in total_dict_to_buy:
            name, unit = key
            quantity = total_dict_to_buy[key]
            result.append(Ingredient(name, quantity, unit))

        result.sort(key=lambda in_res: in_res.name)

        return result


    def __add__(self, other):
        new_list = ShoppingList()

        for item in self._items:
            new_list._items.append(item)

        for item in other._items:
            new_list._items.append(item)

        return new_list


class DietaryRecipe(Recipe):

    def __init__(self, title, diet_type, ingredients=None):
        if ingredients is None:
            ingredients = []
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio):
        new_recipe = super().scale(ratio)
        return DietaryRecipe(new_recipe.title, self.diet_type, new_recipe.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"


