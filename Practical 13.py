import math  # Mathematical functions and constants
import random  # Generating random numbers
import statistics  # Statistical functions
import itertools  # Functional programming tools

# Using math module
def math_operations():
    print("Math Module Operations:")
    number = float(input("Enter a number to calculate its square root, power, log, and factorial: "))
    
    sqrt_value = math.sqrt(number)
    print(f"Square root of {number}: {sqrt_value}")

    power_exponent = int(input("Enter the exponent for power calculation: "))
    power_value = math.pow(number, power_exponent)
    print(f"{number} raised to the power {power_exponent}: {power_value}")

    log_value = math.log(number)
    print(f"Natural log of {number}: {log_value}")

    factorial_number = int(input("Enter an integer to calculate its factorial: "))
    factorial_value = math.factorial(factorial_number)
    print(f"Factorial of {factorial_number}: {factorial_value}")

    print()

# Using random module
def random_operations():
    print("Random Module Operations:")
    lower_bound = int(input("Enter the lower bound for a random integer: "))
    upper_bound = int(input("Enter the upper bound for a random integer: "))
    random_int = random.randint(lower_bound, upper_bound)
    print(f"Random integer between {lower_bound} and {upper_bound}: {random_int}")

    random_float_lower = float(input("Enter the lower bound for a random float: "))
    random_float_upper = float(input("Enter the upper bound for a random float: "))
    random_float = random.uniform(random_float_lower, random_float_upper)
    print(f"Random float between {random_float_lower} and {random_float_upper}: {random_float}")

    choices = input("Enter a list of choices separated by commas (e.g., apple,banana,cherry): ").split(',')
    random_choice = random.choice(choices)
    print(f"Random choice from list: {random_choice}")

    print()

# Using statistics module
def statistics_operations():
    print("Statistics Module Operations:")
    data = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
    mean_value = statistics.mean(data)
    print(f"Mean of the data: {mean_value}")

    median_value = statistics.median(data)
    print(f"Median of the data: {median_value}")

    stdev_value = statistics.stdev(data)
    print(f"Standard deviation of the data: {stdev_value}")

    print()

# Using itertools module
def itertools_operations():
    print("Itertools Module Operations:")
    data = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    
    permutations = list(itertools.permutations(data))
    print(f"Permutations of {data}: {permutations}")

    combination_length = int(input("Enter the length of combinations: "))
    combinations = list(itertools.combinations(data, combination_length))
    print(f"Combinations of {data} taken {combination_length} at a time: {combinations}")

    count_start = int(input("Enter the starting value for count: "))
    count_step = int(input("Enter the step value for count: "))
    count = itertools.count(start=count_start, step=count_step)
    count_list = [next(count) for _ in range(5)]
    print(f"First 5 values from count starting at {count_start} with step {count_step}: {count_list}")

    print()

# Main program to demonstrate all modules
if __name__ == "__main__":
    math_operations()
    random_operations()
    statistics_operations()
    itertools_operations()
