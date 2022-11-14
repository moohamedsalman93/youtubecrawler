from youtubesearchpython import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

i=0
cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred)

db=firestore.client()


tp = [
  'Html',
  'Python',
  'C++',
  'Java',
  'C',
  'Javascript',
  'PHP',
  'Sql',
  'MangoDB',
  'Swift',
  'Kotlin',
  'Go',
  'Solidity',
  'R',
  'TypeScript',
  'Shellscript',
]
img = [
  'html',
  'python',
  'cp',
  'java',
  'c',
  'javascript',
  'php',
  'sql',
  'mangodb',
  'shift',
  'kotlin',
  'go',
  'solidity',
  'r',
  'typescript',
  'linux',
]
#array

def cat(ks):
    Li=[]
    temp=''
    for k in ks:
      temp=temp+k
      Li.append(temp)
    return Li

for t in tp:
    db.collection('all').document(t).set({
          'title':t,
          'topic':'Programming',
          "caseSearch": cat(t.lower()),
          'img':f"https://firebasestorage.googleapis.com/v0/b/cs-explorer.appspot.com/o/Programming%2F{img[i]}.png?alt=media&token=6da31624-f12b-4fa5-a897-9e956959d9b1",
          'value':i
          })
    i=i+1
    print(i)
    print(t)