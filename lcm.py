import math

# Function to calculate the LCM of two numbers
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# Function to calculate the LCM of a list of numbers
def lcm_of_list(numbers):
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = lcm(lcm_result, num)
    return lcm_result

# Get user input and convert it into a list of integers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate LCM of the list
result = lcm_of_list(numbers)

# Display the result
print(f"The LCM of {numbers} is {result}")
