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

      	// création de l'élément <span> qui sera notre bouton de MODIFICATION d'utilisateur
		let editIconUI = document.createElement("span");
		editIconUI.class = "edit-user";
		editIconUI.innerHTML = " ✎";
		//on crée un attribut à <span> qui prend comme valeur la key de l'utilisateur sur lequel on est entrain d'itérer
		editIconUI.setAttribute("userid", key);
		// <span> aura un addEventListener avec comme callback la fonction 'editButtonClicked' qui fait apparaître le formulaire pour modifier en BDD l'utilisateur ciblé.
		//Il est important de créer le addEventListener AVANT de le placer dans le DOM, sinon il n'est pas écouté.
		editIconUI.addEventListener("click", editButtonClicked)
				
		// création de l'élément <span> qui sera notre bouton de SUPPRESSION d'utilisateur
		let deleteIconUI = document.createElement("span");
		deleteIconUI.class = "delete-user";
		deleteIconUI.innerText = "  X";
		deleteIconUI.style.color = "red";
		//on crée un attribut à <span> qui prend comme valeur la key de l'utilisateur sur lequel on est entrain d'itérer
		deleteIconUI.setAttribute("userid",key);
		// <span> aura un addEventListener avec comme callback la fonction 'deleteButtonClicked' qui déclenche la suppression en BDD de l'utilisateur ciblé.
		//Il est important de créer le addEventListener AVANT de le placer dans le DOM, sinon il n'est pas écouté.
		deleteIconUI.addEventListener("click", deleteButtonClicked);

			
   		//On place nos deux <span> à la fin du <li> que l'on est entrain de créer
		$li.append(editIconUI);
		$li.append(deleteIconUI);
      	// On rajout un addEventListener au <li> avec comme callback la fonction 'userClicked' qui déclenche l'affichage des informations de l'utilisateur.
      	//Il est important de créer le addEventListener AVANT de le placer dans le DOM, sinon il n'est pas écouté.
		$li.addEventListener("click", userClicked)
		//On place le <li> que l'on vient de créer dans le <ul>'user-list'
      	//On a fini pour l'itération de cet utilisateur, on passe au suivant.
		userListUI.append($li);

		})
	})
}

// --------------------------
// FONCTION QUI AFFICHE LES INFORMATIONS DE L'UTILISATEUR CIBLÉ EN REMPLISSANT LA DIV 'user-detail'
// --------------------------
function userClicked(event){
	// Une fonction déclenché sous forme de callback prend comme event plusieurs parametres natifs au callback
	//On va récupérer l'attribut 'user-key'(la key de l'utilisateur ciblé) sur l'élément ou le addEventListener a été déclenché par un click.
	let userId = event.target.getAttribute("user-key");
	//grace à cette key, on va créer un schéma qui récupère les informations de l'utilisateur ciblé dans la BDD.
	const userRef = dbRef.child("users/"+userId);
	//on récupere la div ou l'on va afficher les informations de l'utilisateur.
	let userDetailUI = document.getElementById("user-detail");
	//".on" est comme un "addEventListener" en Jquery.
	// ici, c'est une méthode asynchrone du schéma 'userRef' qui perdure dans le temps même si la fonction qui l'appelle est terminé
  
	//Lorsqu'il y a un changement des valeurs du schéma "userRef"(réprésentant l'utilisateur), l'event s'active et crée un nouveau schéma 'snap' avec les nouvelles valeurs.
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
	//grace à cette key, on va créer un schéma qui récupère les informations de l'utilisateur ciblé" dans la BDD.
	const userRef = dbRef.child("users/"+userID);
	//On utilise la methode .remove() du schéma 'userRef' pour supprimer l'utilisateur ciblé. 
	userRef.remove();
  }

// --------------------------
// FONCTION QUI CRÉE UN NOUVEL UTILISATEUR
// --------------------------
// récupération du bouton 'add-user-btn' (le bouton qui valide l'ajout d'un utilisateur après avoir remplis le formulaire)
const addUserBtnUI = document.getElementById("add-user-btn");
//lors du click de ce bouton, crée un callback qui déclenche la fonction addUserBtnClicked
addUserBtnUI.addEventListener("click", addUserBtnClicked);

function addUserBtnClicked() {
	//On récupère tous les <input> du formulaire d'ajout d'un utilisateur car ils ont tous l'attribut 'user-imput'
	const addUserInputsUI = document.querySelectorAll(".user-input");
  
	// On crée un dictionnaire vide qui servira a stocker les informations de notre nouvel utilisateur
	let newUser = {};
	// On fait une boucle du nombre d'inputs que l'on a récupéré
	for(let i = 0; i < addUserInputsUI.length; i++){
	  // pour chaque Input, on récupère l'attribut data-key qui a une valeur identique à la key utilisé pour stocker une information d'utilisateur dans la bdd
	  let key = addUserInputsUI[i].getAttribute('data-key');
	  // pour chaque Input, on récupère la valeur de l'input    
	  let value = addUserInputsUI[i].value;
	  // On stocke les informations en relation key:valeur dans notre dictionnaire
	  // Une fois tous les inputs itérés, on aura toutes les informations de l"utilisateur dans notre dictionnaire.
		newUser[key] = value;
	}
	// Grace à la fonction .child de firebase, on va créer un schéma qui récupère tous les utilisateurs de la table "users" dans la BDD.
	const usersRef = dbRef.child("users");
	// En utilisant le méthode .push() de notre schéma, on ajoute notre nouvel utilisateur dans la BDD en utilisant le dictionnaire qui contient les informations
	usersRef.push(newUser);
   // On vide les inputs de leur valeur pour un prochain ajout d'utilisateur grace à la fonction .reset() du formulaire
	document.getElementById('leFormulaireAjout').reset();
}


// --------------------------
// EDIT : on click sur le bouton de modification ✎ d'un utilisateur et ca ouvre un formulaire pré rempli pour modifier par la suite cet utilisateur
// --------------------------
function editButtonClicked(e) {
//On récupère le formulaire de modification en display none et on le fait apparaître.
document.getElementById('edit-user-module').style.display = "block";
//setup du userID sur le input caché hidden
document.querySelector(".edit-userid").value = e.target.getAttribute("userid");
// on vise le bon Ga dans la BDD via son ID 
const userRef = dbRef.child('users/' + e.target.getAttribute("userid"));
// setup  des données sur les champs utilisateurs pré remplir les input du formulaire
const editUserInputsUI = document.querySelectorAll(".edit-user-input");
console.log(editUserInputsUI);

// On pré rempli le formulaire pour editer (en récupérant les key et valeurs)
userRef.on("value", snap => {
    for(var i = 0, len = editUserInputsUI.length; i < len; i++) {
		//On récupère les KEY (name, mail,age)
        var key = editUserInputsUI[i].getAttribute("data-key");
		//Pour chaque value des inputs, on lui assigne la valeur de la key
                editUserInputsUI[i].value = snap.val()[key];
    }
});
	//Dans le form on récupère le bouton save et on place un addEventListener dessus
	//Qui executera la fonction pour sauvegarder les modifications.
	const saveBtn = document.querySelector("#edit-user-btn");
	saveBtn.addEventListener("click", saveUserBtnClicked);
}
// --------------------------
// EDIT - SAVE - UPDATE
// --------------------------
function saveUserBtnClicked() {
	//On récupère l'id de l'utilisateur que lon veut modifier
	const userID = document.querySelector(".edit-userid").value;
	//Avec l'id on va pouvoir viser le bon user dans la BDD
	const userRef = dbRef.child('users/' + userID);
	//On crée un objet vide qui sera rempli avec les value des inputs du formulaire
	let editedUserObject = {};
	//On récupère TOUS les inputs du formulaire
	const editUserInputsUI = document.querySelectorAll(".edit-user-input");
	//Ensuite on fait un système de boucle pour remplir l'objet vide avec les value des inputs
	editUserInputsUI.forEach(function(textField) {
		//Pour chaque input on récupère les key (data-key) (input du mail, ou du name ou age)
		let key = textField.getAttribute("data-key");
		// let value = textField.value;
  		// editedUserObject[textField.getAttribute("data-key")] = textField.value
		//On rempli notre objet avec les value des inputs (pour chaque key)
  		editedUserObject[key] = textField.value;
	});
	userRef.update(editedUserObject);
    console.log("USER UPDATED");
	//Ensuite on reMasque le formulaire de modif.
	document.getElementById('edit-user-module').style.display = "none";
}
