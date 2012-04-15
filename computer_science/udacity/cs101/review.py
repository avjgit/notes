# unit    1 100
# hw      1 89
    given any string s, which of following 
    has always same value as s?
    > a ('a' + s) [1:] #yes, of course (facepalm)
    > b s + ''
    c s[0] + s[1:] # fails for empty?
    d s[0:] #looks like ok..
# unit    2 100
# hw      2 86
    # does this loop finishes? :: no...
    n = any positive integer
    while n != 1:
        if n % 2 == 0: # the % means remainder, so this tests if n is even
            n = n / 2
        else:
            n = 3 * n  +  1
# unit    3 88
# hw      3 88
# unit    4 90
# hw      4 --

# unit    5 68
    #Creating an Empty Hash Table
    #Define a procedure, make_hashtable,
    #that takes as input a number, nbuckets,
    #and outputs an empty hash table with
    #nbuckets empty buckets.

    def make_hashtable(nbuckets):
        hash = []
        for bucket in range(0,nbuckets):
            hash.append([])
        return hash

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

    #Define a procedure,

    #hashtable_add(htable,key,value)

    #that adds the key to the hashtable
    #(in the correct bucket), with the
    #correct value.

    def hashtable_add(htable,key,value):
        bucket = hashtable_get_bucket(htable,keyword)
        bucket.append([key, value])

    def hashtable_get_bucket(htable,keyword):
        return htable[hash_string(keyword,len(htable))]

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

    #Define a procedure,

    #hashtable_update(htable,key,value)

    #that updates the value associated
    #with key. If key is already in the
    #table, change the value to the new
    #value. Otherwise, add a new entry
    #for the key and value.

    #Hint: Use hashtable_lookup as a
    #starting point.

    def hashtable_update(htable,key,value):
        bucket = hashtable_get_bucket(htable,key)
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
                return
        bucket.append([key, value])

    def hashtable_lookup(htable,key):
        bucket = hashtable_get_bucket(htable,key)
        for entry in bucket:
            if entry[0] == key:
                return entry[1]
        return None

    def hashtable_add(htable,key,value):
        bucket = hashtable_get_bucket(htable,key)
        bucket.append([key,value])    


    def hashtable_get_bucket(htable,keyword):
        return htable[hash_string(keyword,len(htable))]

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

# hw      5 71
    Suppose we have a hash table implemented as described in Unit 5 using the hash_string function. Which of the following are true statements?
    Statement 1
    > The number of string comparisons done to lookup a keyword that is not a key in the hash table may be less than the number needed to lookup a keyword that is a key in the hash table.
    Statement 2
    > We should expect the time to lookup most keywords in the hash table will decrease as we increase the number of buckets.
    Statement 3
    It is always better to have more buckets in a hash table.
    Statement 4
    The time to lookup a keyword in the hash table is always less than the time it would take in a linear time list (as used in Unit 4).

#6. In video 28. Update, it was suggested that some of the duplicate code in
#lookup and update could be avoided by a better design.  We can do this by
#defining a procedure that finds the entry corresponding to a given key, and
#using that in both lookup and update.

#Here are the original procedures:

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

#Whenever we have duplicate code like the loop that finds the entry in
#hashtable_update and hashtable_lookup, we should think if there is a better way
#to write this that would avoid the duplication.  We should be able to rewrite
#these procedures to be shorter by defining a new procedure and rewriting both
#hashtable_update and hashtable_lookup to use that procedure.

#Modify the code for both hashtable_update and hashtable_lookup to have the same
#behavior they have now, but using fewer lines of code in each procedure.  You
#should define a new procedure to help with this.  Your new version should have
#approximately the same running time as the original version, but neither
#hashtable_update or hashtable_lookup should include any for or while loop, and
#the block of each procedure should be no more than 6 lines long.

#Your procedures should have the same behavior as the originals.  For example,

table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print hashtable_lookup(table, 'Python') # => Guido van Rossum




# unit    6 
# hw      6 
# unit    7 
# hw      7 
# exam    