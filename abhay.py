from bs4 import BeautifulSoup
soup = BeautifulSoup(open("indexlinkedin.html"),"html.parser")
rahulbhandari=str(soup.find_all("p", "title", "ltr"))
# print rahulbhandari
rahulbhandari = rahulbhandari.split('>')
rahulbhandari=rahulbhandari[1]
rahulbhandari = rahulbhandari.split('<')
rahulbhandari=rahulbhandari[0]
# print rahulbhandari.length
print rahulbhandari



soup = str(soup)

