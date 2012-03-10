# 01 /44 Introduction
# 02 /44 Stooges - Question
stooges = ['Moe', 'Larry', 'Curly']
# 03 /44 Days In A Month - Question
#Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

#define a procedure, how_many_days,
#that takes as input a number
#representing a month, and outputs
#the number of days in that month.

#how_many_days(1) => 31
#how_many_days(9) => 30
def how_many_days(month):
    return days_in_month[month-1]
# 04 /44 Nested Lists
# 05 /44 Countries - Question
#Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

#Write code to print out the capital of India
#by accessing the array.
print countries[1][1]




# 06 /44 Relative Size - Question
#What multiple of Romania's population is the population
#of China? Please print your result.
print countries[0][2]/ countries[2][2]

# 07 /44 Mutation
# Lists can be changed; with strings, new instances are created

# 08 /44 A List Of Strings
# 09 /44 Different Stooges - Question
#We defined:

stooges = ['Moe','Larry','Curly']

#but in some Stooges films, Curly was
#replaced by Shemp.

#Write one line of code that changes
#the value of stooges to be:

#['Moe','Larry','Shemp']

#but does not create a new List
#object.

stooges[2] = 'Shemp'

# 10 /44 Yello Mutation
# p = ['a']
# q = p
# now, q referes to same object
# p[0] = 'b'
# print q[0] will print 'b' as well

# 11 /44 Aliasing
# 12 /44 Secret Agent Man - Question
# 13 /44 Replace Spy - Question
#Define a procedure, replace_spy,
#that takes as its input a list of
#three numbers, and modifies the
#value of the third element in the
#input list to be one more than its
#previous value.

spy = [0,0,7]

#replace_spy(spy)
#print spy => [0,0,8]
def replace_spy(spy):
    spy[2] = spy[2]+1
print spy
# passed by reference!

# 14 /44 List Operations
<list>.append(<element>) #mutates list
# 15 /44 List Addition And Length
<list> + <list> # produces new list
len(<list>)
# 16 /44 Len Quiz - Question
# 17 /44 Append Quiz - Question
# 18 /44 How Computers Store Data
# 19 /44 Dram
latency - time to receive a value
# 20 /44 Memory Hierarchy - Question
# 21 /44 Hard Drives - Question
# 22 /44 Loops On Lists - Question
# 23 /44 For Loops
for name in list:
    block
# 24 /44 Sum List - Question
#Define a procedure, sum_list,
#that takes as its input a
#List of numbers, and produces
#as its output the sum of all
#the elements in the input list.

#For example,
#sum_list([1,7,4]) => 12

def sum_list(list):
    sum = 0
    for element in list:
        sum += element
    return sum

# 25 /44 Measure Udacity - Question
#Define a procedure, measure_udacity,
#that takes its input a list of Strings,
#and outputs a number that is a count
#of the number of elements in the input
#list that start with the letter 'U'
#(uppercase).


def measure_udacity(list):
    udacity = 0
    for name in list:
        if name[0] == 'U':
            udacity += 1
    return udacity

measure_udacity(['Dave','Sebastian','Katy'])

measure_udacity(['Umika','Umberto'])


# 26 /44 Find Element - Question
#Define a procedure, find_element,
#that takes as its inputs a List
#and a value of any type, and
#outputs the index of the first
#element in the input list that
#matches the value.

#If there is no matching element,
#output -1.

#find_element([1,2,3],3) => 2

#find_element(['alpha','beta'],'gamma') => -1
def find_element(list, target):
    i = 0
    for word in list:
        if word == target:
            return i
        i += 1
    return -1

def find_element(_list, target):
    i = 0
    while i < len(_list):
        if _list[i] == list(target):
            return i
        i += 1
    return -1

# 27 /44 Index - Question
# list.index(value)
# doesn't return -1 - returns error


# <value> in <list> #true/ false
#Define a procedure, find_element,
#using index that takes as its
#inputs a List and a value of any
#type, and outputs the index of
#the first element in the input
#list that matches the value.

#If there is no matching element,
#output -1.

#find_element([1,2,3],3) => 2

#find_element(['alpha','beta'],'gamma') => -1



# 28 /44 Guest Speaker
# 29 /44 Union - Question
# 30 /44 Pop
# 31 /44 Pop Quiz - Question
# 32 /44 Collecting Links
# 33 /44 Get All Links
# 34 /44 Links
# 35 /44 Starting Get All Links - Question
# 36 /44 Updating Links - Question
# 37 /44 Finishing Get All Links - Question
# 38 /44 Finishing The Web Crawler
# 39 /44 Crawling Process - Question
# 40 /44 Crawl Web - Question
# 41 /44 Crawl Web Loop - Question
# 42 /44 Crawl If - Question
# 43 /44 Finishing Crawl Web - Question
# 44 /44 Conclusion
