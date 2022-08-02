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

// On stock dans une variable la reférence à notre BDD
const dbRef = firebase.database().ref();
//on va chercher les informations de "users" dans la BDD, on le les stocks dans la variable.(la bdd resemble a un json)
const usersRef = dbRef.child('users');

//".on" est le "addEventListener" en Jquery.
// on écoute la variable jusqu'a ce qu'il y ai des valeurs ou un changement de valeur,
//puis on fait un callback ou l'on itère ses valeurs pour les afficher en console.
usersRef.on("value", snap => {
    snap.forEach(childSnap => {
      console.log(childSnap.val())
      
    })
})

