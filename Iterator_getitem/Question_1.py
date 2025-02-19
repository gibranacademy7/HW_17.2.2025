from HW_1 import Homework
from typing import override

class Question1(Homework):


    @override
    def question_1(self):
        return (f"{"-"*50} Question 1: {"-"*50}\nIn order to implement an Iterator, we need to implement the following functions:\
        \n{" "*2}1. __iter__: Returns the iterator itself.\
        \n{" "*2}2. __next__: Sets the conditions for the iteration process: What objects do we want to iterate on,\
        \n{" "*15}When to stop the iteration process and what values to return.\n\nTo finish the iterator, we need to raise a StopIteration Error")

    @override
    def question_2(self):
        pass

    @override
    def question_3(self):
        pass
