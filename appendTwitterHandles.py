import csv

filePeople=open("maindatabase.csv", "rb")
people = csv.reader(filePeople)

newPeople = open("People2.csv", "wb")
cwrite = csv.writer(newPeople)

count= 0
for r in people:
	# print r[0] 
	temp = open("legitnamelist.csv")
	legitList = csv.reader(temp)
	flag=0
	for a in legitList:
		if a[0] == r[0].lower(): 
			twitter = "https://twitter.com/" + a[1]
			cwrite.writerow([r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], twitter])
			count+=1
			flag=1
	temp.close()
	if(flag==0):
		cwrite.writerow([r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11]])
	# print cwrite[12]
print count	

filePeople.close()





