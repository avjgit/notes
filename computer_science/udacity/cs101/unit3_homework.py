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

#5
#Define a procedure, total_enrollment,
#that takes as an input a list of elements,
#where each element is a list containing
#three elements: a university name,
#the total number of students enrollect,
#and the annual tuition.

#The procedure should return two numbers,
#not a string,
#giving the total number of students
#enrolled at all of the universities
#in the list, and the total tuition
#(which is the sum of the number
#of students enrolled times the
#tuition for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

#>>> print total_enrollment(udacious_univs)
#(90000,0)

#>>> print total_enrollment(usa_univs)
#(77285,3058581079L)

def total_enrollment(universities):
    total_students = 0
    total_tuition  = 0
    
    for u in universities:
        students = u[1]
        tuition  = u[2]
        total_students += students
        total_tuition  += students * tuition
    
    return total_students, total_tuition
    
    