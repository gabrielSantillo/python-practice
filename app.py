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

#####################################################################################################################################

# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

# str_x = "Emma is good developer. Emma is writer"

# print(str_x.count("Emma"))

#####################################################################################################################################

# Exercise 8: Print the following pattern

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# for num in range(10):
#     for i in range(num):
#         print (num, end=" ") #print number
#     # new line after each row to display pattern correctly
#     print("\n")

#####################################################################################################################################

# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

# number = input("Type in a number: ")

# reverse_list = list(reversed(number))
# reverse = ''
# reverse = reverse.join(reverse_list)

# if number == reverse:
#     print(True)
# else:
#     print(False)

#####################################################################################################################################

# Exercise 10: Create a new list from a two list using the following condition

# Create a new list from a two list using the following condition
# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# list3 = []

# for i in range(len(list1)):
#     if list1[i] % 2 != 0:
#         list3.append(list1[i])

# for i in range(len(list2)):
#     if list2[i] % 2 == 0:
#         list3.append(list2[i])

# print(list3)

#####################################################################################################################################

# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")

#####################################################################################################################################

# Exercise 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20

# Expected Output:
# For example, suppose the taxable income is 45000 the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

def tax(income):
    if income <= 10000:
        tax = 0
        return tax
    elif income <= 20000:
        next = 10000
        tax = next * .1
        return tax
    else:
        income -= 10000
        next = 10000
        tax = next * .1
        remaining = income - next
        tax += remaining * .2
        return tax

tax(45000)