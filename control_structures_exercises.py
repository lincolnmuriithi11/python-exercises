# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

day_of_the_week = input("What day is today? ") #add a while and list of days in order to limit inputs that people put
days_of_the_week = day_of_the_week.lower()
if days_of_the_week == "monday":
  print("Today is Monday")
else:
  print("Today is not Monday")


day_of_the_week = input("What day is today? ")
days_of_the_week = day_of_the_week.lower()
if days_of_the_week.startswith('s'):
  print (" it's the weekend")
else:
  print("it's a weekday")


weekly_working_hours = float(40)
hourly_rate = float(50) 
weekly_rate = hourly_rate * weekly_working_hours
overtime = float(input("How many overtime hours did you work?"))
if overtime > 0:
  weekly_rate = weekly_rate + (hourly_rate * 1.5 * overtime) 
  print(f"your full time pay is ${weekly_rate}") 
else:
  print(f"your weekly pay is ${weekly_rate}")


# Loop Basics

# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:
i = 5
while i <= 15:
  print(i)
  i += 1

# whileloop starting at 2 ending at 100
i = 0
while 1 <= 100:
  print(i)
  if i == 100:
    break
  i += 2


# Alter your loop to count backwards by 5's from 100 to -10.
  i = 0
while i < 100:
  print(i)
  if i == 100:
    break
  i += 2
while i >= -10:
  print(i)
  if i == -10:
    break
  i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1_000_000: # no need for a break because the answers are limited
    print(i)
    i **= 2
#  2
#  4
#  16
#  256
#  65536


# Write a loop that uses print to create the output shown below.
  i = 100
while i >= 5:
  print(i)
  if i ==5:
    break
  i -= 5


# b For Loops

# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:
num = int(input("enter a number? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x',i,'=', num*i)

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70



# ii. Create a for loop that uses print to create the output shown below.
for i in range(1,10):
  print(int(str(i) * i))
# also a possible answer
# num = int(9)
# for i in range (1, num+1): 
#     for j in range(1, i+1):
#           print(i, end="")
#     print()

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999





# c. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# Your output should look like this:
num = input("Please pick a number ")
while True:
  if (num.isdigit() == False or int(num) > 50 or int (num)<1 or int(num)% 2 ==0):
    print ('Invalid input')
    num = input("Please enter another number ")
  else: 
    break
num_int = int(num)

for x in range(1, 50, 2):
    if x == num_int:
        print('Yikes! skipping number: ', x)
    else:
        print('Here is an odd number: ', x)

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17




# Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1,101):
  if num % 3 == 0 and num % 5 ==0: #the key is the order of how you arrange the order of operation
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)

# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

import math
num = input("What number would you like to go upto? ")
num_int = int(num)

print('number | squared | cubed') 
print('------ | ------- | -----')   
for x in range(1, num_int + 1):
    num_squared = x ** 2
    num_cubed = x ** 3
    print(f'{x: <6} | {num_squared: ^7} | {num_cubed: 5}')

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125




# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

while True:
  class_grade = int(input("What is your numerical grade? "))

  if class_grade in range(0,60):
    class_grade = "F"
  elif class_grade in range (60,67):
    class_grade = "D"
  elif class_grade in range (67,80):
    class_grade = "C"
  elif class_grade in range (80,88):
    class_grade = "B"
  else:
    class_grade = "A"
  print(class_grade)

  choice = input("If you want to continue, please enter yes or y: ")
  if choice.lower() in ['yes', 'y']:
    
    continue 
  else:
    break

# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# bookshelf = [
#     {'title': 'Annihilation',
#     'author': 'Jeff Vandermeer',
#     'genre': 'Science Fiction'},
#     {'title': 'Octopus Pie',
#     'author': 'Maredeth Gran',
#     'genre': 'Comic'},
#     {'title': 'Cabin At the End of the World',
#     'author': 'Paul Tremblay',
#     'genre': 'Horror'},
#     {'title': 'Severance',
#     'author': 'Ling Ma',
#     'genre': 'Science Fiction'},
# ]
# # if ',' is in book['genre']:
# #     book['genre'].split(',')
# # if type(book['genre']) 

# for key in book:
#     print(key, book[key])
# for book in bookshelf:
#     print('we are living in a single dictionary here')
#     [print(key, ': ', book[key]) for key in book]
#     print('------')

#     picked_genre = input('Please pick a genre and I will return the titles of that genre on shelf. \n')
# Please pick a genre and I will return the titles of that genre on shelf. 
# comedy
# # start with an empty list,
# # add the book dictionary to the list if it is of the correct genre
# # include a check for a still empty list to indicate via message that there are no 
# # books of that genre
# matches = []
# for book in bookshelf:
#     if book['genre'].lower() == picked_genre.lower():
#         matches.append(book['title'])
# if matches == []:
#     print('no books in that genre available. please check back later')
# else:
#     print(f'I have the following titles in the genre {picked_genre}')
#     [print(match) for match in matches]
 
  



