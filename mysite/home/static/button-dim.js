function dim(id) {
    let elem = document.getElementById(id);
    elem.classList.add("button-animation");
    elem.style.filter = ("brightness(0.5)");
}

function undim(id) {
    let elem = document.getElementById(id);
    elem.classList.remove("button-animation");
    elem.style.filter = ("brightness(1)");
}