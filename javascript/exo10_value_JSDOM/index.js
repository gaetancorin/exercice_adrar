txt = document.body.querySelector("textarea");
btn = document.body.querySelector("button");
console.log(txt);
console.log(btn);

txt.addEventListener("keypress", function(){
    if (txt.value.length >= 5){
        btn.disabled = true;
    }
    console.log(txt.value)
})