let getAllDrinks = async() => {
     // promesse
    let data = await fetch('http://localhost:3000/getAllDrinks');
    // json
    let count = await data.json();
    console.log(count);
    await seeObject(count)
}
getAllDrinks();



document.querySelectorAll(" body > div").forEach(item => {
  item.addEventListener('click', event => {
    console.log( "Bonjour" );
    let attribute = item.getAttribute("id");
    console.log(attribute);

    document.querySelectorAll(" body > div").forEach(item => {
      let oldChild = item.remove(" body > div > img");
      oldChild = item.remove(" body > div > div ");
      
    });
    let getOneDrink = async() => {
      let env = String('http://localhost:3000/getOneDrink/'+attribute)
      let data = await fetch(env);
      let count = await data.json();
      console.log(count);
      // await seeObject(count)
    }
    getOneDrink();
    
  })
})



let seeObject = async(json) =>{
  let compteur = 0
  // await console.log(count.length);
  await json.forEach( element => {
    compteur += 1;
    let title = element.title;
    let price = (element.price/100);
    let description = element.description;
    let imageUrl = element.imageUrl;
    // console.log(element);
    let idTitle = title.replace(/ /g, "_");

    let newDiv = document.querySelector(" body > div");
    newDiv.className = "drink";
    newDiv.id = idTitle;
    let image = document.createElement("img");
    image.className = idTitle;
    image.setAttribute("src", imageUrl);
    newDiv.appendChild(image);
    otherDiv = document.createElement("div");
    otherDiv.className = 'Content';
    newDiv.appendChild(otherDiv);
    let firstp = document.createElement("p");
    firstp.innerText = title;
    otherDiv.appendChild(firstp);
    let secondp = document.createElement("p");
    secondp.innerText = price;
    otherDiv.appendChild(secondp);
    let thirstp = document.createElement("p");
    thirstp.innerText = title;
    otherDiv.appendChild(thirstp);
  
    document.body.appendChild(newDiv);

  });
}