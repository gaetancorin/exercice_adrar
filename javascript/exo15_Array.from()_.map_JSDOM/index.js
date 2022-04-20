let lesImages = document.body.getElementsByTagName("img");
tabImg = Array.from(lesImages);
console.log(tabImg);
console.log(lesImages);


tabImg.map(function(uneImage,index){
  uneImage.addEventListener("load", function(){
    console.log(index);
  })
});