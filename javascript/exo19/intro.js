let counter = document.body.querySelector("h2");
const majCounter = async() => {
    let data = await fetch('https://api.countapi.xyz/hit/sltcava/visites')
    console.log(data)
    let count = await data.json()
    console.log(count)
    counter.innerHTML = count.value;
    counter.style.filter = "blur(0)";
}
majCounter()
