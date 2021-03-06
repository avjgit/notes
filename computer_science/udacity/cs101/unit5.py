﻿# 01/ 34 Introduction
# 02/ 34 Making Things Fast
# 03/ 34 Measuring Speed - Question
# 04/ 34 Stopwatch
# eval = as "dynamic sql" - evaluates any string as Python code
import time
print(time.clock())
05/ 34 Spin Loop
06/ 34 Predicting Run Time - Question
import time
def time_execution(code):
    start = time.clock()
    result = eval(code)
    stop = time.clock()
    run_time = stop - start
    return result, run_time
def spin_loop(n):
    i = 0
    while i < n:
        i = i+1
print(time_execution('spin_loop(1)'))
print(time_execution('spin_loop(10)'))
print(time_execution('spin_loop(100)'))
print(time_execution('spin_loop(1000)'))
print(time_execution('spin_loop(10000)'))
print(time_execution('spin_loop(100000)'))
print(time_execution('spin_loop(1000000)'))



# 07/ 34 Make Big Index
# 08/ 34 Index Size Vs. Time - Question
# 09/ 34 Lookup Time - Question
# 10/ 34 Worst Case - Question
# 11/ 34 Fast Enough - Question
# 12/ 34 Making Lookup Faster
# 13/ 34 Hash Table - Question
# 14/ 34 Hash Function
# 15/ 34 Modulus Operator
# 16/ 34 Modulus Quiz - Question
# 17/ 34 Equivalent Expressions - Question
# 18/ 34 Bad Hash - Question
# 19/ 34 Better Hash Functions - Question
#Define a function, hash_string,
#that takes as inputs a keyword
#(string) and a number of buckets,
#and outputs a number representing
#the bucket for that keyword.

#print hash_string('a',12) => 1
#print hash_string('b',12) => 2
#print hash_string('a',13) => 6

#print hash_string('au',12) => 10
#print hash_string('udacity',12) => 11

def hash_string(keyword,buckets):
    wordsum = 0
    for c in keyword:
        wordsum = wordsum + ord(c)
    return wordsum%buckets

print(hash_string('a',12)) 
print(hash_string('b',12))
print(hash_string('a',13))
print(hash_string('au',12))
print(hash_string('udacity',12))

# 20/ 34 Testing Hash Functions
# 21/ 34 Keywords And Buckets - Question
# 22/ 34 Implementing Hash Tables - Question
# 23/ 34 Empty Hash Table - Question
#Creating an Empty Hash Table
#Define a procedure, make_hashtable,
#that takes as input a number, nbuckets,
#and outputs an empty hash table with
#nbuckets empty buckets.

def make_hashtable(nbuckets):
    hash = []
    for bucket in range(0,nbuckets):
        hash.append([])


# 24/ 34 The Hard Way - Question
# 25/ 34 Finding Buckets - Question
#Define a procedure, hashtable_get_bucket,
#that takes two inputs - a hashtable, and
#a keyword, and outputs the bucket where the
#keyword could occur.

#hash_string(keyword,nbuckets) => index of bucket

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

# 26/ 34 Adding Keywords - Question
def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable,keyword).append([key, [value]])

# 27/ 34 Lookup - Question
#Define a procedure,

#hashtable_lookup(htable,key)

#that takes two inputs, a hashtable
#and a key (string),
#and outputs the value associated
#with that key.

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for i in bucket:
        if i[0] == key:
            return i[1]
        else:
            return 'None'
# 28/ 34 Update - Question
def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key, value])

# 29/ 34 Dictionaries
# Isn't the list just a special case of dictionary (where keys are ints)?
# 30/ 34 Using Dictionaries
elements = { 'hydrogen': 1, 'helium': 2, 'carbon': 6}
# 31/ 34 Population - Question
population = {'Mumbai': 12.5}
# 32/ 34 A Noble Gase
#in dictionaries, values can be other dictionaries
elements = {}
elements['H'] = {'name': 'Hydrogen', 'number': 1, 
'weight': 1.00794}


print elements['H']['weight']
# 33/ 34 Modifying The Search Engine - Question
# 34/ 34 Changing Lookup - Question
#Change the lookup procedure
#to now work with dictionaries.

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
