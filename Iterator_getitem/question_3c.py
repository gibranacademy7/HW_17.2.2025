import logging
import recipe
from Question_3 import Question3
from typing import override

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Q3C(Question3):
    @override
    def q3_a(self):
        pass

    @override
    def q3_b(self):
        pass

    @override
    def q3_c(self):
        print(f"{"-"*50} Question 3c: {"-"*50}")
        try:
            index = int(input("Please enter the ingredient number you're looking for in the Pancakes recipe:"))
        except ValueError:
            logging.info("Ingredient index entered")
        if index > len(recipe.recipe1.ingredients)+1:
            logging.error(f"Ingredient index out of range - - typed {index} out of {len(recipe.recipe1.ingredients)} ingredients")
            return "Ingredient not found"
        else:
            return f"ingredient number {index} in Pancakes recipe is: {recipe.recipe1[index-1]}"