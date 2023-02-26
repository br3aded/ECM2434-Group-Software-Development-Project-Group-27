const gameState = {
    "waitingForPlayers": {
        id: 0,
        template: "gamelobby.html",
    },
    "settingTask": {
        id: 1,
        template: "/game/setting_task",
    },
    "respondToTask": {
        id: 2,
        template: "respond-to-task.html"
    },
    "waitingForRanking": {
        id: 3,
        template: "waiting-for-ranking.html"
    },
    "displayCurrentResults": {
        id: 4,
        template: "display-results.html"
    },
    "endOfGame": {
        id: 5,
        template: "end-of-game.html"
    },
};

const currentState = parseInt(getCookie("current-state"));

function getCurrentState() {
    // get task state from database
    return 0;
}

function setCookie(value) {
    var currentState = "current-state" + "=" + encodeURIComponent(value);
    document.cookie = currentState;
}

function getCookie(name) {
    let cookieArr = document.cookie.split(";");
    
    // Loop through the array elements
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");
        
        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if(name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }
    
    // Return null if not found
    return null;
}

function getStateById() {

}

function next() {
    let nextValue = 1 + parseInt(getCookie("current-state"));
    console.log(nextValue);
    setCookie(nextValue);
    window.location.replace("/game/setting_task");
}

if( document.cookie.indexOf("current-state=") < 0) { 
    setCookie(0);
}
else console.log(getCookie("current-state"));
