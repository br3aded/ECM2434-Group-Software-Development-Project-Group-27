const isMobile = isMobileDevice();

function isMobileDevice() {
    if(/Android|webOS|iPhone|iPad/i.test(navigator.userAgent)) return true;
    else return false
}

function setPageTitle() {
    let titleElem = document.getElementById("title");
    if (isMobile) titleElem.innerHTML = "T";
    else titleElem.innerHTML = "Taskmaster";
}

setPageTitle();

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