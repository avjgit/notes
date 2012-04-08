#Rabbits Multiplying 

#A (slightly) more realistic model of rabbit multiplication than the Fibonacci
#model, would assume that rabbits eventually die. For this question, assume that
#every rabbit dies when it is six months old.
#
#Thus, we can model the number of rabbits as: 
#
#rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
#rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
#For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
#rabbits(n) = rabbits(n - 1) + rabbits(n - 2) 
# 
#
#For months > 5:
# All the rabbits that are over 5 months old die, but after first reproducing.
#rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)  
#
#This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ... 
#
#Define a procedure rabbits that takes as input a number n, and returns a 
#number that is the value of the nth number in the rabbit sequence. 
#For example, rabbits(10) -> 35. (It is okay if your procedure takes too 
#                                long to run on inputs above 30.)

def rabbits(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return rabbits(n-1) + rabbits(n-2) - rabbits(n-5)


# print(rabbits(10))
# print(rabbits(10))
#>>> 35

# s = ""
# for i in range(1,12):
   # s = s + str(rabbits(i)) + " "
# print(s)
# >>> 1 1 2 3 5 7 11 16 24 35 52 

    
 
#Spreading Udaciousness
 
#One of our modest goals is to teach everyone in the world to program and
#understand computer science. To estimate how long this will take we have
#developed a (very flawed!) model:

#Everyone answering this question will convince a number, spread, (input to the
#model) of their friends to take the course next offering. This will continue,
#so that all of the newly recruited students, as well as the original students, 
#will convince spread of their
#friends to take the following offering of the course.
#recruited friends are unique, so there is no duplication among the newly
#recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
#target), that takes three inputs: the starting number of Udacians, the spread
#rate (how many new friends each Udacian convinces to join each hexamester), and
#the target number, and outputs the number of hexamesters needed to reach (or
#exceed) the target.

#For credit, your procedure must not use: while, for, or import math. 

def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    return 1 + hexes_to_udaciousness(n + n*spread, spread, target)


#0 more needed, since n already exceeds target
# print(hexes_to_udaciousness(100000, 2, 36230) )
#>>> 0

#after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
# print(hexes_to_udaciousness(50000, 2, 150000) )
#>>> 1 

#need to match or exceed the target
# print(hexes_to_udaciousness(50000, 2, 150001))
#>>> 2 

#only 12 hexamesters (2 years) to world domination!
# print(hexes_to_udaciousness(20000, 2, 7 * 10 ** 9) )
#>>> 12 

#more friends means faster world domination!
# print(hexes_to_udaciousness(15000, 3, 7 * 10 ** 9))
#>>> 10 



#Deep Count 

#The built-in len operator outputs the number of top-level elements in a List,
#but not the total number of elements. For this question, your goal is to count
#the total number of elements in a list, including all of the inner lists.

#Define a procedure, deep_count, that takes as input a list, and outputs the
#total number of elements in the list, including all elements in lists that it
#contains.


#For this procedure, you will need a way to test if a value is a list. We have
#provided a procedure, is_list(p) that does this:

def is_list(p):
    return isinstance(p, list)

#It is not necessary to understand how is_list works. It returns True if the
#input is a List, and returns False otherwise.

def deep_count(p):
    l = len(p)
    for el in p:
        if is_list(el):
            l = l + deep_count(el)
    return l







# print(deep_count([1, 2, 3]))
#>>> 3

# the empty list still counts as an element of the outer list
# print(deep_count([1, [], 3]) )
#>>> 3 

# print(deep_count([1, [1, 2, [3, 4]]]))
#>>> 7

# print(deep_count([[[[[[[[1, 2, 3]]]]]]]]))
#>>> 10
 

 #Feeling Lucky
 
#In Unit 6, we implemented a page ranking algorithm, but didn't finish the final
#step of using it to improve our search results. For this question, you will use
#the page rankings to produce the best output for a given query.

#Define a procedure, lucky_search, that takes as input an index, a ranks
#dictionary (the result of compute_ranks), and a keyword, and returns the one
#URL most likely to be the best site for that keyword. If the keyword does not
#appear in the index, lucky_search should return None.

def lucky_search(index, ranks, keyword):
    urls = lookup(index, keyword)
    if not urls:
        return None
    best = urls[0]
    for url in urls:
        if ranks[url] > ranks[best]:
            best = url
    return best
    
            

cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""",
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""",
}

def get_page(url):
    if url in cache:
        return cache[url]
    return ""


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

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


#Here's an example of how your procedure should work on the test site: 

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)

print(lucky_search(index, ranks, 'Hummus'))
#>>> http://udacity.com/cs101x/urank/kathleen.html

print(lucky_search(index, ranks, 'the'))
#>>> http://udacity.com/cs101x/urank/nickel.html

print(lucky_search(index, ranks, 'babaganoush'))
#>>> None
