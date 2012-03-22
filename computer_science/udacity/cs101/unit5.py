# 01/ 34 Introduction
# 02/ 34 Making Things Fast
# 03/ 34 Measuring Speed - Question
# 04/ 34 Stopwatch
# eval = as "dynamic sql" - evaluates any string as Python code
# import time
# print(time.clock())
# 05/ 34 Spin Loop
# 06/ 34 Predicting Run Time - Question
# import time
# def time_execution(code):
#     start = time.clock()
#     result = eval(code)
#     stop = time.clock()
#     run_time = stop - start
#     return result, run_time
# def spin_loop(n):
#     i = 0
#     while i < n:
#         i = i+1
# print(time_execution('spin_loop(1)'))
# print(time_execution('spin_loop(10)'))
# print(time_execution('spin_loop(100)'))
# print(time_execution('spin_loop(1000)'))
# print(time_execution('spin_loop(10000)'))
# print(time_execution('spin_loop(100000)'))
# print(time_execution('spin_loop(1000000)'))



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


    
# 24/ 34 The Hard Way - Question
# 25/ 34 Finding Buckets - Question
# 26/ 34 Adding Keywords - Question
# 27/ 34 Lookup - Question
# 28/ 34 Update - Question
# 29/ 34 Dictionaries
# 30/ 34 Using Dictionaries
# 31/ 34 Population - Question
# 32/ 34 A Noble Gase
# 33/ 34 Modifying The Search Engine - Question
# 34/ 34 Changing Lookup - Question