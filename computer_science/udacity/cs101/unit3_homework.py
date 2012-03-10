#1
p = [0, 1, 1] #?
p[0] = p[0] + p[1]
p[1] = p[0] + p[2]
p[2] = p[0] + p[1]
print p # [1,2,3]
#2 quiz
#3
#Define a procedure, product_list,
#takes as input a list of numbers,
#and returns a number that is
#the result of multiplying all
#those numbers together.

#product_list([9]) => 9
#product_list([1,2,3,4]) => 24
def product_list(numbers):
    mult = 1
    for n in numbers:
        mult = mult * n
    return mult

#4 
#Define a procedure, greatest,
#that takes as input a list
#of positive numbers, and
#returns the greatest number
#in that list. If the input
#list is empty, the output
#should be 0.

#greatest([4,23,1]) => 23
#greatest([]) => 0

def greatest(numbers):
    greatest = 0
    for n in numbers:
        if n > greatest:
            greatest = n
    return greatest