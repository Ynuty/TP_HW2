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
    pass
    

class ShoppingList:
    pass


class DietaryRecipe(Recipe):
    pass
