#                      +------------------+
#                      |     Homework      |
#                      +------------------+
#                      | + question_1()   |
#                      | + question_2()   |
#                      | + question_3()   |
#                      +------------------+
#                              |    |    |
#                              |    |    |
#                              |    |    |
#           +------------------+    |    +------------------+
#           |                       |                       |
#           |                       |                       |
# +------------------+   +------------------+   +------------------+
# |    Question1     |   |    Question2     |   |    Question3     |
# +------------------+   +------------------+   +------------------+
# | + question_1()   |   | + question_2()   |   | + question_1()   |
# | + question_2()   |   | + question_1()   |   | + question_2()   |
# | + question_3()   |   | + question_3()   |   | + question_3()   |
# +------------------+   +------------------+   +------------------+
#                              |
#                              |
#                   +------------------+
#                   |       Q3A       |
#                   +------------------+
#                   | + q3_a()         |
#                   | + q3_b()         |
#                   | + q3_c()         |
#                   +------------------+
#                              |
#                   +------------------+
#                   |       Q3B       |
#                   +------------------+
#                   | + q3_a()         |
#                   | + q3_b()         |
#                   | + q3_c()         |
#                   +------------------+
#                              |
#                   +------------------+
#                   |       Q3C       |
#                   +------------------+
#                   | + q3_a()         |
#                   | + q3_b()         |
#                   | + q3_c()         |
#                   +------------------+

#---------------------------------------------------------------------------------

### Explanation

# This code implements an abstract base class `Homework` that defines a structure for homework questions.
# The subclasses `Question1`, `Question2`, and `Question3` inherit from this base class and provide specific implementations for the questions.
# The `Question3` class is further divided into three subclasses: `Q3A`, `Q3B`, and `Q3C`, each responsible for a different aspect of the question.

# -------------------------------------------------------------------------------------------

# 1. **HW_1.py**:
#    - Defines the abstract class `Homework` with three abstract methods (`question_1`, `question_2`, `question_3`).
#    - Serves as a blueprint for all homework questions.

# 2. **Question_1.py**:
#    - Inherits from `Homework` and overrides `question_1` to provide a detailed explanation of how to implement an iterator in Python.
#    - The other two methods are left unimplemented.
#
# 3. **Question_2.py**:
#    - Similar to `Question_1`, it overrides `question_2` to explain the implementation of the `__getitem__` method for using `[]` with an iterator.
#
# 4. **Question_3.py**:
#    - An abstract class that inherits from `Homework` and introduces three additional abstract methods (`q3_a`, `q3_b`, `q3_c`) for further breakdown of the question.
#
# 5. **question_3a.py**:
#    - Inherits from `Question3` and provides an implementation for `q3_a`, listing ingredients for a pancake recipe.
#    - The other methods are left unimplemented.
#
# 6. **question_3b.py**:
#    - Inherits from `Question3` and implements `q3_b`, returning the first ingredient of the pancake recipe.
#    - The other methods are left unimplemented.
#
# 7. **question_3c.py**:
#    - Inherits from `Question3` and implements `q3_c`, which prompts the user for an ingredient index and returns the corresponding ingredient from the pancake recipe.
#    - Includes logging for error handling.
#
# 8. **recipe.py**:
#    - Defines a `Recipe` class that initializes a recipe with its name, ingredients, and instructions.
#    - Implements iterator methods (`__iter__`, `__next__`) and the `__getitem__` method for accessing ingredients by index.
#
# 9. **main.py**:
#    - The entry point of the application. It creates instances of the question classes and calls their methods, printing the results to the console.
