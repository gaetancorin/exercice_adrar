// document.addEventListener("click", function(unEvent){
//   console.log(unEvent, unEvent.pageX, unEvent.pageY)
//   monImg = document.createElement("img")
//   monImg.setAttribute("style","position:absolute; left:"+(unEvent.pageX-30)+"px; top:"+(unEvent.pageY-30)+"px;");
//   monImg.setAttribute("src","https://www.fillmurray.com/60/60");
//   document.body.append(monImg)
// })

//Dans toute la page on reagit au click, on veut capter cet event.
document.addEventListener("click", function(unEvent) {
  //On concole log l'event que l'on capte pour voir si des propriétés 
  //peuvent nous interresser
  console.log(unEvent);
  //on console log les propriétés X et Y du click (clientX, clientY)
  console.log("Coord X",unEvent.x, "-", "Coord Y:", unEvent.y);
  //Ensuite on va créer une image 
  const monImg = document.createElement("img");
  const taille = 90;
  //Puis on va modifier l'attribut SRC de l'image, pour lui asisgner 
  //L'url d'une image de notre choix
  monImg.setAttribute
  //Optimisation : avec la variable taille dans l'url
      ("src",`https://www.placecage.com/${taille}/${taille}/`);
          //Puis on change le type de position (absolute ca se place ou on veut dans la page)
          monImg.style.position = "absolute";
          //pour opti le centrage, on soustrait la moitié de la taille de l"img
          monImg.style.left = unEvent.x - taille /2 + "px";
          monImg.style.top = unEvent.y - taille /2 + "px";
          //On oubli pas de placer l'image dns la page
          document.body.appendChild(monImg);
