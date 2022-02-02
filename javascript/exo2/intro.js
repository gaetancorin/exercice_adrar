let titre = document.body.getElementsByTagName("h1")[0];
let para = document.body.getElementsByTagName("p")[0];
console.log(titre)
console.log(para)

document.body.insertBefore(para, titre);