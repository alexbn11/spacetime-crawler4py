import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


def scraper(url, resp):
    print("scrapping...")
    links=[]
    
    if resp.raw_response:
        print('Success!, 200<= raw_response <=400 ')
        links = extract_next_links(url, resp)
    else:
        print('An error has occurred.')
    
    return [link for link in links if is_valid(link)]

# Implementation required.


def extract_next_links(url, resp):
    print("extracting...")
    # create a list to return to scraper()
    tingz = []

    # check if url is valid
    if is_valid(url):
        print("good")
        tingz.append(url)
    else:
        print("bad")
    print(url)

    return thing


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
        print("Checking <netloc>:", parsed.netloc)
        if not re.match(
            r"w?w?w?.ics.uci.edu/?" |
            + r"w?w?w?.cs.uci.edu/?" |
            + r"w?w?w?.informatics.uci.edu/?" |
            + r"w?w?w?.stat.uci.edu/?" |
            + r"today.uci.edu/?", parsed.netloc):
            return False

        if not re.match(
            r"department/information_computer_sciences/", parsed.path.lower()):
            return False

        print("Checking <netloc>:", parsed.netloc," For traps")
        if re.match(r"calendar", parsed.netloc):
            return False
        # Checks the <path> part of the URL to see if it's valid
        # If <path> ends with this file extension
        # re.match finds a match which returns True, not makes it false
        print("Checking <path>:", parsed.path.lower())
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

    except TypeError:
        print("TypeError for ", parsed)
        raise
