from bs4 import BeautifulSoup
# soup = BeautifulSoup(open("index.html"),"html.parser")
# rahulbhandari=str(soup.find_all("p", "title", "ltr"))
# # print rahulbhandari
# rahulbhandari = rahulbhandari.split('>')
# rahulbhandari=rahulbhandari[1]
# rahulbhandari = rahulbhandari.split('<')
# rahulbhandari=rahulbhandari[0]
# # print rahulbhandari.length
# print rahulbhandari


# soup = BeautifulSoup(open("index.html"),"html.parser")
# # soup = BeautifulSoup(htmlFile,"html.parser")
# importantInfo = str(soup.find_all("p", "TweetTextSize TweetTextSize--16px js-tweet-text tweet-text"))
# print importantInfo

# # updatedPeople.close()

import csv
# import BeautifulSoup
import webbrowser
import urllib

opener = urllib.FancyURLopener({})

updatedPeople = open("People2.csv", "rb")
cread = csv.reader(updatedPeople)

b=open("temp.csv", "wb")
cwrite = csv.writer(b)

# for r in cread:
# 	tweet=""
# 	following=""
# 	if r[12] != '':
		# openerFile = opener.open(r[12])
		# htmlFile = openerFile.read()
		# soup = BeautifulSoup(htmlFile,"html.parser")
		# onetweet = str(soup.find_all("p", "TweetTextSize TweetTextSize--16px js-tweet-text tweet-text"))
		# print onetweet
		# tweet=tweet+"\n"+onetweet
		
# 		# print htmlFile
# 	cwrite.writerow([r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],tweet])

updatedPeople.close()

openerFile = opener.open("https://twitter.com/WhaatsWithYou")
htmlFile = openerFile.read()
print htmlFile
soup = BeautifulSoup(htmlFile,"html.parser")
onetweet = str(soup.find_all("a", "ProfileCard-avatarLink js-nav js-tooltip"))
print onetweet
# tweet=tweet+"\n"+onetweet