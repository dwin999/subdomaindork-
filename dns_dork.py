#!/usr/bin/env python
import urllib2
import urllib
import json
import sys
from time import sleep
def find_subdmains(searchstrings):
    url = 'http://ajax.googleapis.com/ajax/services/search/web?'
    params = { 'q': "site:"+target+' -site:www.'+target+searchstrings}
    data = urllib.urlencode(params)
    url = url + data + '&v=1.0'
    print str(url)
    request = urllib2.Request( url,None, {'Referer': 'http://www.duckduckgo.com' })
    response = urllib2.urlopen(request)
    results = json.load(response)
    startlen = len(subdomainlist)
    for reply in results['responseData']['results']:
        if reply['unescapedUrl'] != None:
            print '\n=[Link]= '
            string = reply['unescapedUrl']
            string = string.replace("http://", "")
            string = string.replace("https://", "")
            string = string.replace("www.", "")
            subdomain = string.split("/")
            print subdomain[0] + str(len(subdomainlist))
            subdomainlist.append(subdomain[0])
    if startlen == len(subdomainlist):
        print "no more domains"
        print subdomainlist 
        sys.exit()
            
def update_string(xlist):
    searchstrings = ""
    for item in xlist:
        searchstrings = searchstrings + ' -site:'+item
    return searchstrings
            
target = "lastminute.com"

subdomainlist = []
            
for x in range(20):
    subdomainlist = list(set(subdomainlist)) # removing any duplicate entires
    searchstrings = update_string(subdomainlist)  # create search string from subdomain list
    find_subdmains(searchstrings)  # find those strings 

    
subdomainlist = list(set(subdomainlist)) # removing any duplicate entires
print subdomainlist