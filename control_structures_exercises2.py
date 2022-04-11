# Exercies redo since working in jupyter notebook saved it with all the metadata for web page

#1. Conditional Basics
#1a. prompt the user for a day of the week, print out whether the day is Monday or not.

if input("Enter a day of the week. ") == 'Monday':
    print('It\'s Monday')
else:
    print('It\'s not Monday')

#1b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend.

day= str(input("Enter a day Sunday - Saturday: "))

if (day=='Sunday'):
    print(day,"is a weekend")
elif (day=='Monday'):
    print(day,"is a weekday")
elif (day=='Tuesday'):
    print(day,"is a weekday")
elif (day=='Wednesday'):
    print(day,"is a weekday")
elif (day=='Thursday'):
    print(day,"is a weekday")
elif (day=='Friday'):
    print(day,"is a weekday")
elif (day=='Saturday'):
    print(day,"is a weekend")
else:
    print("Wrong input. Please enter one of the seven days of the week capitalized.")

#1c. create variables and make up values for
#• the number of hours worked in one week
#• the hourly rate
#• how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = [30, 50]
hourly_wages = 20
weekly_wages = [h * hourly_wages for h in hours_worked]


for h in hours_worked:
    if h <= 40:
        h = [h * hourly_wages] 
    else:
        h = [h * hourly_wages * 1.5]
    print('Paycheck is $' + str(h))

#2. Loop Basics
#While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
n = 0

while n <= 100:
    print(n)
    n += 2


# Alter your loop to count backwards by 5's from 100 to -10.
n = 100

while n >= -10:
    print(n)
    n += -5


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
n = 2

while n < 1000000:
    print(n)
    n = n * n


# Write a loop that uses print to create the output shown below.
n = 100

while n >= 5:
    print(n)
    n += -5


# For Loops
#b.  Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
#b.i.
number = int(input("Enter a number. "))

for n in range(1, 11):
    print(f'{number} x {n} = {n * number}')


#b.ii.
# for n in range(1, 10):
#     print(f'{n * (10**(n-1))}')

for n in list(range(1, 10)):
    print(str(n)*n)


#c. break and continue
#c.i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine 
# this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
odd = input("Please enter an odd number from 1 to 50, ")

for n in odd:
    if odd.isdigit() == False:
        odd = input('Please try again using numbers only, ')
    elif odd.isdigit() == True:
        break
        
for n in range(1, 51):
    odd = int(odd)
    if n == odd:
        print('Yikes! Skipping number ' + str(odd))
    elif n % 2 == 0:
        continue
    else:
        print(f'Here is an odd number: {n}')


#d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

pos = input("Enter an positive number: ")
pos.isdigit()
pos = int(pos)

for x in range(pos):
    x = x+1
    if x > 0:
        print(str(x)+' is positive')


#e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
pos = input("Enter an positive number: ")
pos.isdigit()
pos = int(pos)

for x in range(pos):
    x = x+1
    if x > 0:
        x = pos - (x-1)
        print(str(x)+' is positive')


#3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.

for n in range(1, 101):
    print(n)
    n += 1


# For multiples of three print "Fizz" instead of the number
for n in range(1, 101):
    if n % 3 == 0:
        print("Buzz")


# For the multiples of five print "Buzz".
for n in range(1, 101):
    if n % 5 == 0:
        print("Buzz")

# For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1, 101):
    if n % (3 * 5) == 0:
        print("FizzBuzz")

#4. Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
integer = int(input("Enter an integer. "))

print("number |"+" squared |"+" cubed")
for n in range(1, (integer+1)):
    print(str(n) + "      |"+ str(n**n)+ "       |"+ str(n**n**n))

cont = input("Do you want to continue? Yes or No, ")

if cont == 'Yes':
    integer = int(input("Enter an integer, "))
    print("number |"+" squared |"+" cubed")
    for n in range(1, (integer+1)):
        print(str(n) + "      |"+ str(n**n)+ "       |"+ str(n**n**n))
else:
    print('Thanks for playing')



#5. Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
grade = int(input("Enter grade from 0-100, "))
A = list(range(88, 101))
B = list(range(80, 88))
C = list(range(67, 80))
D = list(range(60, 67))
F = list(range(60))

grade_ranges = [A, B, C, D, F]

if grade in grade_ranges[0]:
    print('Grade is A')
elif grade in grade_ranges[1]:
    print('Grade is B')
elif grade in grade_ranges[2]:
    print('Grade is C')
elif grade in grade_ranges[3]:
    print('Grade is D')
else:
    print('Grade is F')
    
    
cont = input("Would you like to continue? Yes or No, ")
if cont == 'Yes':
    grade = int(input("Enter grade from 0-100, "))
    if grade in grade_ranges[0]:
        print('Grade is A')
    elif grade in grade_ranges[1]:
        print('Grade is B')
    elif grade in grade_ranges[2]:
        print('Grade is C')
    elif grade in grade_ranges[3]:
        print('Grade is D')
    else:
        print('Grade is F')

else:
    print('Thanks for playing')

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

#6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

beginning_book = ["Start", 'Sally', 'mystery']
middle_book = ["Continue", 'Billy', 'adventure']
ending_book = ["Finish", 'Tommy', 'horror']

beginning_book = {'title': "Start", 'author': 'Sally', 'genre': 'mystery'}
middle_book = {'title': "Continue", 'author': 'Billy', 'genre': 'adventure'}
ending_book = {'title': "Finish", 'author': 'Tommy', 'genre': 'horror'}

books_read = [beginning_book, middle_book, ending_book]

for book in books_read:
    print("Title: "+ book['title'])
    print("Author: "+ book['author'])
    print("Genre: "+book['genre'])


#a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

user_genre = input("Enter a genre, ")

for book in books_read:
     if book['genre'] == user_genre:
            print("Title: "+ book['title'])
            print("Author: "+ book['author'])
            print("Genre: "+book['genre'])