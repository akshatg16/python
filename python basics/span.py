import re
import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
spans = soup('span')
numbers = []
for span in spans:
    numbers.append(int(span.string))
print ("sum" ,numbers)