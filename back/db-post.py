import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random

cred = credentials.Certificate('./key/xxx.json')
app = firebase_admin.initialize_app(cred) 

db = firestore.client()
docs = db.collection(u'sample')
doc = docs.document(u'test')
doc.set({
        'hoge': random.randint(1, 100),
        'fuga': random.randint(1, 100),
        'piyo': random.randint(1, 100)
    })
