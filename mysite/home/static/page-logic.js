const isMobile = isMobileDevice();

MAX_CODE_LENGTH = 5;

function isMobileDevice() {
    if(/Android|webOS|iPhone|iPad/i.test(navigator.userAgent)) return true;
    else return false
}

function setPageTitle() {
    let titleElem = document.getElementById("title");
    if (isMobile) titleElem.innerHTML = "T";
    else titleElem.innerHTML = "Taskmaster";
}

function checkGameCode() {
    
}

setPageTitle();
