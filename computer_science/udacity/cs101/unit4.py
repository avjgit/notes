# UNIT 4
# 01/ 21 Introduction
# 02/ 21 Data Structures - Question
[
    [keyword, [url1, url2, ..]]
]
# 03/ 21 Add To Index - Question
#Define a procedure, add_to_index,
#that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

#If the keyword is already
#in the index, add the url
#to the list of urls associated
#with that keyword.

#If the keyword is not in the index,
#add an entry to the index: [keyword,[url]]

index = []


#add_to_index(index,'udacity','http://udacity.com')
#add_to_index(index,'computing','http://acm.org')
#add_to_index(index,'udacity','http://npr.org')
#print index => [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

def add_to_index(index,keyword,url): 
    for row in index:
        if row[0] == keyword:
            row[1].append(url)
            return index
    index.append([keyword, [url]])

# 04/ 21 Lookup - Question
#Define a procedure, lookup,
#that takes two inputs:

#   - an index
#   - keyword

#The output should be a list
#of the urls associated
#with the keyword. If the keyword
#is not in the index, the output
#should be an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

#lookup(index,keyword) => ['http://udacity.com','http://npr.org']


def lookup(index,keyword):
    for record in index:
        if record[0] == keyword:
            return record[1]
    return []


# 05/ 21 Building The Web Index
string.split

# 06/ 21 Add Page To Index - Question
#Define a procedure, add_page_to_index,
#that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

#It should update the index to include
#all of the word occurences found in the
#page content by adding the url to the
#word's associated url list.


index = []

#add_page_to_index(index,'fake.text',"This is a test")
#print index => [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    tags = content.split()
    for tag in tags:
        add_to_index(index, tag, url)


# 07/ 21 Finishing The Web Crawler - Question
# 08/ 21 Startup
# 09/ 21 The Internet
# 10/ 21 Networks - Question
# 11/ 21 Smoke Signals
# 12/ 21 Latency - Question
# 13/ 21 Bandwidth
# 14/ 21 Bits - Question
# 15/ 21 Buckets Of Bits
# 16/ 21 What Is Your Bandwidth - Question
# 17/ 21 Traceroute
# 18/ 21 Traveling Data - Question
# 19/ 21 Making A Network
# 20/ 21 Protocols
# 21/ 21 Conclusion
