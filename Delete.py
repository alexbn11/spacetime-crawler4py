import re
import requests
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from urllib.parse import urlparse
from bs4 import BeautifulSoup
"""
# Making a get request
response = requests.get('http://www.ics.uci.edu/~sharad/personal-home-page')
  
# prinitng request text
#print(response.text)

if response:
    print('Success!')
else:
    print('An error has occurred.')

 # http ://calendar.ics.uci.edu/calendar.php?type=month&calend
"""
#<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
# If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.
# Return None if the string does not match the pattern; note that this is different from a zero-length match.
# Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
# If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).
# SEEDURL = https://www.ics.uci.edu,https://www.cs.uci.edu,https://www.informatics.uci.edu,https://www.stat.uci.edu

txt = "ngs.ics.uci.edu"
txt = "www.ics.uci.edu"
txt = "calendar.php?type=month&calend"
parsed = urlparse('https://evoke.ics.uci.edu/values-in-design-fellows-honored-at-iconference-2013/?replytocom=43778#respond')
print(parsed)
print(parsed.netloc)
print(parsed.path)
print(parsed.query)


if re.match(r".*\?", parsed.netloc):
    print("question?")


