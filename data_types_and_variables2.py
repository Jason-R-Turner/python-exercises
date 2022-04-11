type(99.9)
#float

type("False")
#str

type(False)
#bool

type('0')
#str

type(0)
#int

type(True)
#bool

type('True')
#str

type([{}])
#list

type({'a': []})
#dict

# What data type would best represent:

# A term or phrase typed into a search box?
# If a user is logged in?
# A discount amount to apply to a user's shopping cart?
# Whether or not a coupon code is valid?
# An email address typed into a registration form?
# The price of a product?
# A Matrix?
# The email addresses collected from a registration form?
# Information about applicants to Codeup's data science program?
# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

#Error because str and int can't be added like that
'1' + 2
#TypeError: can only concatenate str (not "int") to str

#A remainder of 2
6 % 4
#2

#type is int
type(6 % 4)
#class 'int'

#type is type
type(type(6 % 4))
#class 'type'

#Error with adding str to int types
'3 + 4 is ' + 3 + 4
TypeError: can only concatenate str (not "int") to str

#False, not mathematically true
0 < 0
#False

#False, str is not equivalent to boolean
'False' == False
#False

#False, boolean not equivalent to str
True == 'True'
#False

#True, 5 is 10 greater than -5
5 >= -5
#True

#True, or statement only needs one to be true
True or "42"
#True

#remainder of 1
6 % 5
#1

#False, 5 is not less than 4 and 1 is equivalent to itself but both need to be true
5 < 4 and 1 == 1
#False

#False, first statement is true but second is not making both together false
'codeup' == 'codeup' and 'codeup' == 'Codeup'
#False

#True, 4 is greater than 0 and int 1 is not equivalent to str 1
4 >= 0 and 1 !== '1'
#SyntaxError: invalid syntax

#True, remainder of 0 is equivalent to itself
6 % 3 == 0
#True

#True, 1 is not equal to 0
5 % 2 != 0
#True

#Error, list and int values can't be added together in this way
[1] + 2
#TypeError: can only concatenate list (not "int") to list

#[3]?
[1] + [2]
#[1, 2]

#Error, list and int values can't be multiplied like this
[1] * 2
#[1, 1]

#[1, 1]
[1] * [2]
#TypeError: can't multiply sequence by non-int of type 'list'

#True, null plus null equals null which is equivalent to null
[] + [] == []
#True

#{}?
{} + {}
#TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

little_mermaid = 3
brother_bear = 5
hercules = 1

movies = [little_mermaid, brother_bear, hercules]
print(movies)
price = 3
rentals = 0

for days in movies:
   rentals += days * price
print(rentals)


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350
hourly_rate = [google, amazon, facebook]
hours_worked = [6, 4, 10]
weeks_pay = []

weeks_pay = hourly_rate[0] * hours_worked[0] + hourly_rate[1] * hours_worked[1] + hours_worked[2] * hourly_rate[2]
print(weeks_pay)

google = 400
amazon = 380
facebook = 350
hourly_rate = [google, amazon, facebook]
hours_worked = [6, 4, 10]
weeks_pay = []

for rate in range(len(hourly_rate)):
    weeks_pay.append(hourly_rate[rate] * hours_worked[rate])
print(sum(weeks_pay))


# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

student_enrolled = True
full_class = False
class_schedule = True
current_schedule = False
student_enrolled != full_class and (class_schedule != current_schedule)


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

three_plus_items = True
not_expired = True

product_offer = three_plus_items and not_expired
print(product_offer)

premium_members = not_expired
print(premium_members)

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_at_least_5_char = True
username_more_than_20_char = False
password_is_username = False

proper_username_and_password = password_at_least_5_char and not username_more_than_20_char and not password_is_username
print(proper_username_and_password)
