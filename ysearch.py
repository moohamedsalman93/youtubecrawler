from unicodedata import name
from youtubesearchpython import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

tp = [
  'Html',
  'Python',
  'C++',
  'C#',
  'Java',
  'C',
  'Javascript',
  'PHP',
  'Reactjs',
  'Angularjs',
  'Flutter',
  'Expressjs',
  'Sql',
  'MangoDB',
  'Swift',
  'Kotlin',
  'Go',
  'Solidity',
  'Flask',
  'Django',
  'R',
  'TypeScript',
  'Vuejs',
  'Nodejs',
  'Shellscript',
  '.Net',
  'XB.Net',
  'Asp.Net'
]


def salman(inh):

    cs=CustomSearch(f"{inh} programming",VideoDurationFilter.long,limit=6)

    for i in range(6):
        _name=cs.result()['result'][i]['channel']['name']
        link=cs.result()['result'][i]['link']
        dur=cs.result()['result'][i]['duration']
        icon=cs.result()['result'][i]['channel']['thumbnails'][0]['url']
        view=cs.result()['result'][i]['viewCount']['short']
        thumb=cs.result()['result'][i]['thumbnails'][0]['url']
        url =icon.replace("s68", "s200" )


        db.collection('all').document(inh).collection('nyt').document(_name).set({
          'title':_name,
          'img':url,
          'dur':dur,
          'views':view,
          'topic':inh,
          'url':link,
          'thumb':thumb,
          'value':i
          })

        print("------------------------------")
        print(_name)
        print(link)
        print(dur)
        print(view)
        print(url)
for i in tp:
    salman(i)
    print(i)