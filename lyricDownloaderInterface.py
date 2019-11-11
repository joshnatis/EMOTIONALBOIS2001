#!/usr/bin/env python

import requests
import urllib
import json
import os
from bs4 import BeautifulSoup

client_access_token = "B0ji-zXRGhBl2VQezJGpDVXJAarPyAelHOpAVHw0a4NBthn7XU-wJiCf-lvBwLON"

def searchGenius(search_term):
	#Formatting the request URL for Genius API
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

def createArtistDict(search_results):
	#print("Scraping lyrics...")
	artists = {new_list: [] for new_list in range(0)}
	artist_count = 0

	for item in search_results:
		artist_name = item['result']['primary_artist']['name']
		song_name = item['result']['title'].encode('ascii', 'ignore').decode("utf-8")
		song_name = song_name.replace('/', '')
		URL = item['result']['url']

		#Scrape page for lyrics
		page = requests.get(URL)
		html = BeautifulSoup(page.text, "html.parser") #extracts html as string
		lyrics = html.find("div", class_="lyrics").get_text()

		#if this is the first search result
		if artist_count == 0:
			artists[artist_name] = {song_name : lyrics}
			artist_count += 1
		#artist already exists, append to them
		elif artist_name in artists.keys():
			artists[artist_name][song_name] = lyrics

	# dictionary containing 1 artist, which is a dict containing a dict of song and lyrics
	return artists

def makeArtistDirWithSongs(artists):
	artist_name = [artist for artist in artists]
	artist_name = artist_name[0]
	artist_dir = "/home/josh/master_lyrics_dir/" + artist_name
	#create dir named $artist_name inside of $artist_dir
	if not os.path.exists(artist_dir):
		os.makedirs(artist_dir)

	for artist in artists:
		for song in artists[artist]:
			f = open(artist_dir + "/" + song + ".txt", "w+")
			f.write(artists[artist][song])
			f.close()
			print("Created", artist_dir + "/" + song + ".txt")

def getListFromTxt(filename):
	text_file = open(filename, "r")
	rappers = text_file.read().split('\n')
	text_file.close()
	rappers = list(filter(None, rappers)) # remove blank entries
	return rappers

def scrapeLyricsForArtistsInList(artist_names_list):
	for artist_name in artist_names_list:
		print("Scraping lyrics for", artist_name, "...")
		scrapeLyricsForArtist(artist_name)
	print("Done!")

def scrapeLyricsForArtist(search_term):
	search_results = searchGenius(search_term) #search results for search term
	artists = createArtistDict(search_results) #dict of 1 artist holding their songs + lyrics
	makeArtistDirWithSongs(artists) #adds dir with artistname and songs inside of master dir

def generateArtistsForManualChoosing(search_results):
	print("Scraping lyrics...")
	artists = {new_list: [] for new_list in range(0)}

	for item in search_results:
		artist_name = item['result']['primary_artist']['name']
		song_name = item['result']['title'].encode('ascii', 'ignore').decode("utf-8")
		song_name = song_name.replace('/', '')
		URL = item['result']['url']

		#Scrape page for lyrics
		page = requests.get(URL)
		html = BeautifulSoup(page.text, "html.parser") #extracts html as string
		lyrics = html.find("div", class_="lyrics").get_text()

		if artist_name not in artists.keys():
			artists[artist_name] = {song_name : lyrics}
		else:
			artists[artist_name][song_name] = lyrics

	return artists

def manuallyGetLyrics():
	cont = True
	while cont:
		search_term = input("Search Genius...")
		search_results = searchGenius(search_term)
		artists = generateArtistsForManualChoosing(search_results)
		print("Pick an artist: ")
		artists_list = [artist for artist in artists]
		for i, artist in enumerate(artists_list):
			print("(",i,")", artist)
		artist_name = artists_list[int(input("#"))]

		artist_dir = "/home/josh/master_lyrics_dir/" + artist_name
		#create dir named $artist_name inside of $artist_dir
		if not os.path.exists(artist_dir):
			os.makedirs(artist_dir)

		for artist in artists:
			for song in artists[artist]:
				f = open(artist_dir + "/" + song + ".txt", "w+")
				f.write(artists[artist][song])
				f.close()
				print("Created", artist_dir + "/" + song + ".txt")

		cont = (input("Continue? (y/n) ") == "y")
	print("Finished")
#rappers = getListFromTxt("artistnames.txt")
#scrapeLyricsForArtistsInList(rappers)

manuallyGetLyrics()
