//Un schéma est une class servant a récupérer les informations dans la BDD.
// Sur firebase, le schéma se crée automatiquement en faisant la requête .child et retourne un objet "database"
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


readUserData();

function readUserData(){
  //récupération de l'élément ul 'user-list' (vide pour le moment)
  const userList = document.getElementById('user-list');
  // Grace à la fonction .child de firebase, on va créer un schéma qui récupère les informations de la table "users" dans la BDD.
  const usersRef = dbRef.child("users");
  //".on" est comme un "addEventListener" en Jquery.
  // ici, c'est une méthode asynchrone du schéma 'usersRef' qui perdure dans le temps même si la fonction qui l'appelle est terminé

  //Lorsqu'il y a un changement des valeurs du schéma "usersRef", l'event s'active et crée un nouveau schéma 'snap' avec les nouvelles valeurs
  usersRef.on("value", snap =>{
    //On vide le contenu précédent de ul représentant la liste de nom des utilisateurs
    userList.innerHTML = "";
    // On va parcourir le nouveau schéma 'snap'
    // on sépare chaque élément du schéma 'snap'(qui est la table users)
    // en schéma 'childSnap' (qui est chaque user)
    snap.forEach(childSnap =>{ 
      //On récupère la valeur key pour chaque user en utilisant la méthode .key du schéma ChildSnap
      let key = childSnap.key;
      //On récupère les valeurs(email, name, age) sous forme de dictionnaire pour chaque user en utilisant la méthode .val() du schéma childSnap
      let value =childSnap.val();
      //creation d'un <li>
      let $li = document.createElement("li");
      //remplissage du <li> avec le name
      $li.innerHTML = value.name;
      //On place un attribut user-key sur le <li> qui prend comme valeur la key de l'utilisateur sur lequel on est entrain d'itérer
      $li.setAttribute("user-key", key);
      //On place le <li> que l'on vient de créer dans le <ul>'user-list'
      //On a fini pour l'itération de cet utilisateur, on passe au suivant.
      userList.append($li);})

  })




}