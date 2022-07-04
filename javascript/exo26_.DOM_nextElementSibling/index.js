const elt = document.getElementById('main');
console.log(elt);
// elt nous retourne la div #main avec ses éléments enfants

let children = elt.children;
console.log(children);
// elt.children  nous retournera uniquement les enfants de l'élément  #main

let parent = elt.parentElement
console.log(parent);
// elt.parentElement nous retournera le parent de l'élément #main avec ses éléments enfants

let next = elt.nextElementSibling
console.log(next);
// elt.nextElementSibling nous retournera l'élement qui suit l'élément #main

let previous = elt.previousElementSibling
console.log(previous);
// elt.nextElementSibling nous retournera l'élement qui est avant l'élément #main