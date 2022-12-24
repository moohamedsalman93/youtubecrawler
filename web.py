import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
i=0
URL = "https://jobssforu.in/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('div',class_= 'mg-posts-sec-inner')
artics=results.find_all('article',class_= 'd-md-flex mg-posts-sec-post align-items-center')

def li(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('div',class_= 'mg-blog-post-box')
    artic=results.find('h1',class_= 'has-text-align-center')
    linkt=artic.find('a')
    return linkt['href']

for artic in artics:
    t=[]
    title=artic.find('h4',class_='entry-title title')
    date=artic.find('span',class_='mg-blog-date')
    linkt=title.find('a')
    t=title.text.strip().split(" ",1)
    print(title.text.strip())
    print(date.text.strip())
    print(li(linkt["href"]))
    db.collection('job').document().set({
          'title':title.text.strip(),
          'topic':t[0],
          'link':li(linkt["href"]),
          'date':date.text.strip(),
          'value':i
          })
