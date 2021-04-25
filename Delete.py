import re
import requests
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
<<<<<<< HEAD

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
#tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!')

example_sent = """This is a sample sentence, showing off the stop words filtration."""

stop_words = set(stopwords.words('english'))

word_tokens = tokenizer.tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(word_tokens)
print(filtered_sentence)


=======
import re
>>>>>>> parent of 7fbbbd7 (Added text processing?)
"""
# Making a get request
response = requests.get('http://www.ics.uci.edu/~sharad/personal-home-page')

# prinitng request text
# print(response.text)

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

txt = "ngs.ics.uci.edu"
txt = "www.ics.uci.edu"
txt = "calendar.php?type=month&calend"
parsed = urlparse('https://today.uci.edu/department/information_computer_sciences')
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
"""

<<<<<<< HEAD
=======
if re.match(r"today\.uci\.edu/?", parsed.netloc) and re.match(r"/department/information_computer_sciences/?", parsed.path.lower()):
    print("Pass")
else :   
    print("fail")        
>>>>>>> parent of 7fbbbd7 (Added text processing?)
'''
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
'''
