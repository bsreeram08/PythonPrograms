import requests
from bs4 import BeautifulSoup
r=requests.get("https://pythonhow.com/example.html")
c=r.content
#print(c)
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())
all=soup.find_all("div",({"class":"cities"}))
for i in all:
    x=i.find_all("h2")[0].text
    print  (x)
