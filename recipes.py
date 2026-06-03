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
    pass


class DietaryRecipe(Recipe):
    pass
