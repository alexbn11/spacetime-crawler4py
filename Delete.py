import re
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# Making a get request
response = requests.get('http://www.ics.uci.edu/~sharad/personal-home-page')

response.encoding = 'utf-8'
soup = BeautifulSoup(response.content, "lxml")
stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')
word_tokens = tokenizer.tokenize(soup.get_text().lower())
filtered_tokens = [w for w in word_tokens if not w in stop_words]
example="boot\'s and cuts"
x=tokenizer.tokenize(example)
print(x)

print(filtered_tokens)

def computeWordFrequencies(List):
    wordFreq = OrderedDict() 
    for word in List:
        if word == "":
            continue
        elif word not in wordFreq:
            wordFreq[word] = 1
        else:
            wordFreq[word] += 1
    return wordFreq

# prinitng request text
# print(response.text)
"""
if response:
    print('Success!')
else:
    print('An error has occurred.')

 # http ://calendar.ics.uci.edu/calendar.php?type=month&calend
"""
# <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
# If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.
# Return None if the string does not match the pattern; note that this is different from a zero-length match.
# Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
# If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).
# SEEDURL = https://www.ics.uci.edu,https://www.cs.uci.edu,https://www.informatics.uci.edu,https://www.stat.uci.edu
"""
txt = "ngs.ics.uci.edu"
txt = "www.ics.uci.edu"
txt = "calendar.php?type=month&calend"
parsed = urlparse('https://ngs.ics.uci.edu')
#   'https://evoke.ics.uci.edu/values-in-design-fellows-honored-at-iconference-2013/?replytocom=43778#respond')
parsed2 = urlparse('https://today.uci.edu/department/information_computer_sciences')
#    'http://www.example.com/shoes?sex=men&color=black&size=44&sale=no')
parsed1 = urlparse('https://speedtest.ics.uci.edu/')
# https://www.stat.uci.edu/news/page/2
# print(parsed)
# print(parsed.netloc)
# print(parsed.path)
# print(parsed.query)
#print(parsed1.status_code)
print(parsed)

response = requests.get('https://ngs.ics.uci.edu')
if re.match(r".+(\.ics\.uci\.edu)$", parsed.netloc) and re.match(r"/$" + r"|$", parsed.path): 
    

    soup = BeautifulSoup(response.text, "lxml")
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
"""


    
"""
req = Request("https://www.stat.uci.edu//www.stat.uci.edu/news")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print("Links:", links)


#if re.match(r"(www\.)?calendar"
if re.match(r'/events', parsed2.path.lower()):
    print("TRIGGERED")

if parsed1.fragment:
    print("TRIGGERED")
else:
    print("PASSED")

if parsed.fragment:
    print("FAILED:FRAG")


if parsed.scheme not in set(["http", "https"]):
    print("FAILED:SCHEME")

if not re.match(
    r".+\.ics\.uci\.edu"
    + r"|.+\.cs\.uci\.edu"  # |in front helps sperate the searches
    + r"|.+\.informatics\.uci\.edu"
        + r"|.+\.stat\.uci\.edu", parsed.netloc):
    print("FAILED:NETLOC")
elif re.match(r"today\.uci\.edu/?", parsed.netloc) and re.match(r"department/information_computer_sciences/?", parsed.path.lower()):
    print("PASSED:NETLOC")


if re.match(r"(www\.)?calendar", parsed.netloc):
    print("FAILED:NETLOC")


if parsed.query:
    print("FAILED:QUERY")

"""
"""
parsed = urlparse("http://www.informatics.uci.edu/files/pdf/InformaticsBrochure-March2018")
print(parsed)
if re.match(
    r".*\.(css|js|bmp|gif|jpe?g|ico"
    + r"|png|tiff?|mid|mp2|mp3|mp4"
    + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
    + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
    + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
    + r"|epub|dll|cnf|tgz|sha1"
    + r"|thmx|mso|arff|rtf|jar|csv"
    + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower()):
        print("FAILED:PATH")
else:
    print("Passed:path")        
    
if re.match(
    r".*/(css|js|bmp|gif|jpe?g|ico"
    + r"|png|tiff?|mid|mp2|mp3|mp4"
    + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
    + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
    + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
    + r"|epub|dll|cnf|tgz|sha1"
    + r"|thmx|mso|arff|rtf|jar|csv"
    + r"|rm|smil|wmv|swf|wma|zip|rar|gz)", parsed.path.lower()):
        print("FAILED:PATH2")
else:
    print("Passed:path2")   
    """   
