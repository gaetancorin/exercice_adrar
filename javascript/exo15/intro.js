let leTexte = document.body.querySelector("input");
let txtTab = [];
let voyelles = ["a", "e", "i", "o", "u", "y"];

leTexte.addEventListener("keypress", function(unEvent){
  let uneTouche = unEvent.key;
  if (!voyelles.includes(uneTouche)){
    console.log("Consonne !")
    if (!txtTab.includes(uneTouche)){
      txtTab.push(uneTouche)
    }
  }
  console.log(txtTab.join("-"));
})