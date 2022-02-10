let monForm = document.body.querySelector("form");

monForm.addEventListener("submit", function(event) {
    event.preventDefault();
    console.log(event);
    monForm.reset();
  });

