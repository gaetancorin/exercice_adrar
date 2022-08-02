// Se connecte a firebase "firebasetutosimple" "realtime database" sans utiliser npm ni cdn.
// C'est l'ancienne maniere de se connecter a firebase, maintenant, ils forcent l'utilisation de npm
const firebaseConfig = {
  apiKey: "AIzaSyDU5Drjn-nlVLIn_dQwCiodn8Ynt0wVlKE",
  authDomain: "fir-tutosimple.firebaseapp.com",
  databaseURL: "https://fir-tutosimple-default-rtdb.firebaseio.com",
  projectId: "fir-tutosimple",
  storageBucket: "fir-tutosimple.appspot.com",
  messagingSenderId: "739362601872",
  appId: "1:739362601872:web:cea52988d672922b83d115",
  measurementId: "G-E0L3H7N29J"
};
firebase.initializeApp(firebaseConfig);
// (je ne sais plus a quoi correspond firestore)
// var db = firebase.firestore();

// On stock dans une variable la reférence à notre BDD
const dbRef = firebase.database().ref();
//REF à USERS avec un S (ca nous ramène à l'adresse de tous les utilisateurs dans la BDD)
const usersRef = dbRef.child('users');

usersRef.on("value", snap => {
    snap.forEach(childSnap => {
      console.log(childSnap.val())
      
    })
})

