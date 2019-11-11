#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

URL="https://en.wikipedia.org/wiki/List_of_hip_hop_musicians"
page=requests.get(URL)
html = BeautifulSoup(page.text, "html.parser")
content = html.findAll("div", class_="div-col")

artists=[]
for item in content:
	section = item.getText()
	artists = artists + (section.split('\n'))

#print(artists)
#artists = artists[:15]
f = open("allpeoples.txt", "w+")

for artist in artists :
	print("--")
	print(artist)
	keep = input("Keep? (y/n) ")
	if keep == "e":
		f.write(artist + "\n")
	else:
		artists.remove(artist)

f.close()
