import re
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# nltk.download('stopwords')
# nltk.download('punkt')

longest = 0
def scraper(url, resp):
    # print("scrapping...")
    links = []
    global longest 
    try:
        if resp.raw_response:
            # print('Success!, 200 <= raw_response <= 400 ')
            if resp.raw_response.content != b'':
                totalLength = processPage(url, resp)
                #print(url, " num of tokens:", totalLength)
                links = extract_next_links(url, resp)
                isICS(url,resp)
                if totalLength > longest:
                    longest = totalLength
                    urlLenFile = open("report/urlLen.txt", "w")
                    urlLenFile.write("{} LENGTH:{}\n".format(url, totalLength))
                    urlLenFile.close()

                uniqueUrl = open("report/unique.txt", "a")
                uniqueUrl.write("{}\n".format(url))
                uniqueUrl.close()

        else:
            print("Error")
            # print("Code:", resp.raw_response.status_code)Causes ERROR
    except:
        print("Scrapper Broke")

    return [link for link in links if is_valid(link)]


def isICS(url, resp):
    try:
        parsed = urlparse(url)
        if re.match(r".+(\.ics\.uci\.edu)$", parsed.netloc) and re.match(r"/$" + r"|$", parsed.path): 
                soup = BeautifulSoup(resp.raw_response.text, "lxml")
                links = []
                for link in soup.findAll('a'):
                    links.append(link.get('href'))
                
                icsPage = open("report/icsPage.txt", "a")
                icsPage.write("{}, {}\n".format(url,len(links)))
                icsPage.close()


    except TypeError:
        print("TypeError for ", parsed)
        raise


def processPage(url, resp):
    try:
        resp.raw_response.encoding = 'utf-8'
        soup = BeautifulSoup(resp.raw_response.content, "lxml")
        stop_words = set(stopwords.words('english'))

        tokenizer = RegexpTokenizer(r'\w+')
        word_tokens = tokenizer.tokenize(soup.get_text().lower())
        filtered_tokens = [w for w in word_tokens if not w in stop_words]

        return len(filtered_tokens)

    except:
        print("processPage() broke")
        return 0


def extract_next_links(url, resp):
    # print("extracting...")
    # create a list to return to scraper()
    tingz = []
    resp.raw_response.encoding = 'utf-8'
    soup = BeautifulSoup(resp.raw_response.text, "lxml")
    linkers = []
    # reterive all links from webpage
    for link in soup.findAll('a'):
        linkers.append(link.get('href'))

    # check if link is valid and/or relative
    for link in linkers:

        if link != None and re.match(r"/.*", link):
            link = urljoin(url, link)

        if is_valid(link):
            tingz.append(link)

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
        # print("Checking <netloc>: {}".format(parsed.netloc))
        if not re.match(
            r".+\.ics\.uci\.edu"
            + r"|.+\.cs\.uci\.edu"  # |in front helps sperate the searches
            + r"|.+\.informatics\.uci\.edu"
                + r"|.+\.stat\.uci\.edu", parsed.netloc):
            return False
        elif re.match(r"today\.uci\.edu", parsed.netloc) and re.match(r"/department/information_computer_sciences/?", parsed.path.lower()):
            return True

        # print("Checking <netloc>: {} for traps".format(parsed.netloc))
        if re.match(r"(www\.)?calendar", parsed.netloc):
            return False

        if re.match(r"/events"
                    + r"|/calendar", parsed.path.lower()):  # problem area?
            return False

        # Checks the <path> part of the URL to see if it's valid
        # If <path> ends with this file extension   .\.
        # re.match finds a match which returns True, not makes it false
        # print("Checking <path>:{}".format(parsed.path.lower()))
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

        # avoid Queries: it's a crawler trap
        # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        # if re.search(r"replytocom=", parsed.query.lower()):
        #    return False
        if parsed.query:
            return False

        # avoid Fragments : They appear to be self-referential
        if parsed.fragment:
            return False

        return True

    except TypeError:
        print("TypeError for ", parsed)
        raise
