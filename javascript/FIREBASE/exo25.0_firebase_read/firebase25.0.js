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
//on va chercher les informations de la table "users" dans la BDD, on les stocks dans la variable sous forme d'objet database.
const usersRef = dbRef.child("users");

readUserData();

function readUserData(){
  //récupération de la liste (vide pour le moment)
  const userList = document.getElementById('user-list');
//".on" est un "addEventListener" en Jquery.
// on écoute la variable "usersRef" jusqu'a ce qu'il y ai des valeurs ou un changement de valeur,
//puis on fait un callback ou snap représente ses nouvelles valeurs.
  usersRef.on("value", snap =>{
    //On vide le contenu précédent
    userList.innerHTML = "";
    // snap est encore un objet database.
    // On va parcourir snap (table users)
    // childSnap va représenter chaque user sous forme d'objet database
    snap.forEach(childSnap =>{ 
      //On stock la key pour chaque user
      let key = childSnap.key;
      //On stock les valeurs correspondantes(email, name, age)
      let value =childSnap.val()
      console.log(value);
      //creation de la <li></li>
      let $li = document.createElement("li");
      //remplissage de la <li></li>
      $li.innerHTML = value.name;
      //On place un attribut user-key sur chaque <li></li>(qui est la key de la personne dans la BDD)
      $li.setAttribute("user-key", key);
      //on place dans la liste <ul></ul> les <li> </li> créees
      userList.append($li);})

  })




}