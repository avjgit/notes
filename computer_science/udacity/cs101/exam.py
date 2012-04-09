# 01 Grammars
# How many different strings can the following grammar generate, starting from Word?
# Word → udacious
# Word → super Word
# :: I think, infinitely many

# 02 Procedures And If
#Define a procedure, unique, that takes three numbers as its inputs and returns
#the Boolean value True if all three numbers are different. Otherwise, it should
#return the Boolean value False.

def unique(a, b, c):
    return not (a == b or b == c or a == c)


#For example,

# print (unique(1, 2, 3))
#>>> True

# print (unique(1, 0, 1))
#>>> False

# print (unique(7, 7, 7))
#>>> False

# 03 Prefix Removal
#Prefix Removal


#Define a procedure, remove_prefix, that takes as input a string, and returns a
#string that is the part of the string following the first hyphen -. If the input string does
#not contain any hyphen -, remove_prefix should return the full input string.

def remove_prefix(s):
    hyphen = s.find("-")
    return s[hyphen+1:]



#For example,

# print(remove_prefix('super-udacity'))
#>>> 'udacity'

# print(remove_prefix('counter-counter-intelligence'))
#>>> 'counter-intelligence'

# print(remove_prefix('antigravity'))
#>>> 'antigravity'

# 04 Collatz Returns
#Collatz Returns!


#Define a procedure, collatz_steps, that takes as input a positive integer, n, and returns
#the number of steps it takes to reach 1 by following these steps:

#    If n is even, divide it by 2. (You can test for evenness using n % 2 == 0.)
#    If n is odd, replace it with 3n + 1.

def collatz_steps(n):
    steps = 0
    while n > 1:
        steps = steps + 1
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return steps


#For example,

# print(collatz_steps(1))
#>>> 0

# print(collatz_steps(2))
#>>> 1

# print(collatz_steps(6))
#>>> 8

# print(collatz_steps(101))
#>>> 25

# 05 Cost
# Check each of the following procedures whose running time scales linearly with the number of elements in the input p in the worst case. 
# You may assume all the elements in p are fairly small numbers. 
# You should also assume that all multiplication operations take constant time regardless of the size of the input 
# (even though this could not be true in practice).
# let's take p = 4. 
def product(p):
    result = 1
    for e in p:
        result = result * e
    return result
# It runs for 1, 2, 3, 4. Linearly.
def find_match(p, target):
    for x in p:
        for y in p:
            if x * y == target:
                return True
    return False
# It runs for 1, 1, 2, 3, 4, 2, 1, 2, 3, 4, 3, 1.... square.
def tricky_loop(p):
    while True: #while true, yes, but...
        if len(p) == 0: # .. it runs until there are no elements in a loop
            break
        else:
            if p[-1] == 0: # let's assume worst case = it's not 0; then..
                p.pop() # assume pop is a constant time operation
            else:
                p[-1] = 0 # .. in the next steps it makes it zero
    return 101 # so, total length looks like 2p.. so, linearly

# 06 List Explosion
#List Explosion


#Define a procedure, explode_list, that takes as inputs a list and a number, n.
#It should return a list which contains each of the elements of the input list,
#in the original order, but repeated n times.

def explode_list(p,n):
    result  = []
    for el in p:
        for i in range(0,n):
            result.append(el)
    return result



#For example,

# print (explode_list([1, 2, 3], 2))
#>>> [1, 1, 2, 2, 3, 3]

# print (explode_list([1, 0, 1], 0))
#>>> []

# print (explode_list(["super"], 5))
#>>> ["super", "super", "super", "super", "super"]

# 07 Reverse Index
#Define a procedure, reverse_index, that takes as input a Dictionary, and
#returns a new Dictionary where the keys are the values in the input dictionary.
#The value associated with a key in the result is a list of all the keys in the
#input dictionary that match this value (in any order).

def reverse_index(dict):
    reverse = {}
    for hash in dict:
        key = dict[hash]
        if key in reverse:
            reverse[key].append(hash)
        else:
            reverse[key] = [hash]
    return reverse

#For example,

winners_by_year = {
    1930: 'Uruguay', 1934: 'Italy', 1938: 'Italy', 1950: 'Uruguay',
    1954: 'West Germany', 1958: 'Brazil', 1962: 'Brazil', 1966: 'England',
    1970: 'Brazil', 1974: 'West Germany', 1978: 'Argentina',
    1982: 'Italy', 1986: 'Argentina', 1990: 'West Germany', 1994: 'Brazil',
    1998: 'France', 2002: 'Brazil', 2006: 'Italy', 2010: 'Spain' }

wins_by_country = reverse_index(winners_by_year)

# print (wins_by_country['Brazil'])
#>>> [1958, 2002, 1970, 1994, 1962]

# print (wins_by_country['England'])
#>>> [1966]

# 08 Same Structure
#Same Structure

#Define a procedure, same_structure, that takes two inputs. It should output
#True if the lists contain the same elements in the same structure, and False
#otherwise. Two values, p and q have the same structure if:

#    Neither p or q is a list.

#    Both p and q are lists, they have the same number of elements, and each
#    element of p has the same structure as the corresponding element of q.


#For this procedure, you can use the is_list(p) procedure from Homework 6:

def is_list(p):
    return isinstance(p, list)


def same_structure(a,b):
    if not is_list(a) and not is_list(b):
        return True
    if is_list(a) and is_list(b):
        if len(a) == len(b):
            for i in range(0,len(a)):
                if not same_structure(a[i], b[i]):
                    return False
            return True
    return False




#Here are some examples:

print(same_structure(3, 7))
#>>> True

print(same_structure([1, 0, 1], [2, 1, 2]))
#>>> True

print(same_structure([1, [0], 1], [2, 5, 3]))
#>>> False

print(same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['d', 'e']]]]))
#>>> True

print(same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['de']]]]))
#>>> False

# 09 Reachability
# 10 Spelling Correction
# 11 Multiword Queries