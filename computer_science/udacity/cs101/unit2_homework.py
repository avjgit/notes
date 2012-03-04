# 1/7
# Define a procedure, udacify, that takes as 
# input a string, and returns a string that 
# is an uppercase 'U' followed by the input string.
# for example, when we enter

# print udacify('dacians')

# the output should be the string 'Udacians'

# Make sure your procedure has a return statement.

def udacify(input):
    return 'U' + input

# Define a procedure, median, that takes three
# numbers as its inputs, and outputs the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
        
def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median():