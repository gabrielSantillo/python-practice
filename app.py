# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

# number1 = 40
# number2 = 30

# def make_the_math(num1, num2):
#     if num1 * num2 >= 1000:
#         result = num1 + num2
#         return result
#     else:
#         result = num1 * num2
#         return result

# print(make_the_math(number1, number2))

#####################################################################################################################################

# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

# previous_num = 0

# for number in range(10):
#     print("current " + str(number) + " previous " + str(previous_num) + " - sum: " + str(number + previous_num))
#     previous_num = number

#####################################################################################################################################

# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

name = input("Enter a word: ")

size = len(name)

for i in range(0, size):
    if int(i) % 2 == 0:
        print(name[i])

