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

# hw      5 
# unit    6 
# hw      6 
# unit    7 
# hw      7 
# exam    