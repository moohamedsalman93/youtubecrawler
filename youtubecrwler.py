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
  'XB.Net',
  ]

for t in tp:
    db.collection('all').document(t).set({
          'topic':'Programming',
          })