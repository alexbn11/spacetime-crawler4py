import re
import requests
"""
# Making a get request
response = requests.get('http://www.ics.uci.edu/~sharad/personal-home-page')
  
# prinitng request text
#print(response.text)

if response:
    print('Success!')
else:
    print('An error has occurred.')

 # http ://calendar.ics.uci.edu/calendar.php   ?type=month&calend
"""
# If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.
# Return None if the string does not match the pattern; note that this is different from a zero-length match.
# Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
# If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).
# SEEDURL = https://www.ics.uci.edu,https://www.cs.uci.edu,https://www.informatics.uci.edu,https://www.stat.uci.edu

txt = "ngs.ics.uci.edu"
txt = "www.ics.uci.edu"
# r'^(?:www.)?ics\.uci\.edu|.+\.ics\.uci\.edu'
if re.match(r".+\.ics\.uci\.edu", txt):
    print("Matched")
else:
    print("no match")
