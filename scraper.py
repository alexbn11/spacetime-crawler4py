import re
from urllib.parse import urlparse
import requests


def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

# Implementation required.


def extract_next_links(url, resp):
    # create a list to return to scraper()
    thing = []

    # check if url is valid
    if is_valid(url):
        print("good")

    return thing


def is_valid(url):
    try:
        # Parse a URL into 6 components:
        # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        # Checks the <netloc> part of the url to see if it's valid
        return not re.match(
            r".ics.uci.edu/" |
            + r".cs.uci.edu/" |
            + r".informatics.uci.edu/" |
            + r".stat.uci.edu/" |
            + r"today.uci.edu/department/information_computer_sciences/", parsed.netloc)
        # Checks the <path> part of the URL to see if it's valid
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print("TypeError for ", parsed)
        raise
