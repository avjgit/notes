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

def bucket_find(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket, key)
    if entry:
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




# unit    6 73
# hw      6 --
# hw *    6 --
# unit    7 
# hw      7 
# exam    100%!
# exam *    --

#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.


def reachable(graph, node):





#For example,

graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

#print reachable(graph, 'a')
#>>> ['a', 'c', 'd', 'b']

#print reachable(graph, 'd')
#>>> ['d', 'a', 'c', 'b']

#print reachable(graph, 'e')
#>>> ['e', 'a', 'c', 'd', 'b']


#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def edit_distance(s,t):



#For example:

# Delete the 'a'
#print edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
#print edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
#print edit_distance('peter', 'sarah')
#>>> 5

# One deletion
#print edit_distance('pete', 'peter')
#>>> 1

#Multi-word Queries

#Triple Gold Star

#For this question, your goal is to modify the search engine to be able to
#handle multi-word queries.  To do this, we need to make two main changes:

#    1. Modify the index to keep track of not only the URL, but the position
#    within that page where a word appears.

#    2. Make a version of the lookup procedure that takes a list of target
#    words, and only counts a URL as a match if it contains all of the target
#    words, adjacent to each other, in the order they are given in the input.

#For example, if the search input is "Monty Python", it should match a page that
#contains, "Monty Python is funny!", but should not match a page containing
#"Monty likes the Python programming language."  The words must appear in the
#same order, and the next word must start right after the end of the previous
#word.

#Modify the search engine code to support multi-word queries. Your modified code
#should define these two procedures:

#    crawl_web(seed) => index, graph
#        A modified version of crawl_web that produces an index that includes
#        positional information.  It is up to you to figure out how to represent
#        positions in your index and you can do this any way you want.  Whatever
#        index you produce is the one we will pass into your multi_lookup(index,
#        keyword) procedure.

#    multi_lookup(index, list of keywords) => list of URLs
#        A URL should be included in the output list, only if it contains all of
#        the keywords in the input list, next to each other.


def multi_lookup(index, query):
    


def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
    



cache = {
   'http://www.udacity.com/cs101x/final/multi.html': """<html>
<body>

<a href="http://www.udacity.com/cs101x/final/a.html">A</a><br>
<a href="http://www.udacity.com/cs101x/final/b.html">B</a><br>

</body>
""", 
   'http://www.udacity.com/cs101x/final/b.html': """<html>
<body>

Monty likes the Python programming language
Thomas Jefferson founded the University of Virginia
When Mandela was in London, he visited Nelson's Column.

</body>
</html>
""", 
   'http://www.udacity.com/cs101x/final/a.html': """<html>
<body>

Monty Python is not about a programming language
Udacity was not founded by Thomas Jefferson
Nelson Mandela said "Education is the most powerful weapon which you can
use to change the world."
</body>
</html>
""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None
    





#Here are a few examples from the test site:

#index, graph = crawl_web('http://www.udacity.com/cs101x/final/multi.html')

#print multi_lookup(index, ['Python'])
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

#print multi_lookup(index, ['Monty', 'Python'])
#>>> ['http://www.udacity.com/cs101x/final/a.html']

#print multi_lookup(index, ['Python', 'programming', 'language'])
#>>> ['http://www.udacity.com/cs101x/final/b.html']

#print multi_lookup(index, ['Thomas', 'Jefferson'])
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

#print multi_lookup(index, ['most', 'powerful', 'weapon'])
#>>> ['http://www.udacity.com/cs101x/final/a.html']
