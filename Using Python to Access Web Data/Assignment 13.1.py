from urllib.request import urlopen
import xml.etree.ElementTree as ET

# DATA
# http://py4e-data.dr-chuck.net/comments_631349.xml

address = input('Enter location: ')
xml_data = urlopen(address).read()
stuff = ET.fromstring(xml_data)
lst = stuff.findall('comments/comment')

ans = 0
for item in lst:
    ans += int(item.find('count').text)

print(ans)
