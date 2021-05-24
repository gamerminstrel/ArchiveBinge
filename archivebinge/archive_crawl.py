import requests
#import fnmatch
from bs4 import BeautifulSoup

### MISSION OBJECTIVE ###
#Archive_Crawl will ultimately take a webcomic's Archive page
#and parse it to find all the available pages of a webcomic.
#Most comics stick to a set pattern for their pages. 

#Step 1: get a webpage
#archive_page = requests.get('https://comic.galebound.com/comic/archive')
archive_page = requests.get(input("Paste URL to archive page here:"))
site_page = archive_page.url.split('.com', 1)[0] + '.com' 
print (site_page) #debug check

page_links = []
soup = BeautifulSoup(archive_page.text)
for link in soup.findAll('a'):
    page_links.append (link.get('href'))





###################
#To Do:

