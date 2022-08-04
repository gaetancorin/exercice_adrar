//Un schéma est une class servant a récupérer les informations dans la BDD.
//Sur firebase, le schéma se crée automatiquement en faisant la requête .child et retourne un objet "database"
const firebaseConfig = {
	apiKey: "AIzaSyC_AK135jh7eGsNtwWyZ3RpAQeVehYZLaQ",
	authDomain: "projettestadrar.firebaseapp.com",
	databaseURL: "https://projettestadrar-default-rtdb.firebaseio.com",
	projectId: "projettestadrar",
	storageBucket: "projettestadrar.appspot.com",
	messagingSenderId: "99208050807",
	appId: "1:99208050807:web:b7bfbd2d4a2cd52fc66e72"
  };
//Avec cette config on initialise l'appli
firebase.initializeApp(firebaseConfig);
// On stock dans une variable la reférence à notre BDD
const dbRef = firebase.database().ref();


// --------------------------
//CREATION DE LA LISTE D UTILISATEURS
// --------------------------
readUserData();

function readUserData() {
	//récupération de l'élément ul 'user-list' (vide pour le moment)
	const userListUI = document.getElementById("user-list");
	// Grace à la fonction .child de firebase, on va créer un schéma qui récupère les informations de la table "users" dans la BDD.
	const usersRef = dbRef.child("users");
	//".on" est comme un "addEventListener" en Jquery.
	// ici, c'est une méthode asynchrone du schéma 'usersRef' qui perdure dans le temps même si la fonction qui l'appelle est terminé
  
	//Lorsqu'il y a un changement des valeurs du schéma "usersRef", l'event s'active et crée un nouveau schéma 'snap' avec les nouvelles valeurs
	usersRef.on("value", snap => {
		//On vide le contenu précédent de ul représentant la liste de nom des utilisateurs
		userListUI.innerHTML = "";
		// On va parcourir le nouveau schéma 'snap'
	  	// on sépare chaque élément du schéma 'snap'(qui est la table users)
	  	// en schéma 'childSnap' (qui est chaque user)
		snap.forEach(childSnap => {
			//On récupère la valeur key pour chaque user en utilisant la méthode .key du schéma ChildSnap
			let key = childSnap.key;
			//On récupère les valeurs(email, name, age) sous forme de dictionnaire pour chaque user en utilisant la méthode .val() du schéma ChildSnap
			let value = childSnap.val();
			//creation d'un <li>
			let $li = document.createElement("li");
			//remplissage du <li> avec le name
			$li.innerHTML = value.name;
			//On place un attribut user-key sur le <li> qui prend comme valeur la key de l'utilisateur sur lequel on est entrain d'itérer
			$li.setAttribute("user-key", key);

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
			deleteIconUI.innerHTML = " ☓";
			deleteIconUI.style.color = "red";
			//on crée un attribut à <span> qui prend comme valeur la key de l'utilisateur sur lequel on est entrain d'itérer
			deleteIconUI.setAttribute("userid", key);
			// <span> aura un addEventListener avec comme callback la fonction 'deleteButtonClicked' qui déclenche la suppression en BDD de l'utilisateur ciblé.
			//Il est important de créer le addEventListener AVANT de le placer dans le DOM, sinon il n'est pas écouté.
			deleteIconUI.addEventListener("click", deleteButtonClicked)

			
   			//On place nos deux <span> à la fin du <li> que l'on est entrain de créer
			$li.append(editIconUI);
			$li.append(deleteIconUI);

      		// On rajout un addEventListener au <li> avec comme callback la fonction 'userClicked' qui déclenche l'affichage des informations de l'utilisateur.
      		//Il est important de créer le addEventListener AVANT de le placer dans le DOM, sinon il n'est pas écouté.
			$li.addEventListener("click", userClicked)
			//On place le <li> que l'on vient de créer dans le <ul>'user-list'
      		//On a fini pour l'itération de cet utilisateur, on passe au suivant.
			userListUI.append($li);

		});
	})
}

// --------------------------
// FONCTION QUI AFFICHE LES INFORMATIONS DE L'UTILISATEUR CIBLÉ EN REMPLISSANT LA DIV 'user-detail'
// --------------------------
function userClicked(event) {
	// Une fonction déclenché sous forme de callback prend comme event plusieurs parametres natifs au callback
	//On va récupérer l'attribut 'user-key'(la key de l'utilisateur ciblé) sur l'élément ou le addEventListener a été déclenché par un click.
    let userId = event.target.getAttribute("user-key");
	//grace à cette key, on va créer un schéma qui récupère les informations de l'utilisateur ciblé dans la BDD.
    const userRef = dbRef.child('users/' + userId);
	//on récupere la div ou l'on va afficher les informations de l'utilisateur.
    let userDetailUI = document.getElementById("user-detail");
	//".on" est comme un "addEventListener" en Jquery.
	// ici, c'est une méthode asynchrone du schéma 'userRef' qui perdure dans le temps même si la fonction qui l'appelle est terminé
  
	//Lorsqu'il y a un changement des valeurs du schéma "userRef"(réprésentant l'utilisateur), l'event s'active et crée un nouveau schéma 'snap' avec les nouvelles valeurs.
    userRef.on("value", snap =>{
		//On vide la div du contenu précédent 
        userDetailUI.innerHTML = "";
	  	// On va parcourir le nouveau schéma 'snap'
	  	// on sépare chaque élément du schéma 'snap'(qui représente l'utilisateur)
	  	// en schéma 'childSnap' (qui est une information précise de l'utilisateur)
		//On trie ensuite si c'est une image ou un paragraphe
        snap.forEach(childSnap =>{

            if (childSnap.key == "image-profil"){
                let $img = document.createElement("img");
				// .val() est une méthode du schéma 'childsnap' qui retourne toutes ses valeurs en format dictionnaire, ou str si il en a qu'une seule
                $img.src = childSnap.val();
				$img.style ="width: 75px";
				//on place dans la <div>'user-detail' le <img> que l'on vient de créer
                userDetailUI.append($img);
            }
            else{
            let $p = document.createElement("p");
			// .key est une méthode du schéma 'childsnap' qui retourne la key
            $p.innerHTML = childSnap.key + " : " + childSnap.val();
			//on place dans la <div>'user-detail' le <p> que l'on vient de créer
            userDetailUI.append($p);}
        })
    })
}

// --------------------------
// FONCTION QUI SUPPRIME UN USER LORS DU CLICK SUR L'ICONE DELETE(le <span> dans le <li>)
// --------------------------
function deleteButtonClicked(event) {
	// Une fonction déclenché sous forme de callback prend comme event plusieurs parametres natifs au callback
	//On va récupérer sur l'élément ou le addEventListener a été déclenché(par un click) l'attribut 'user-key' qui réprésente la key de l'utilisateur ciblé.
	let userID = event.target.getAttribute("userid");
	//grace à cette key, on va créer un schéma qui récupère les informations de l'utilisateur ciblé" dans la BDD.
	const userRef = dbRef.child('users/' + userID);
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
	//On récupère tous les <input> du formulaire d'ajout d'un utilisateur car ils ont tous l'attribut 'user-imput
	const addUserInputsUI = document.getElementsByClassName("user-input");

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
	document.getElementById('leFormulaireAjoutUser').reset();
}


// --------------------------
//FONCTION QUI OUVRE LE FORMULAIRE DE MODIFICATION D'UTILISATEUR ET PRÉREMPLIS LES INPUTS
// --------------------------
function editButtonClicked(event) {
	//On récupère le formulaire de modification d'utilisateur (en display none actuellement).
	let EditUserInputs = document.getElementById('edit-user-module');
	//et on le fait apparaître
	EditUserInputs.style.display = "block";

	// Une fonction déclenché sous forme de callback prend comme event plusieurs parametres natifs au callback
	//On va récupérer l'attribut 'userid'(la key de l'utilisateur ciblé) sur l'élément ou le addEventListener a été déclenché par un click.
	let userId = event.target.getAttribute("userid");
	//grace à cette key, on va créer un schéma qui récupère les informations de l'utilisateur ciblé dans la BDD.
	const userRef = dbRef.child("users/"+userId);

	//Lorsqu'il y a un changement des valeurs de ce schéma, l'event s'active et crée un nouveau schéma 'snap' avec les nouvelles valeurs. 
	userRef.on("value", snap => {
		// On va récupérer tous les inputs dans le formulaire de modification(sauf celui de l'Id)
		const editUserInputsUI = document.querySelectorAll(".edit-user-input");
		//On va créer une boucle du nombre de ses inputs permettant de sélectionner chaque input les un après les autres.
		for(var i = 0; i < editUserInputsUI.length; i++) {
			// pour chaque input, on récupère l'attribut "data-key"  qui est identique à la key du schéma qui possède la valeur que l'on veut mettre dans cette input.
			var key = editUserInputsUI[i].getAttribute("data-key");
			//et on donne comme valeur à l'input la valeur que l'on a ciblé dans le schéma.
        	editUserInputsUI[i].value = snap.val()[key];
    	}
		//Dans firebase, la méthode .val() du schéma de l'utilisateur a toutes les informations de l'utilisateur mais pas l'id.
		//On récupère donc l'input id et on lui assigne la valeur de la variable 'userId' défini plus haut représentant l'id de l'utilisateur ciblé
		document.querySelector(".edit-userid").value = userId;
	});

	//On récupère le bouton à la fin du formulaire de modification
	const saveBtn = document.querySelector("#edit-user-btn");
	//Et à chaque clique sur le bouton, on déclenche la fonction 'saveUserBtnClicked' qui sauvegarde en bdd l'intégralité des informations des inputs contenant les modifications de valeur de l'utilisateur ciblé.
	saveBtn.addEventListener("click", saveUserBtnClicked);
}

// --------------------------
// FONCTION QUI ENREGISTRE EN BDD LES MODIFICATIONS DE L UTILISATEUR CIBLÉ PAR LE FORMULAIRE DE MODIFICATIONS
// --------------------------
function saveUserBtnClicked() {
	//On récupère l'id de l'utilisateur que lon veut modifier dans l'input id
	const userID = document.querySelector(".edit-userid").value;
	//Avec l'id on va pouvoir viser le bon user dans la BDD
	const userRef = dbRef.child('users/' + userID);
	//On crée un objet vide qui sera rempli avec les value des inputs du formulaire
	let editedUserObject = {};
	//On récupère TOUS les inputs du formulaire
	const editUserInputsUI = document.querySelectorAll(".edit-user-input");
	//Ensuite on fait un système de boucle pour remplir l'objet vide avec les value des inputs
	editUserInputsUI.forEach(function(oneInput) {
		//Pour chaque input on récupère les key (data-key) (input du mail, ou du name ou age)
		let key = oneInput.getAttribute("data-key");
		//On rempli notre objet avec les value des inputs (pour chaque key)
  		editedUserObject[key] = oneInput.value;
	});
	userRef.update(editedUserObject);
	//Ensuite on reMasque le formulaire de modif.
	document.getElementById('edit-user-module').style.display = "none";
}


// -------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------

// --------------------
// --------------------
// ARTICLE
// --------------------
// --------------------



// --------------------------
//CREATION DE LA LISTE D ARTICLES
// --------------------------
readArticleData();

function readArticleData() {
	//récupération du <ul>
	const articleListUI = document.getElementById("article-list");
	const articlesRef = dbRef.child('articles');
	//snap représente une ref des articles a chaque modif de valeurs
	articlesRef.on("value", snap => {
		articleListUI.innerHTML = "";
		//childsnap représente un article
		snap.forEach(childSnap => {
			let key = childSnap.key;
			let value = childSnap.val();
			let $li = document.createElement("li");
			$li.innerHTML = value.titre;
			$li.setAttribute("article-key", key);

			// edit icon
			let editIconUI = document.createElement("span");
			editIconUI.class = "edit-article";
			editIconUI.innerHTML = " ✎";
			editIconUI.setAttribute("articleid", key);
            editIconUI.addEventListener("click", editArticleButtonClicked)
            
            // delete icon
			let deleteIconUI = document.createElement("span");
			deleteIconUI.class = "delete-article";
			deleteIconUI.innerHTML = " ☓";
			deleteIconUI.style.color = "red";
			deleteIconUI.setAttribute("articleid", key);
			deleteIconUI.addEventListener("click", deleteArticleButtonClicked)

			
			$li.append(editIconUI);
			$li.append(deleteIconUI);

			$li.addEventListener("click", articleClicked)
			articleListUI.append($li);

		});
	})
}

// --------------------------
// FONCTION QUI AFFICHE LES INFORMATIONS DE L'ARTICLE CIBLÉ EN REMPLISSANT LA DIV 'article-detail'
// --------------------------
function articleClicked(event) {
	//récupère l'attribut de l element qui a déclencher le callback
	let articleId = event.target.getAttribute("article-key");
	//On crée une ref de l 'article ciblé
	const articleRef = dbRef.child('articles/' + articleId);
	// On récup la DIV ou on va afficher les informations
	const articleDetailUI = document.getElementById("article-detail");
	//"snap" représente un article
	articleRef.on("value", snap =>{
		articleDetailUI.innerHTML = "";
		//Childsnap représente une information de l' article
		snap.forEach(childSnap =>{
			//Si la key match avec un regex(qui commence par img)
			if (childSnap.key.match(/^img/)){
                let $img = document.createElement("img");
                $img.src = childSnap.val();
				$img.style ="width: 90px";
                articleDetailUI.append($img);
            }
            else{
            let $p = document.createElement("p");
            $p.innerHTML = childSnap.key + " : " + childSnap.val();
            articleDetailUI.append($p);}
		})
	})
}

// --------------------------
// FONCTION QUI SUPPRIME UN ARTICLE LORS DU CLICK SUR L'ICONE DELETE(le <span> dans le <li>)
// --------------------------
function deleteArticleButtonClicked(event) {
	let articleID = event.target.getAttribute("articleid");
	let articleRef = dbRef.child('articles/' + articleID);
	articleRef.remove();
}

// --------------------------
// FONCTION QUI CRÉE UN NOUVEL ARTICLE
// --------------------------
//On récup le button à la fin du formulaire, on place un adeventListener au click dessus 
const addArticleBtnUI = document.getElementById("add-article-btn");
addArticleBtnUI.addEventListener("click", addArticleBtnClicked);

function addArticleBtnClicked() {
	// Récup des inputs
	const addArticleInputsUI = document.getElementsByClassName("article-input");

 	// Cet objet va stocker les toutes les informations du nouvel article
    let newArticle = {};
    // On fait une boucle pour récupérer les attributs et valeurs de chaque input du formulaire,
	// Et remplir le newArticle
    for (let i = 0; i < addArticleInputsUI.length; i++) {
        let key = addArticleInputsUI[i].getAttribute('data-key');	
		let value = addArticleInputsUI[i].value;
	//l'attribut de l input sert pour créer la key de l'article et la valeur pour la valeur
        newArticle[key] = value;
	}
	//une reférence à notre table articles
	const articlesRef = dbRef.child('articles');
	// on ajoute notre nouvel article dans la BDD
	articlesRef.push(newArticle);
   // On vide les inputs de leur valeur pour un prochain ajout d'article.
	document.getElementById('leFormulaireAjoutArticle').reset();
}


// --------------------------
//FONCTION QUI OUVRE LE FORMULAIRE DE MODIFICATION D'UTILISATEUR ET PRÉREMPLIS LES INPUTS
// --------------------------
function editArticleButtonClicked(event) {
//affiche le formulaire de modification
let EditArticlesInputs = document.getElementById('edit-article-module');
EditArticlesInputs.style.display = "block"

let articleId = event.target.getAttribute("articleid");
//Ref de l'article ciblé
const articleRef = dbRef.child("articles/"+articleId);

// à la modif de l'article ciblé
articleRef.on("value", snap => {
	// on récupère les inputs
	const editArticleInputsUI = document.querySelectorAll(".edit-article-input");
	//boucle de chaque input
    for(var i = 0; i < editArticleInputsUI.length; i++) {
		//On récupère l'attribut de l'input
        var key = editArticleInputsUI[i].getAttribute("data-key");
		//cet attribut est identique a une key de l'article.
		//On peut donc se servir de l'attribut pour trouver une valeur dans l'article.
        editArticleInputsUI[i].value = snap.val()[key];
    }
	//on remplis l'input id de l'id de l'article
	document.querySelector(".edit-articleid").value = articleId;
});
	//Dans le form on récupère le bouton save et on place un addEventListener dessus
	//Qui executera la fonction pour sauvegarder les modifications.
	const saveBtn = document.querySelector("#edit-article-btn");
	saveBtn.addEventListener("click", saveArticleBtnClicked);
}
// --------------------------
// FONCTION QUI ENREGISTRE EN BDD LES MODIFICATIONS DE L'ARTICLE CIBLÉ PAR LE FORMULAIRE DE MODIFICATIONS
// --------------------------
function saveArticleBtnClicked() {
	//On récupère l'id de l'article que lon veut modifier dans l'input id
	const articleID = document.querySelector(".edit-articleid").value;
	//Avec l'id on va pouvoir viser le bon article dans la BDD
	const articleRef = dbRef.child('articles/' + articleID);
	//On crée un objet vide qui sera rempli avec les value des inputs du formulaire
	let editedArticleObject = {};
	//On récupère TOUS les inputs du formulaire
	const editArticleInputsUI = document.querySelectorAll(".edit-article-input");
	//Ensuite on fait un système de boucle pour remplir l'objet vide avec les value des inputs
	editArticleInputsUI.forEach(function(oneInput) {
		//Pour chaque input on récupère les key (data-key) (input du titre ou contenu ou image(1, 2 ou 3))
		let key = oneInput.getAttribute("data-key");
		//On rempli notre objet avec les value des inputs (pour chaque key)
  		editedArticleObject[key] = oneInput.value;
	});
	articleRef.update(editedArticleObject);
	//Ensuite on reMasque le formulaire de modif.
	document.getElementById('edit-article-module').style.display = "none";
}