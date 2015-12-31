import csv
a=open("maindatabase.csv", "rb")
cread = csv.reader(a)
count=0
b=open("temp.csv", "wb")
cwrite = csv.writer(b)
for row in cread:
 	if(row[5]!=''):
 		print row[5]
 		count=count+1
 		word, space, rest = row[0].partition(' ')
 		lastword = row[0].split()[-1]
		cwrite.writerow([row[5]])
print count
a.close()
b.close()