# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

number1 = 40
number2 = 30

def make_the_math(num1, num2):
    if num1 * num2 >= 1000:
        result = num1 + num2
        return result
    else:
        result = num1 * num2
        return result

print(make_the_math(number1, number2))

