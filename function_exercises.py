#1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

x = input("insert a number ")
def is_two(x):    
  return x == 2 or x == "2"


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
  
  if type(x) == str:                              #first check if its a string
      result = x.lower() in ['a','e','i','o','u'] #result should be one of the elements in the list 
      return result                               # return the result 
  else:
      return False 

# Define a function named is_consonant. It should return True if the passed 
# string is a consonant, False otherwise. Use your is_vowel function to accomplish this.


def is_vowel(a):
  
  if type(a) == str:
      result = a.lower() in ['a','e','i','o','u']
      return result
  else:
      return False
# Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.
def is_consonant (a):
  if type(a) == str:
    consonant_letters = a.isalpha()
    return consonant_letters and not is_vowel(a) 
  else:
    return False

# Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.
def cap_firstletter (a):       
  if type(a) == str:
      cap_firstletter = a.capitalize()
  return cap_firstletter
# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(bill, tip):
    if type(bill) == float or int  and type (tip) == float or int:
        calculate_tip = bill * tip
        return calculate_tip

# Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, percent):
    if type(price) == float or int  and type (percent) == float or int:

        apply_discount = price - (price*percent)     #discount is 10 %
    return apply_discount


# Define a function named handle_commas. It should accept a string that is a number that contains commas 
# in it as input, and return a number as output.
def handle_comas (a):
  if type (a) == str:
    handle_comas = (a.replace(',',""))  
    handle_comas = float(handle_comas)
    return handle_comas

# Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

def letter_grade (a):
    
    if type(a) == int or type(a) == float:
        letter_grade = int(a)
        if letter_grade >= 90:
            return "A"
        elif letter_grade >= 80:
            return "B"
        elif letter_grade >= 70:
            return "C"
        elif letter_grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Input must be a number"
    return letter_grade
    
# print(letter_grade(59))

#Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels (a):
  vowels = ["a","e","i","o","u"]
  s = ''
  if type(a) == str:
    for i in a.lower():
      if i not in vowels:
        s = s + i
    return s

#Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
def normalize_name(string):
    new_output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            new_output += character
    new_output = new_output.strip()
    new_output = new_output.replace(' ', '_')
    return new_output


