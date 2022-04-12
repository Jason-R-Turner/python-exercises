# # Functions
#1 Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    return n == 2

print(is_two(2))
is_two(3)
# also include string version of '2'


#2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(char):
    return char.lower() in 'aeiou'    

print(is_vowel('e'))
is_vowel('z')
# use list method, like ['a', 'e', 'i', 'o', 'u'] to avoid returning true for character strings within "aeiou",

#3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(char):
    return char.lower() not in 'aeiou'    

print(is_consonant('e'))
is_consonant('z')
# input.isalpha() tells you if it's a letter and not some other character

#4 Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalizer(word):
    first_char = word[0]
    if is_consonant(first_char):
        return first_char.upper()
    else:
        return 'Not a consonant.'

print(capitalizer('elise'))
capitalizer('boba')


#5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percent, total):
    tip = (percent * total)
    return tip

calculate_tip(.5, 12)
print(str(calculate_tip(.1, 100)) + '% tip')


#6 Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, disc):
    disc_price = price - (price * (disc))
    return '$' + str(round(disc_price, 2))

print(apply_discount(100, .25))
apply_discount(50, .275)


#7 Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.


#8 Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(num_grade):
    letter_grade = num_grade
    if letter_grade >= 90:
        print("You got an A")
    elif letter_grade >= 80:
        print("You got a B")
    elif letter_grade >= 70:
        print("You got a C")
    elif letter_grade >= 70:
        print("You got a D")
    else:
        print("You got a F")


#9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    newstr = string
    vowels = ('a', 'e', 'i', 'o', 'u')
    for letter in string.lower():
        if letter in vowels:
            newstr = newstr.replace(letter,"")
    return newstr

remove_vowels('howdy do')

#9 Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(name):
    return

#11 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# Additional Exercise

# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.
# Bonus

# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27