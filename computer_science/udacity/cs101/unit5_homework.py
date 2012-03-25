# 5.1: Growth
# For which of these procedures does the worst-case running time scale linearly in the number of elements in the input list p?
# (You may assume that the elements in the list are all small numbers)
> sum_list
def sum_list(p):
    sum = 0
    for e in p:
        sum = sum + e
    return sum

has_duplicate_element
def has_duplicate_element(p):
   res = []
   for i in range(0, len(p)):
       for j in range(0, len(p)):
           if i != j and p[i] == p[j]:
               return True
   return False
> mystery
def mystery(p):
   i = 0
   while True:
       if i >= len(p):
           break
       if p[i] % 2:
           i = i + 2
       else:
           i = i + 1
   return i
 
 
5.2: Hash String
Suppose we have a hash table implemented as described in Unit 5 using the hash_string function. Which of the following are true statements?
Statement 1
The number of string comparisons done to lookup a keyword that is not a key in the hash table may be less than the number needed to lookup a keyword that is a key in the hash table.
 
Statement 2
We should expect the time to lookup most keywords in the hash table will decrease as we increase the number of buckets.
 
Statement 3
It is always better to have more buckets in a hash table.
 
Statement 4
The time to lookup a keyword in the hash table is always less than the time it would take in a linear time list (as used in Unit 4).
 
5.3: Is Offered
Dictionaries of Dictionaries (of Dictionaries)
 
The next several questions concern the data structure below for keeping
track of Udacitys courses (where all of the values are strings):
 
{ <hexamester>, { <class>: { <property>: <value>, ... },
                  ... },
  ... }

 
For example,
 
courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }
 
 
 
For the following questions, you will find the
for <key> in <dictionary>:
                   <block>

 
construct useful.  This loops through the key values in the Dictionary.  For
example, this procedure returns a list of all the courses offered in the given
hexamester:
 
def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res
 
Define a procedure, is_offered(courses, course, hexamester), that returns True
if the input course is offered in the input hexamester, and returns False
otherwise.  For example,
 
print is_offered(courses, 'cs101', 'apr2012') => True
print is_offered(courses, 'cs003', 'apr2012') => False

 
 
(Note: it is okay if your procedure produces an error if the input hexamester is not included in courses.  
For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
 
def is_offered(courses, course, hexamester):
    for c in courses[hexamester]:
        if c == course:
            return True
    return False
5.4: When Offered
Define a procedure, when_offered(courses, course), that takes as a courses data
structure and a string representing a class, and returns a list of strings
representing the hexamesters when the input course is offered.  For example,
 
print when_offered (courses, 'cs101') => ['apr2012', 'feb2012']
print when_offered(courses, 'bio893') => []

 
 
def when_offered(courses,course):
    res = []
    for h in courses:
        for c in courses[h]:
            if c == course:
                res.append(h)
    return res

 
5.5: Involved
[Double Gold Star] Define a procedure, involved(courses, person), that takes as
input a courses structure and a person and returns a Dictionary that describes
all the courses the person is involved in.  A person is involved in a course if
they are a value for any property for the course.  The output Dictionary should
have hexamesters as its keys, and each value should be a list of courses that
are offered that hexamester (the courses in the list can be in any order).
 
For example,
 
print involved(courses, 'Dave') => {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}
print involved(courses, 'Peter C.') => {'apr2012': ['cs262'], 'feb2012': ['cs101']}
print involved(courses, 'Dorina') => {'jan2044': ['cs001']}

 
def involved(courses, person):
    res = {}
    for h in courses:
        cs = []
        for c in courses[h]:
            for p in courses[h][c]:
                if courses[h][c][p] == person:
                    cs.append(c)
        if len(cs) > 0:
            res[h] = cs
    return res
 
5.6: Refactoring
6. In video 28. Update, it was suggested that some of the duplicate code in
lookup and update could be avoided by a better design.  We can do this by
defining a procedure that finds the entry corresponding to a given key, and
using that in both lookup and update.
 
Here are the original procedures:
 
def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key, value])
 
def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None
 
 
def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table
 
def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size
 
def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]
 
 
Whenever we have duplicate code like the loop that finds the entry in
hashtable_update and hashtable_lookup, we should think if there is a better way
to write this that would avoid the duplication.  We should be able to rewrite
these procedures to be shorter by defining a new procedure and rewriting both
hashtable_update and hashtable_lookup to use that procedure.
 
Modify the code for both hashtable_update and hashtable_lookup to have the same
behavior they have now, but using fewer lines of code in each procedure.  You
should define a new procedure to help with this.  Your new version should have
approximately the same running time as the original version, but neither
hashtable_update or hashtable_lookup should include any for or while loop, and
the block of each procedure should be no more than 6 lines long.
 
Your procedures should have the same behavior as the originals.  For example,
 
table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print hashtable_lookup(table, 'Python')  => Guido van Rossum

 
 
5.7: Memoization
[Double Gold Star] Memoization is a way to make code run faster by saving
previously computed results.  Instead of needing to recompute the value of an
expression, a memoized computation first looks for the value in a cache of pre-
computed values.
 
Define a procedure, cached_execution(cache, code), that takes in two inputs: a
cache, which is a Dictionary that maps strings representing Python expressions
to their previously computed values, and code, a string that is a Python
expression.  Your procedure should return the value ofO code, but should only
evaluate code if it has not been previously evaluated.
 
def cached_execution(cache,code):
    if code not in cache:
        cache[code] = eval(code)
    return cache[code]
 
 
 
Here is an example showing the desired behavior of cached_execution:
 
def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
 
cache = {}  start cache as an empty dictionary
 first execution (should print out Running factorial and the result)
print cached_execution(cache, 'factorial(50)')                          
 
print "Second time:"
 second execution (should only print out the result)
print cached_execution(cache, 'factorial(50)')
 
 
Here is a more interesting example using cached_execution
(do not worry if you do not understand this, though,
it will be more clear after Unit 6):
 
def cached_fibo(cache, n):
    if n == 1 or n == 0:
        return n
    else:
        return cached_execution(cache, 'cached_fibo(cache, ' + str(n - 1) + ')') \
               + cached_execution(cache, 'cached_fibo(cache, ' + str(n - 2) + ')')
 
cache = {}
 do not try this at home...at least without a cache!

print cached_execution(cache, 'cached_fibo(cache, 100)')

 
Hint: you will need to use the built-in eval function similarly to how we used
it in time_execution.  The eval function takes a string as input, and returns
the result of evaluating that string as a Python expression.