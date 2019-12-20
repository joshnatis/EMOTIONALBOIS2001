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
   
* `lyricsInterface.py`
  + provides a grungy interface to search Genius for artists and view or download their song lyrics
  + is also able to take a .txt file of artists and scrape their lyrics into directories
  + `master_lyrics_dir` was generated with this script

**Notes:**

Don't steal my API token, it's free, just make your own.

TODO: Change scraping mechanism to scrape artists first, then songs once user picks an artist (rather than scraping everything at the start, resulting in a long pause)

## SOFTWARE
**Genius API, Wikipedia API, Python 3, JSON, urllib, Requests, Beautiful Soup**

For sentiment/emotion analysis I'm looking at **textblob**, though that's to be determined. To generate tripply visuals I'll likely have to seek out another library (**mathplotlib**?).

## LICENSE
You can steal this when it's finished, but do not touch for now plz.

## EMOTIONALBOIS2001
![EMOTIONALBOIS2001](https://github.com/joshnatis/EMOTIONALBOIS2001/blob/master/EMBS2001c.jpg)
