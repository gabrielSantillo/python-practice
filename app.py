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

# name = input("Enter a word: ")

# size = len(name)

# for i in range(0, size):
#     if int(i) % 2 == 0:
#         print(name[i])

#####################################################################################################################################

# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# For example:

# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.

# def remove_chars(word, num):
#     x = word[num:]
#     return x

# remove_chars("gabriel", 3)


#####################################################################################################################################

# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# numbers = [1,2,3,5]

# def match_first_and_last(numbers):
#         first_num = numbers[0]
#         last_num = numbers[-1]

#         if first_num == last_num:
#             return True
#         else:
#             return False

# print(match_first_and_last(numbers))

#####################################################################################################################################

# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# numbers = [5, 10, 15, 18, 25, 49]

# for i in range(len(numbers)):
#     if numbers[i] % 5 == 0:
#         print(numbers[i])