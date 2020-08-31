#parse and extract the comment counts from the XML data, compute the sum of the numbers in the file and enter the sum,

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
xml = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)
print("Retrieved ",len(tree)," characters.")


tags = tree.findall("comments/comment")
print("Count ",len(tags))
sum=0
for tag in tags:
    sum+=int(tag.find("count").text)
print("Sum: ",sum)


# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

# counts = tree.findall('.//count')
# Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.