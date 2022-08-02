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


//CREATION DE LA LISTE D UTILISATEURS
readUserData();

function readUserData(){
  //récupération de l'élément ul 'user-list' (vide pour le moment)
  const userListUI = document.getElementById("user-list");
  //on va chercher les informations de la table "users" dans la BDD, on les stocks dans la variable sous forme d'objet "database".
  const usersRef = dbRef.child("users");
  //".on" est un "addEventListener" en Jquery.
  // on écoute la variable "usersRef" jusqu'a ce qu'il y ai des valeurs ou un changement de valeur,
  //puis on fait un callback ou snap représente ses nouvelles valeurs.
  usersRef.on("value", snap =>{
    //On vide le contenu précédent
    userListUI.innerHTML = "";
    // snap est encore un objet database.
    // On va parcourir snap (qui est la table users)
    // on sépare chaque snap en childSnap qui représente chaque user sous forme d'objet database
    snap.forEach(childSnap =>{
        //On stock les key pour chaque user
        let key = childSnap.key;
        //On stock les valeur correspondantes (email, name, age) sous forme de dictionnaire
        let value = childSnap.val();
        //creation de la <li></li>
        let $li = document.createElement('li');

        // création de l'icone DELETE en élément <span> et ajout du addEventListener avec un callback d'une fonction 'deleteButtonClicked' durant la création de span et AVANT DE LE PLACER DANS LE DOM.
        // le callback déclenche la supression en bdd
        let deleIconUi = document.createElement("span");
        deleIconUi.class = "delete-user";
        deleIconUi.innerText = "  X";
        deleIconUi.style.color = "red";
        deleIconUi.setAttribute("userid",key);
        deleIconUi.addEventListener("click", deleteButtonClicked);
        //remplissage de la <li></li> avec le name
        $li.innerHTML = value.name;
        //On place un attribut user-key sur chaque <li></li>(qui prend comme valeur la key de l'utilisateur dans la BDD)
        $li.setAttribute('user-key', key);
        //On place le <span> DELETE à la fin du <li> de l'utilisateur que l'on est entrain de créer
        $li.append(deleIconUi);
        // ajout du addEventListener de <li> avec un callback d'une fonction 'userClicked' durant la création de li et AVANT DE LE PLACER DANS LE DOM.
        //Le callback déclenche l'affichage des informations
        $li.addEventListener("click", userClicked);
        //on place dans la liste <ul></ul>'user-list' le <li></li> créé
        userListUI.append($li)
        
    })
  })
}

// FONCTION QUI REMPLIS LA DIV 'user-detail' QUI AFFICHE LES DETAILS DE L UTILISATEUR CLIQUÉ
function userClicked(event){
  // Une fonction déclenché sous forme de callback prend comme event plusieurs parametres natif au callback
  // on récupère l'attribut 'user-key' sur l"élément ou le addeventlistener a été déclenché(la ou on clique)
  let userId = event.target.getAttribute("user-key");
  //grace à la key de l'user ciblé, on va chercher les informations de l'user sur la table "users" dans la BDD, on les stocks dans la variable sous forme d'objet "database".
  const userRef = dbRef.child("users/"+userId);
  //on recupere la div ou l'on va afficher les infos de l'user
  let userDetailUI = document.getElementById("user-detail");
  //".on" est un "addEventListener" en Jquery.
  // on écoute la variable "usersRef" jusqu'a ce qu'il y ai des valeurs ou un changement de valeur,
  //puis on fait un callback ou snap représente ses nouvelles valeurs sous forme de database
  userRef.on("value", snap =>{
    // console.log(snap.val());
    //On vide le contenu précédent
    userDetailUI.innerHTML="";
    //pour chaque info de l'utilisateur sous forme de database:
    snap.forEach(childSnap =>{
      //on crée paragraphe, on met la key grace a .key propre à firebase et la value grace a .val() propre à firebase
      let $p = document.createElement('p');
      $p.innerHTML = `${childSnap.key} : ${childSnap.val()}`;
      //on place dans la <div>'user-detail' le <p> créé
      userDetailUI.append($p);
     })
  })
}

// FONCTION QUI SUPPRIME UN USER LORS DU CLICK SUR L'ICONE DELETE
function deleteButtonClicked(event){
  // Une fonction déclenché sous forme de callback prend comme event plusieurs parametres natif au callback
  // on récupère l'attribut 'userid' sur l"élément ou le addeventlistener a été déclenché(la ou on clique)
  let userID = event.target.getAttribute("userid");
  //grace à la key de l'user ciblé, on va chercher les informations de l'user sur la table "users" dans la BDD, on les stocks dans la variable sous forme d'objet "database".
  const userRef = dbRef.child("users/"+userID);
  //On supprime l'user grace a la fonction remove
  userRef.remove();
}


// --------------------------
// CREATE CORRECTION MAIS LE MIEN FONCTIONNE
// --------------------------
const addUserBtnUI = document.getElementById("add-user-btn");
addUserBtnUI.addEventListener("click", addUserBtnClicked);

function addUserBtnClicked() {
    //une reférence à notre table users
    // const usersRef = dbRef.child('users');
    // Récup des 3 inputs
    // const addUserInputsUI = document.getElementsByClassName("user-input");
    const addUserInputsUI = document.querySelectorAll(".user-input");

    console.log(addUserInputsUI);
     // Cet objet va stocker les infos du nouvel utilisateur
    let newUser = {};
    // On fait une boucle pour récupérer les valeurs de chaque input dans le formulaire
    for(let i = 0; i < addUserInputsUI.length; i++){
    // Ci dessous on récupère les key et value
        let key = addUserInputsUI[i].getAttribute('data-key');
    // Valeur qu'on récup dans les inputs.    
        let value = addUserInputsUI[i].value;
    // Pour chaque CLé (age, name, et email on les associe à notre nouvel utilisateur)
        newUser[key] = value;
    }
    //on va chercher les informations de la table "users" dans la BDD, on les stocks dans la variable sous forme d'objet "database".
    const usersRef = dbRef.child("users");
    // on ajoute notre nouvel utilisateur dans la BDD
    usersRef.push(newUser);
    console.log("New User SAVED");
    console.log(`${newUser.name} il a ${newUser.age} ans`);
    document.getElementById('leFormulaireAjout').reset();
}

