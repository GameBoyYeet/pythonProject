import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "Movies-Golang-EricS",
})

db = firestore.client()

docName = input("")
mov = input("What movie did you get today?")
doc_ref = db.collection(u'movs').document(u'')
