// For Firebase JS SDK v7.20.0 and later, measurementId is optional
//La config de firebase
const firebaseConfig = {
    apiKey: "AIzaSyC_AK135jh7eGsNtwWyZ3RpAQeVehYZLaQ",
    authDomain: "projettestadrar.firebaseapp.com",
    projectId: "projettestadrar",
    storageBucket: "projettestadrar.appspot.com",
    messagingSenderId: "99208050807",
    appId: "1:99208050807:web:b7bfbd2d4a2cd52fc66e72"
  };
  //ensuite avec cette config on initialise l'appli
  firebase.initializeApp(firebaseConfig);
// On stock dans une variable la reférence à notre BDD
const dbRef = firebase.database().ref();
//REF à USERS avec un S (ca nous ramène à l'adresse de tous les utilisateurs dans la BDD)
const usersRef = dbRef.child('users');

 


readUserData();
// --------------------------
// READ : il va falloir un système de boucle pour afficherles données de la base.
//On va afficher 1 donnée, et répeter ce système d'affichage TANT que on a des données dans la BDD.
// --------------------------
function readUserData() {
//On va stocker la liste vide en html que l'on remplira avec les données
	const userListUI = document.getElementById("user-list");
//On surveille la BDD QUE si ya des changments de value dans notre objet users.
//On enregistre dans une variable snap ou snapshot (convention)
	usersRef.on("value", snap => {
		userListUI.innerHTML = "";
//snap = Photo de la BDD à ce moment là 
		snap.forEach(childSnap => {
			//on Stock les clé et valeurs
			let key = childSnap.key,
				value = childSnap.val();

			let $li = document.createElement("li");

			// edit icon
			let editIconUI = document.createElement("span");
			editIconUI.class = "edit-user";
			editIconUI.innerHTML = " ✎";
			editIconUI.setAttribute("userid", key);
            editIconUI.addEventListener("click", editButtonClicked)
            
            // delete icon
			let deleteIconUI = document.createElement("span");
			deleteIconUI.class = "delete-user";
			deleteIconUI.innerHTML = " ☓";
			deleteIconUI.setAttribute("userid", key);
			deleteIconUI.addEventListener("click", deleteButtonClicked)

			
			$li.innerHTML = value.name;
			$li.append(editIconUI);
			$li.append(deleteIconUI);

			$li.setAttribute("user-key", key);
			$li.addEventListener("click", userClicked)
			userListUI.append($li);

});
	})
}

// --------------------------
// DISPLAY USER INFO
// --------------------------
// La fonction va prendre en param un event
function userClicked(event) {
	console.log(event)
	// Pour identifier sur quel utilisateur on a cliqué
	// récuperer l'id des USERS via getAttribute
	let userID = event.target.getAttribute("user-key");
	console.log(userID);

	// on vise 1 utilisateur précis dans la BDD via son id
	const userRef = dbRef.child('users/' + userID);
	// On récup la DIV avec l'id user-detail
	const userDetailUI = document.getElementById("user-detail");

	userRef.on("value", snap =>{
		userDetailUI.innerHTML = "";
//on va faire une boucle pour afficher  à côté du nom utilisateur 
//Les paires clé valeur (la boucle affiche autant de paragraphe qu'il ya des key-value)
		snap.forEach(childSnap =>{
			let $p = document.createElement("p");
			$p.innerHTML = childSnap.key + " : " + childSnap.val();
			userDetailUI.append($p);
		})
	})
}

// --------------------------
// ADD
// --------------------------
//On récup le button, on place un adeventListener au click dessus 
const addUserBtnUI = document.getElementById("add-user-btn");
addUserBtnUI.addEventListener("click", addUserBtnClicked);

function addUserBtnClicked() {
	//une reférence à notre table users
	const usersRef = dbRef.child('users');
	// Récup des 3 inputs
	const addUserInputsUI = document.getElementsByClassName("user-input");
	console.log(addUserInputsUI);
 	// Cet objet va stocker les infos du nouvel utilisateur
    let newUser = {};
    // On fait une boucle pour récupérer les valeurs de chaque input dans le formulaire,
	// Et remplir le newUser
    for (let i = 0, len = addUserInputsUI.length; i < len; i++) {
	// Ci dessous on récupère les key et value
        let key = addUserInputsUI[i].getAttribute('data-key');
	// Valeur qu'on récup dans les inputs.	
		let value = addUserInputsUI[i].value;
	// Pour chaque CLé (age, name, et email on les associe à notre nouvel utilisateur)
        newUser[key] = value;
	}
	// on ajoute notre nouvel utilisateur dans la BDD
	usersRef.push(newUser);
	console.log("New User SAVED");
	console.log(`${newUser.name} il a ${newUser.age} ans ,son mail :${newUser.email}`);
	// Pour etre userFriendly une fois le new user ajouté on reset les champs du formulaire
	document.getElementById('leFormulaireAjout').reset();
}

// --------------------------
// DELETE
// --------------------------
function deleteButtonClicked(event) {
		// event.stopPropagation();
		let userID = event.target.getAttribute("userid");
		// on vise 1 user en particulier
		const userRef = dbRef.child('users/' + userID);
		console.log(event);
		console.log(`ADIOS ${event.path[1].innerText}`);
		userRef.remove();
}
// --------------------------
// EDIT : on click sur un user et ca ouvre un formulaire pré rempli pour modifier par la suite ce user
// --------------------------
function editButtonClicked(e) {
//On va afficher le formulaire quand on click sur ✎ icon crayon d'un user
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
