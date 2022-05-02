# # Functions
# 1 Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
# is_two defines a parameter called "n" as a string returning a string value
def is_two(n):
    # is_two returns true if "n" is equivalent to 2 otherwise it will be false
    return n == 2

print(is_two(2))
is_two(3)
# also include string version of '2'


# 2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# is_vowel defines "char" as a string value parameter
def is_vowel(char):
    # will return all letters in "char" as lowercase letters and true if it matches a vowel in "aeiou"
    return char.lower() in 'aeiou'    

print(is_vowel('e'))
is_vowel('z')
# use list method, like ['a', 'e', 'i', 'o', 'u'] to avoid returning true for character strings within "aeiou",

# 3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# is_consonant defines "char" as a string value parameter
def is_consonant(char):
    # will return all non-"aeiou" letters as lowercase letters and true if it's not a vowel
    return char.lower() not in 'aeiou'    

print(is_consonant('e'))
is_consonant('z')
# input.isalpha() tells you if it's a letter and not some other character

# 4 Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# defines function capitalizer using a character string represented by "word"
def capitalizer(word):
    # sets a placeholder item called first_char equal to the first item in "word" treated as a list
    first_char = word[0]
    # uses previously defined is_consonant function on character selected using first_char to check if it's a consonant
    if is_consonant(first_char):
        # if it is a consonant then it is returned as an uppercase letter no matter what case it currently is
        return first_char.upper()
    else:
        # if it isn't flagged as a consonant it'll return 'Not a consonant' as the function answer
        return 'Not a consonant.'

print(capitalizer('elise'))
capitalizer('boba')


# 5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
# function called calculate_tip that takes in two values for percentage a person tips and the total for the bill being tipped
def calculate_tip(percent, total):
    # tip, represents the amount when you multiple the tip percentage with the total for the bill
    tip = (percent * total)
    # returns amount to be tipped
    return tip

calculate_tip(.5, 12)
print(str(calculate_tip(.1, 100)) + '% tip')


# 6 Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
# defines a function, apply_discount, that takes in two variables representing the original price of the item and the discount percentage to be applied
def apply_discount(price, disc):
    # disc_price, subtracts the product of the original price and discount percentage from the original price leaving the total price after the discount is applied
    disc_price = price - (price * (disc))
    # returns the discounted price rounded to two decimal places converted to a str and concatenated with a dollar sign
    return '$' + str(round(disc_price, 2))

print(apply_discount(100, .25))
apply_discount(50, .275)


# 7 Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
# defines function, handle_commas, for a string represented by comma_sep
def handle_commas(comma_sep):
    # if statement that tests if parameter for comma_sep is not a string type.
    if type(comma_sep) != str:
        # returns 'Must be a string' if previous statement is true
        return 'Must be a string'
    # any commas in original comma_sep value are replaced by a none value and sets comma_sep as this transformed value
    comma_sep = comma_sep.replace(',', '')
    # checks to see if values in comma_sep are digits
    if comma_sep.isdigit():
        # if they are digits it converts them to a float value
        return float(comma_sep)
    else:
        # if there are non-digits it states that it needs to be an integer that's a string
        return 'Must be an integer as a string'
    
handle_commas('123,456,789')



# 8 Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
# defines, get_letter_grade as function with num_grade as its parameter
def get_letter_grade(num_grade):
    # sets letter_grade equal to original parameter
    letter_grade = num_grade
    # checks if paramter represented by letter_grade is 90 or greater
    if letter_grade >= 90:
        # prints "You got an A" if True
        print("You got an A")
    # checks if paramter represented by letter_grade is 80 or greater
    elif letter_grade >= 80:
        # prints "You got an B" if True
        print("You got a B")
    # checks if paramter represented by letter_grade is 70 or greater
    elif letter_grade >= 70:
        # prints "You got an C" if True
        print("You got a C")
    # checks if paramter represented by letter_grade is 60 or greater
    elif letter_grade >= 60:
        # prints "You got an D" if True
        print("You got a D")
    # checks if paramter represented by letter_grade is 0 or greater
    elif letter_grade >= 0:
        # prints "You got an F" if True
        print("You got a F")
    else:
        # prints "You got a F" if all above are False
        print("Please type in a number")


# 9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
# defines, remove_vowels, as function with string as parameter
def remove_vowels(string):
    # sets newstr equal to string parameter
    newstr = string
    # sets vowels as a set if individual characters for each vowel
    vowels = ('a', 'e', 'i', 'o', 'u')
    # starts for loop for placeholder letter within string parameter that's been converted to lowercase
    for letter in string.lower():
        # checks if each letter matches a character in vowels set
        if letter in vowels:
            # if true replaces vowel character with none value and saves that as new newstr value
            newstr = newstr.replace(letter,"")
    # returns last saved newstr value       
    return newstr

remove_vowels('howdy do')

# 10 Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
# defines, normalize_name, function for name parameter
def normalize_name(name):
    # sets valid_py_id equal to empty string
    valid_py_id = ''
    # converts characters in name to lowercase
    name = name.lower()
    # begins for loop starting at the first character in name
    for char in name:
        # checks to see if that character is valid identifier or blank space
        if char.isidentifier() or char == ' ':
            # if valid or space it is sequentially added to the valid_py_id string
            valid_py_id += char
    # removes any whitespace from ends of string then sets valid_py_id equal to new string
    valid_py_id = valid_py_id.strip()
    # replaces any left over blank spaces with underscores then sets valid_py_id equal to new string
    valid_py_id = valid_py_id.replace(' ', '_')
    # returns latest saved version of valid_py_id
    return valid_py_id

normalize_name("  12Gar uda 3 ")


# 11 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# defines, cumulative_sum as functions taking in ints parameter
def cumulative_sum(ints):
    # sets cum_ints equal to empty list
    cum_ints = []
    # starts for loop n number of times for the each position of the range created that's equal to the length of the ints parameter
    for n in range(len(ints)):
        # adds up the integers starting from one then adds it to the running tally for each subsequent position by the previous amount plus n
        num_sum = sum(ints[:1+n])
        # adds each number to the cum_ints sequentially for every loop
        cum_ints.append(num_sum)
    # returns final list of integers in cum_ints list
    return cum_ints

print(cumulative_sum([1, 1, 1]))
cumulative_sum([1, 2, 3, 4])

# Additional Exercise

# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.
# Bonus

# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27