const firebaseConfig = {
    apiKey: "AIzaSyC_AK135jh7eGsNtwWyZ3RpAQeVehYZLaQ",
    authDomain: "projettestadrar.firebaseapp.com",
    projectId: "projettestadrar",
    storageBucket: "projettestadrar.appspot.com",
    messagingSenderId: "99208050807",
    appId: "1:99208050807:web:b7bfbd2d4a2cd52fc66e72"
  };

firebase.initializeApp(firebaseConfig);

// On va créer une référence à notre BDD
const dbRef = firebase.database().ref();
// On va également faire une ref directement dans le noeud / """"table""""
const usersRef = dbRef.child("users");

readUserData();

function readUserData(){
  //récupération de la liste (vide pour le moment)
  const userListUI = document.getElementById('user-list');
  //Sur usersRef on va surveiller les changements de valeur sur la """table"""
  //snap = phoyo de la BDD à ce moment là
  usersRef.on("value", snap =>{
    userListUI.innerHTML = "";
    // On va parcourir snap (table users)
    // childSnap va représenter chaque users
    snap.forEach(childSnap =>{ 
      //On stock les key pour chaque user
      let key = childSnap.key;
      //On stock les valeur correspondantes(email, name, age)
      let value =childSnap.val()
      //creation de la <li></li>
      let $li = document.createElement("li");
      //remplissage de la <li></li>
      $li.innerHTML = value.name;
      //On place un attribut user-key sur chaque <li></li>(l'id de la personne)
      $li.setAttribute("user-key", key);
      //on place dans la liste <ul></ul> les <li> </li> créees
      userListUI.append($li);})

  })




}