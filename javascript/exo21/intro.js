let email = document.body.querySelector("input");
console.log(email.value)

document.addEventListener("keyup", myFunction);

function myFunction() {
    console.log(email.value);
}