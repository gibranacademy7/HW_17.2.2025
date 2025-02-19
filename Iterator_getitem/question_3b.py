import recipe
from Question_3 import Question3
from typing import override

class Q3B(Question3):

    @override
    def q3_a(self):
        pass
    @override
    def q3_b(self):
        return f"{"-"*50} Question 3b: {"-"*50}\nFirst ingredient in Pancakes: {recipe.recipe1[0]}"

    @override
    def q3_c(self):
        pass
