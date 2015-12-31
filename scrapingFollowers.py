# To run this program, you will require python 2.7 and the BeautifulSoup library which you can download using a pip installer

from bs4 import BeautifulSoup

import csv
# import BeautifulSoup
import webbrowser
import urllib

opener = urllib.FancyURLopener({})

updatedPeople = open("People2.csv", "rb")
cread = csv.reader(updatedPeople)

b=open("temp.csv", "wb")
cwrite = csv.writer(b)
cwrite.writerow(["working"])
# cwrite.writerow([cread[0][0],0[1],0[2],0[3],0[4],0[5],0[6],0[7],0[8],0[9],0[10],0[11],0[12],"tweets","interests","description"])
for r in cread:
	tweet=""
	following=""
	description = ""
	if r[12] != '':
		openerFile = opener.open(r[12])
		htmlFile = openerFile.read()
		soup = BeautifulSoup(htmlFile,"html.parser")
		onetweet = str(soup.find_all("p", "TweetTextSize TweetTextSize--16px js-tweet-text tweet-text"))
		onetweet=onetweet.replace('<p class="TweetTextSize TweetTextSize--16px js-tweet-text tweet-text" data-aria-label-part="0" lang="en">',"")
		onetweet=onetweet.replace('<p class="TweetTextSize TweetTextSize--16px js-tweet-text tweet-text" data-aria-label-part="0" lang="und">',"")
		onetweet=onetweet.replace('<p class="TweetTextSize TweetTextSize--16px js-tweet-text tweet-text" data-aria-label-part="0" lang="it">',"")
		onetweet=onetweet.replace('<p class="TweetTextSize TweetTextSize--16px js-tweet-text tweet-text" data-aria-label-part="0" lang="in">',"")
		onetweet=onetweet.replace('<p class="TweetTextSize TweetTextSize--16px js-tweet-text tweet-text" data-aria-label-part="0" lang="hi">',"")
		onetweet=onetweet.replace('</p>',"")
		print onetweet
		tweet=tweet+"\n"+onetweet
		onefollowing=str(soup.find_all("a", "ProfileCard-avatarLink js-nav js-tooltip"))
		onefollowing=onefollowing.replace('<a aria-hidden="true" class="ProfileCard-avatarLink js-nav js-tooltip" ',"")
		onefollowing=onefollowing.replace('tabindex="-1"',"")
		onefollowing=onefollowing.replace('<img alt="" class="ProfileCard-avatarImage js-action-profile-avatar"',"")
		onefollowing=onefollowing.replace('</img></a>',"")
		print onefollowing
		following=following+"\n"+onefollowing
		description=str(soup.find_all("p", "ProfileHeaderCard-bio u-dir"))
		description=description.replace('<p class="ProfileHeaderCard-bio u-dir" dir="ltr">',"")
		description=description.replace('</p>',"")
		print description
	cwrite.writerow([r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],tweet,following,description])

updatedPeople.close()