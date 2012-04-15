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

# unit    6 
# hw      6 
# unit    7 
# hw      7 
# exam    