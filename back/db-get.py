import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./key/***.json')
app = firebase_admin.initialize_app(cred) 

db = firestore.client()
ref = db.collection(u'sample')
docs = ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))