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
# 05/ 21 Building The Web Index
# 06/ 21 Add Page To Index - Question
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
