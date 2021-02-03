const firebase = require("firebase");
// Required for side-effects
require("firebase/firestore");

// Initialize Cloud Firestore through Firebase
firebase.initializeApp({
    apiKey: '-----BEGIN PRIVATE KEY-----************',
    authDomain: 'https://accounts.google.com/o/oauth2/auth',
    projectId: 'hackathon-project-fe887'
});
var db = firebase.firestore();

db.collection("#コロナ").get().then(function(querySnapshot) {
    querySnapshot.forEach(function(doc) {
        // doc.data() is never undefined for query doc snapshots
        console.log(doc.id, " => ", doc.data());
    });
});