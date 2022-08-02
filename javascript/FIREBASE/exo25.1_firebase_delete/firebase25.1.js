//Un schéma est une class servant a récupérer les informations dans la BDD.
//Sur firebase, le schéma se crée automatiquement en faisant la requête .child et retourne un objet "database"
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

// --------------------------
//CREATION DE LA LISTE D UTILISATEURS
// --------------------------
readUserData();

function readUserData(){
  //récupération de l'élément ul 'user-list' (vide pour le moment)
  const userListUI = document.getElementById("user-list");
  // Grace à la fonction .child de firebase, on va créer un schéma qui récupère les informations de la table "users" dans la BDD.
  const usersRef = dbRef.child("users");
  //".on" est comme un "addEventListener" en Jquery.
  // ici, c'est une méthode asynchrone du schéma 'usersRef' qui perdure dans le temps même si la fonction qui l'appelle est terminé

  //Lorsqu'il y a un changement des valeurs du schéma "usersRef", l'event s'active et crée un nouveau schéma 'snap' avec les nouvelles valeurs
  usersRef.on("value", snap =>{
    //On vide le contenu précédent de ul représentant la liste de nom des utilisateurs
    userListUI.innerHTML = "";
    // On va parcourir le nouveau schéma 'snap'
    // on sépare chaque élément du schéma 'snap'(qui est la table users)
    // en schéma 'childSnap' (qui est chaque user)
    snap.forEach(childSnap =>{
      //On récupère la valeur key pour chaque user en utilisant la méthode .key du schéma ChildSnap
      let key = childSnap.key;
      //On récupère les valeurs(email, name, age) sous forme de dictionnaire pour chaque user en utilisant la méthode .val() du schéma ChildSnap
      let value = childSnap.val();
      //creation d'un <li>
      let $li = document.createElement('li');
      //remplissage du <li> avec le name
      $li.innerHTML = value.name;
      //On place un attribut user-key sur le <li> qui prend comme valeur la key de l'utilisateur sur lequel on est entrain d'itérer
      $li.setAttribute('user-key', key);

      // création de l'élément <span>
      let deleIconUi = document.createElement("span");
      deleIconUi.class = "delete-user";
      deleIconUi.innerText = "  X";
      deleIconUi.style.color = "red";
      //on crée un attribut à <span> qui prend comme valeur la key de l'utilisateur sur lequel on est entrain d'itérer
      deleIconUi.setAttribute("userid",key);
      // <span> aura un addEventListener avec comme callback la fonction 'deleteButtonClicked' qui déclenche la suppression en BDD de l'utilisateur ciblé.
      //Il est important de créer le addEventListener AVANT de le placer dans le DOM, sinon il n'est pas écouté.
      deleIconUi.addEventListener("click", deleteButtonClicked);

      //On place le <span> à la fin du <li> que l'on est entrain de créer
      $li.append(deleIconUi);
      // le <li> aura un addEventListener avec comme callback la fonction 'userClicked' qui déclenche l'affichage des informations de l'utilisateur.
      //Il est important de créer le addEventListener AVANT de le placer dans le DOM, sinon il n'est pas écouté.
      $li.addEventListener("click", userClicked);
      //on place dans la liste <ul>'user-list' le <li> que l'on vient de créer pour cette itération
      userListUI.append($li)
        
    })
  })
}

// --------------------------
// FONCTION QUI AFFICHE LES INFORMATIONS DE L'UTILISATEUR EN REMPLISSANT LA DIV 'user-detail'
// --------------------------
function userClicked(event){
  // Une fonction déclenché sous forme de callback prend comme event plusieurs parametres natifs au callback
  //On va récupérer sur l'élément ou le addEventListener a été déclenché(par un click) l'attribut 'user-key' qui réprésente la key de l'utilisateur ciblé.
  let userId = event.target.getAttribute("user-key");
  //grace à cette key, on va créer un schéma qui récupère les informations de l'utilisateur ciblé dans la table "users" dans la BDD.
  const userRef = dbRef.child("users/"+userId);
  //on récupere la div ou l'on va afficher les informations de l'utilisateur.
  let userDetailUI = document.getElementById("user-detail");
  //".on" est comme un "addEventListener" en Jquery.
  // ici, c'est une méthode asynchrone du schéma 'userRef' qui perdure dans le temps même si la fonction qui l'appelle est terminé

  //Lorsqu'il y a un changement des valeurs du schéma "userRef", l'event s'active et crée un nouveau schéma 'snap' avec les nouvelles valeurs représentant l'utilisateur
  userRef.on("value", snap =>{
    //On vide la div du contenu précédent 
    userDetailUI.innerHTML="";
    // On va parcourir le nouveau schéma 'snap'
    // on sépare chaque élément du schéma 'snap'(qui représente l'utilisateur)
    // en schéma 'childSnap' (qui est une information précise de l'utilisateur)
    snap.forEach(childSnap =>{
      //on crée un élément <p>
      let $p = document.createElement('p');
      //On récupère la key de l'information ciblé en utilisant la méthode .key du schéma ChildSnap
      //On récupère la valeur de l'information en utilisant la méthode .val() du schéma ChildSnap. Comme il n'y a qu'une valeur, on récupère un str et pas un dictionnaire.
      $p.innerHTML = `${childSnap.key} : ${childSnap.val()}`;
      //on place dans la <div>'user-detail' le <p> que l'on vient de créer
      userDetailUI.append($p);
     })
  })
}

// --------------------------
// FONCTION QUI SUPPRIME UN USER LORS DU CLICK SUR L'ICONE DELETE(le <span> dans le <li>)
// --------------------------
function deleteButtonClicked(event){
  // Une fonction déclenché sous forme de callback prend comme event plusieurs parametres natifs au callback
  //On va récupérer sur l'élément ou le addEventListener a été déclenché(par un click) l'attribut 'user-key' qui réprésente la key de l'utilisateur ciblé.
  let userID = event.target.getAttribute("userid");
  //grace à cette key, on va créer un schéma qui récupère les informations de l'utilisateur ciblé dans la table "users" dans la BDD.
  const userRef = dbRef.child("users/"+userID);
  //On utilise la methode .remove() du schéma 'userRef' pour supprimer l'utilisateur ciblé. 
  userRef.remove();
}


// --------------------------
// FONCTION QUI CRÉE UN NOUVEL UTILISATEUR
// --------------------------
// récupération du bouton 'add-user-btn' (le bouton qui valide l'envois du formulaire d'ajout d'un utilisateur )
const addUserBtnUI = document.getElementById("add-user-btn");
//lors du click de ce bouton, crée un callback qui déclenche la fonction addUserBtnClicked
addUserBtnUI.addEventListener("click", addUserBtnClicked);

function addUserBtnClicked() {
  //On récupère tous les éléments inputs du formulaire qui ont tous l'attribut 'user-imput'
  const addUserInputsUI = document.querySelectorAll(".user-input");

  // On crée un dictionnaire vide qui servira a stocker les informations de notre nouvel utilisateur
  let newUser = {};
  // On fait une boucle du nombre d'inputs que l'on a récupéré
  for(let i = 0; i < addUserInputsUI.length; i++){
    // pour chaque Input, on récupère l'attribut data-key qui a une valeur identique à la key utilisé pour stocker une information d'un utilisateur dans la bdd
    let key = addUserInputsUI[i].getAttribute('data-key');
    // pour chaque Input, on récupère la valeur donnée dans l'input    
    let value = addUserInputsUI[i].value;
    // On stocke les informations en relation key:valeur dans notre dictionnaire
      newUser[key] = value;
  }
  // Grace à la fonction .child de firebase, on va créer un schéma qui récupère les informations de la table "users" dans la BDD.
  const usersRef = dbRef.child("users");
  // En utilisant le méthode .push() de notre schéma, on ajoute notre nouvel utilisateur dans la BDD en utilisant le dictionnaire qui contient les informations
  usersRef.push(newUser);
 // On vide les inputs de leur valeur pour un prochain ajout d'utilisateur grace à la fonction .reset() du formulaire
  document.getElementById('leFormulaireAjout').reset();
}
