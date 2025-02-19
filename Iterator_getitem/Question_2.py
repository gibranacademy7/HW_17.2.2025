from HW_1 import Homework
from typing import override

class Question2(Homework):


    @override
    def question_1(self):
        pass

    @override
    def question_2(self):
        return f"{"-"*50} Question 2: {"-"*50}\nIn order to use '[]' in the iterator, we have to implement the __getitem__ dunder function"

    @override
    def question_3(self):
        pass
