import Firebase from 'firebase'
import 'firebase/firestore'
require('dotenv').config();

console.log(process.env.API_KEY)
const config = {
    apiKey: process.env.API_KEY,
    authDomain: process.env.AUTH_DOMAIN,
    projectId: "hackathon-project-fe887", //何故かこれだけ環境変数にできない
    storageBucket: process.env.STORAGE_BUCKET,
    messagingSenderId: process.env.MESSAGING_SENDER_ID,
    appId: process.env.APP_ID,
    measurementId: process.env.MEASUERMENT_ID
}

const firebaseApp = Firebase.initializeApp(config)
const firestore = firebaseApp.firestore()
firestore.settings({ timestampsInSnapshots: true })

export default firestore