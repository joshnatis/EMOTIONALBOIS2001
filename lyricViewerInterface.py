import requests
import urllib
import json
from bs4 import BeautifulSoup

client_access_token = "B0ji-zXRGhBl2VQezJGpDVXJAarPyAelHOpAVHw0a4NBthn7XU-wJiCf-lvBwLON"

def searchGenius(search_term):	
	# Format a request URI for the Genius API
	_URL_API = "https://api.genius.com/"
	_URL_SEARCH = "search?q="
	querystring = _URL_API + _URL_SEARCH + urllib.request.quote(search_term)

	request = urllib.request.Request(querystring)
	request.add_header("Authorization", "Bearer " + client_access_token)
	request.add_header("User-Agent", "")

	response = urllib.request.urlopen(request, timeout=3)
	string = response.read().decode('utf-8')
	json_obj = json.loads(string)

	search_results = json_obj['response']['hits'][:]

	return search_results

# Scrapes lyrics off of genius URL
# An artist profile is a dictionary containing dictionaries of their songs and lyrics
# This function returns a dictionary of dictionaries (artist : (song: lyrics))
def generateArtistProfiles(search_results):
	print("Scraping lyrics...")
	artists = {new_list: [] for new_list in range(0)}

	for item in search_results:
## PRINTS TITLE BY ARTIST
##print(item['result']['title'], "by", item['result']['primary_artist']['name'])
		artist_name = item['result']['primary_artist']['name']
		song_name = item['result']['title'] 
	
		URL = item['result']['url']
	
		page = requests.get(URL)
		html = BeautifulSoup(page.text, "html.parser") #extracts html as a string
		lyrics = html.find("div", class_="lyrics").get_text()
		
		#If an artist isnt in the dict yet, add them
		if artist_name not in artists.keys():
			artists[artist_name] = {song_name : lyrics}	
		else:
			artists[artist_name][song_name] = lyrics
	
	return artists
	#print(artists.keys())
	#print(artists['Action Bronson'].keys())
	#print(artists['Action Bronson']['Baby Blue'])
	#print(artists[:])

def seeLyrics(artists):
	print("Pick an artist: ")
	artists_list = [artist for artist in artists]
	for i, artist in enumerate(artists_list):
		print("(",i,")" , artist)
	artist_name = artists_list[int(input("#"))]
	
	print("Pick a song: ")
	songs_list = [song for song in artists[artist_name]]
	for i, song in enumerate(songs_list):
		print("(",i,")", song)
	song_name = songs_list[int(input("#"))]
	
	print("==============")
	print("Lyrics for", song_name, "by", artist_name)
	print("==============")
	
	print(artists[artist_name][song_name])

# AVAILABLE FUNCTIONS:
# * searchGenius(search_term)
# * generateArtistProfiles(search_results) 
# * seeLyrics(artists)

search_term = input("Search Genius for something: ")
search_results = searchGenius(search_term)
artists = generateArtistProfiles(search_results)
seeLyrics(artists)
