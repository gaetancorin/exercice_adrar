let monForm = document.body.querySelector(".bar");
document.addEventListener("scroll", function(){

  let scrollMax = document.body.scrollHeight - innerHeight;
  // console.log("scrollHeight=", document.body.scrollHeight);
  // console.log("innerHeight=", innerHeight);
  // console.log("scrolly=", scrollY);
  let  onEstOu = scrollY / scrollMax * 100;
  console.log(onEstOu);
  // monForm.setAttribute("style","width:"+onEstOu+"%;");
  monForm.style.width = onEstOu+"%";
})

// //On stock la div de laBar
// const laBar = document.querySelector(".bar");

// //On va réagir quand le user scroll dans la page
// addEventListener("scroll", function(event) {
//     console.log(event);
//     //Le scrollMax = hauteur de la page - hauteur de affichage
// const scrollMax = document.body.scrollHeight - innerHeight;
// // On fait un pourcentage du scroll de l'utilisateur
// const onEstOu = scrollY / scrollMax * 100;
// //Enfin on assigne ce pourcentage de scroll
// //à la width(%) du style de la bar.
// laBar.style.width = onEstOu + "%";
//     console.log(`
//     Hauteur page : ${document.body.scrollHeight}
//     Hauteur affichage : ${innerHeight}
//     Scroll Position : ${scrollY}
//     pourcentage de scroll :${onEstOu} %`);
// })