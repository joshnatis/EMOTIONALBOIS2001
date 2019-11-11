# EMOTIONALBOIS2001

## ABOUT
This is temporarily a stash for files related to my project, currently masquerading under the title of EMOTIONALBOIS2001. 

EMOTIONALBOIS2001 is planned to be a collection of visualized data created via sentiment and emotion analysis of lyrics. Hopefully by the end of the process we will find out which artist (within the scope of the project, currently limited to the Hip Hop genre) is the saddest, which is the happiest, and so on ad infinitum.

## CONTENT
* `master_lyrics_dir`
  + a folder containing subfolders of artists and their lyrics (as .txt files)
  
* `artists.txt`
  + a list of the names of all the artists whose music will be analyzed in the project
  
* `scrapeWikiForArtists.py`
  + scrapes Wikipedia's Hip Hop artist page for artist names
   + `artists.txt` was created via this script, plus a few manual additions
   
* `lyricViewerInterface.py`
  + allows you to search Genius for an artists, then pick a song for which you want to view the lyrics
  
* `lyricDownloaderInterface.py`
  + provides a grungy interface to search Genius for artists and download their lyrics
  + is also able to take a .txt file of artists and scrape their lyrics into a directory
  + `master_lyrics_dir` was generated with this script
  
**Notes:**
Don't steal my API token, it's free, just make your own.

`lyricViewerInterface.py` and `lyricDownloaderInterface,py` are mostly identical scripts with some additional functions added in the latter -- I will later combine them under an interface that lets you pick what functionality you want to use (and I'll allow for user input, rather than hardcoded values).

## SOFTWARE
**Genius API, Wikipedia API, Python3, JSON, urllib, Beautiful Soup**

For sentiment/emotion analysis I'm looking at **textblob**, though that's to be determined. To generate tripply visuals I'll likely have to seek out another library (**mathplotlib**?).

## LICENSE
You can steal this when it's finished, but do not touch for now plz.
