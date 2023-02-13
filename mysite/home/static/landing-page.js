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