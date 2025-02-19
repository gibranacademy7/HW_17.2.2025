import recipe
from Question_3 import Question3
from typing import override

class Q3A(Question3):

    @override
    def q3_a(self):
        print(f"{"-"*50} Question 3a: {"-"*50}")
        print("🛒 Ingredients in Pancakes Recipe:")
        for ingredient in recipe.recipe1:
            print(f"{" " * 5}- {ingredient}")
        return "And that's it!!! (I'm returning this just because i don't want to get a None...)"

    @override
    def q3_b(self):
        pass

    @override
    def q3_c(self):
        pass

