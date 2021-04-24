import re
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def scraper(url, resp):
    # print("scrapping...")
    links = []

    if resp.raw_response:
        #print('Success!, 200 <= raw_response <= 400 ')
        links = extract_next_links(url, resp)
    else:
        print('An error has occurred.')

    return [link for link in links if is_valid(link)]

# Implementation required.


def extract_next_links(url, resp):
    # print("extracting...")
    # create a list to return to scraper()
    tingz = []

    resp.raw_response.encoding = 'utf-8'
    soup = BeautifulSoup(resp.raw_response.text, "lxml")
    linkers = []
    for link in soup.findAll('a'):
        linkers.append(link.get('href'))

    # check if url is valid
    for url in linkers:
        if link != None and re.match(r'\/.*', link):
            relativeLink = link
            parsed = urlparse(url)
            link = str(parsed.scheme) + '://' + \
                str(parsed.netloc) + str(link)

        if is_valid(url):
            tingz.append(url)

    return tingz


def is_valid(url):
    try:
        # Parse a URL into 6 components:
        # <scheme>://<netloc>            /<path>;<params>?<query>#<fragment>
        # http    ://calendar.ics.uci.edu/calendar.php   ?type=month&calend
        # http    ://www.w3.org          /Addressing/URL/url-spec.txt
        # https   ://ciir.cs.umass.edu   /downloads/SEIRiP.pdf
        parsed = urlparse(url)

        # if <scheme> != http || https
        if parsed.scheme not in set(["http", "https"]):
            return False
        # Checks the <netloc> part of the url to see if it's valid
        #print("Checking <netloc>: {}".format(parsed.netloc))
        if not re.match(
            r".+\.ics\.uci\.edu"
            + r"|.+\.cs\.uci\.edu"  # |in front helps sperate the searches
            + r"|.+\.informatics\.uci\.edu"
                + r"|.+\.stat\.uci\.edu", parsed.netloc):
            return False
        elif re.match(r"today\.uci\.edu/?", parsed.netloc) and re.match(r"department/information_computer_sciences/?", parsed.path.lower()):
            return True

        #print("Checking <netloc>: {} for traps".format(parsed.netloc))
        if re.match(r"(www\.)?calendar", parsed.netloc):
            return False

        # avoid Queries
        # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        if re.search(r"replytocom=", parsed.query.lower()):
            return False

        # Checks the <path> part of the URL to see if it's valid
        # If <path> ends with this file extension   .\.
        # re.match finds a match which returns True, not makes it false
        #print("Checking <path>:{}".format(parsed.path.lower()))
        if re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
                + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower()):
            return False
        return True

    except TypeError:
        print("TypeError for ", parsed)
        raise
