from operator import getitem

import recipe

from HW_1 import Homework
from abc import ABC, abstractmethod
from typing import override


class Question3(Homework,ABC):


    @override
    def question_1(self):
        pass

    @override
    def question_2(self):
        pass

    @override
    def question_3(self):
        pass


    @abstractmethod
    def q3_a(self):
        pass

    @abstractmethod
    def q3_b(self):
        pass

    @abstractmethod
    def q3_c(self):
        pass
