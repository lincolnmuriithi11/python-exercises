#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
#little mermaid = 3days
#brother bear = 5 days 
#hercules = 1 day
#price per movie per day = 3
little_mermaid_days = 3 
brother_bear_days = 5
hercules_days = 1
price_per_day = 3
total_days = little_mermaid_days + brother_bear_days + hercules_days
total_amount = total_days*  price_per_day
total_amount
print(f"Total amount spent on videos is ${total_amount}")

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon
hours_amzn = 4
google_hr_pay = 400
amazon_hr_pay = 380
facebook_hr_pay = 350
hours_google = 6
hours_fb = 10
hours_amzn = 4
total_per_week = google_hr_pay*hours_google + amazon_hr_pay* hours_amzn + facebook_hr_pay * hours_fb 
print(f"Amount received for the week is ${total_per_week}")
#Amount received for the week is $7420

#A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_not_full = True 
no_conflict = True 
student_can_be_enrolled = class_not_full and no_conflict
print(f"student can be enroled? {student_can_be_enrolled}")
#student can be enroled? True

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
premium_member = True
more_than_2_items = False
offer_not_expired = True
discount_available = offer_not_expired and (premium_member or more_than_2_items)
print (f"Is discount valid {discount_available}")



#Create a variable that holds a boolean value 
#for each of the following conditions:

#the password must be at least 5 characters
#the username must be no more than 20 characters
#the password must not be the same as the username
#bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_length = len(password) >= 5
username_length = len(username) <=20
password_not_same_as_username = username != password #you can have booleans inside variables 
username_spaces = username_length =  username != username.strip() #to remove spaces in the username 
password_spaces = password_length = password != password.strip() #to get rid of spaces
