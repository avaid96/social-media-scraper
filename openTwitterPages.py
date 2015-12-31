import csv
from bs4 import BeautifulSoup
import webbrowser
import urllib

opener = urllib.FancyURLopener({})

updatedPeople = open("People2.csv", "rb")
cread = csv.reader(updatedPeople)

for r in cread:
	if r[12] != '':
		openerFile = opener.open(r[12])
		htmlFile = openerFile.read()
		soup = BeautifulSoup(htmlFile,"html.parser")
		importantInfo = str(soup.find_all("p", "TweetTextSize TweetTextSize--16px js-tweet-text tweet-text"))
		print importantInfo
updatedPeople.close()

# openerFile = opener.open("https://www.linkedin.com/reg/webmail-connect-entry-v2?flow=1qbwqgl-1x89vr3")
# htmlFile = openerFile.read()
# print htmlFile


