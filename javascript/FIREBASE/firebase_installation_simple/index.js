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

// On va créer une référence à notre BDD
const dbRef = firebase.database().ref();
// Grace à la fonction .child de firebase, on va créer un schéma qui récupère les informations de la table "users" dans la BDD.
const usersRef = dbRef.child('users');

//".on" est comme un "addEventListener" en Jquery.
// ici, c'est une méthode asynchrone du schéma 'usersRef' qui perdure dans le temps même si la fonction qui l'appelle est terminé

//Lorsqu'il y a un changement des valeurs du schéma "usersRef", l'event s'active et crée un nouveau schéma 'snap' avec les nouvelles valeurs
usersRef.on("value", snap => {
    snap.forEach(childSnap => {
      //On récupère les valeurs(email, name, age) sous forme de dictionnaire pour chaque user en utilisant la méthode .val() du schéma childSnap
      console.log(childSnap.val())
      
    })
})

