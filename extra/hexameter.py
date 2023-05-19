#Lucas Ross 22 Nov. 2022

import requests as rq #get the requests
from bs4 import BeautifulSoup #parse the html

'''
req = rq.get("https://hexameter.co/scan")

soup = BeautifulSoup(req.content, "html.parser")
verse = soup.find("div", {"class": "default-latin-verse"})

print(verse)
'''

verse = "quis locus Aiaci? Pthiam haec Scyrumve ferantur!"
solution = [None for x in range(0, 4)] #DDSS for example

'''
1. isolate syllables (vowel?)
2. iterate through each word, if it has multiple definitions then make iterators to handle each instance
3. apply rules and figure out solution
'''