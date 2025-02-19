
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

from question_3a import Q3A
from question_3b import Q3B
from question_3c import Q3C
from Question_1 import Question1
from Question_2 import Question2


if __name__ == "__main__":
    q1 = Question1()
    q2  =Question2()
    q3a = Q3A()
    q3b = Q3B()
    q3c = Q3C()


    print(q1.question_1())
    print()
    print(q2.question_2())
    print()
    print(q3a.q3_a())
    print()
    print(q3b.q3_b())
    print()
    print(q3c.q3_c())