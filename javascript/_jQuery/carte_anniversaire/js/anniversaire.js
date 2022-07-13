// Ecoute le click du block afficher pour afficher le block suivant
$("header").on("click", () => 
$("div:nth-of-type(1)").css("display","block"));

$("div:nth-of-type(1)").on("click", () => 
$("div:nth-of-type(2)").css("display","block"));

$("div:nth-of-type(2)").on("click", () => 
$("div:nth-of-type(3)").css("display","block"));

// Ecoute le click du dernier block pour lancer le gif, changer le texte des paragraphes et la couleur, et faire apparaître le button

$("div:nth-of-type(3)").on("click", () => {
$("body").css("background","url('giphy.webp')");
$("p").text('Arrête ce bazar !');
$("p").css("font-size", "20px");
$("p").css("color", "yellow");

$("button").css("display", "block");
});


// au click du buton, remet tout comme au début

$("button").on("click", () => {
$("div:nth-of-type(1)").css("display","none");
$("div:nth-of-type(2)").css("display","none");
$("div:nth-of-type(3)").css("display","none");
$("button").css("display", "none");
$("p").text('Clique sur moi !');
$("p").css("font-size", "12px");
$("header p").css("color", "white");
$("div:nth-of-type(1) p").css("color", "black");
$("div:nth-of-type(1) p").css("color", "white");
$("div:nth-of-type(1) p").css("color", "black");
$("body").css("background","");
});
