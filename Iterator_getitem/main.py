# main.py

from factorial_calc import FactorialCalculator
from adapter_float_to_int import AdapterFloat2Int
from adapter_list_to_int import AdapterList2Int

def print_factorial_number(factorial, number):
    result = factorial.calc_factorial(number)
    print(f"Factorial of {number}: {result}")

if __name__ == "__main__":
    # Create an instance of FactorialCalculator
    factorial_calculator = FactorialCalculator()

    # 1*2*3*4*5 = 120
    print_factorial_number(factorial_calculator, 5)

    # Using AdapterFloat2Int for a float number
    print_factorial_number(AdapterFloat2Int(factorial_calculator), 3.0)

    # List of numbers to calculate factorials
    numbers = [7, 9, 10]
    adapter_list = AdapterList2Int(factorial_calculator)

    # Calculate and print factorials for the list
    for number in numbers:
        print_factorial_number(adapter_list, number)
