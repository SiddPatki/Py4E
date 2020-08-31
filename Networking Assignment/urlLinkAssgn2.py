import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL: ")
count = int(input("Enter count:"))
position = int(input("Enter position:"))

i=1
while(i<=count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')

    #extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find

    tags = soup('a')
    j=1
    for tag in tags:
        if(j>position):
            break
        else:
            url = tag.get("href",None)
            j+=1
    print(url)
    i+=1