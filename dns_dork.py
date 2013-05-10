#!/usr/bin/env python
import json
import sys
import urllib
from time import sleep

try:    # Python3 renamed urllib2 to urllib.request
    import urllib2
except ImportError:
    import urllib.request as urllib2
    import urllib.parse as urllib

def find_subdomains(searchstrings):
    url = 'http://ajax.googleapis.com/ajax/services/search/web?'
    params = { 'q': "site:"+target+' -site:www.'+target+searchstrings}
    data = urllib.urlencode(params)
    url = url + data + '&v=1.0'
    print(str(url))

    request = urllib2.Request( url,None, {'Referer': 'http://www.duckduckgo.com' })
    response = urllib2.urlopen(request)
    results = json.loads(response.read().decode("utf-8"))
    
    startlen = len(subdomainlist)

    for reply in results['responseData']['results']:
        if reply['unescapedUrl'] != None:
            print('\n=[Link]= ')
            string = reply['unescapedUrl']
            string = string.replace("http://", "")
            string = string.replace("https://", "")
            subdomain = string.split("/")
            print(subdomain[0] + " " + str(len(subdomainlist)))
            subdomainlist.append(str(subdomain[0])) # subdomain[0] is unicode, cast it to str

    if startlen == len(subdomainlist):
        print("no more domains")
        print(subdomainlist)
        sys.exit()
            
def update_string(xlist):
    searchstrings = ""
    for item in xlist:
        searchstrings = searchstrings + ' -site:'+item
    return searchstrings

def get_args():
    global target
    try:
        target = sys.argv[1]
    except:
        print("\nUsage: " + sys.argv[0] + " <target>\n")
        sys.exit(1)


if __name__ == "__main__":
    global target
    get_args()
    subdomainlist = []
            
    for x in range(20):
        subdomainlist = list(set(subdomainlist)) # removing any duplicate entires
        searchstrings = update_string(subdomainlist)  # create search string from subdomain list
        find_subdomains(searchstrings)  # find those strings 

    subdomainlist = list(set(subdomainlist)) # removing any duplicate entires
    subdomainlist.sort()
    print(subdomainlist)