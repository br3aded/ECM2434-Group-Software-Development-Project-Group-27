// Author: Matthew Wood

const enterCodeInput = document.getElementById('next');
const url = window.location.search;
const urlParams = new URLSearchParams(url);
var response = null;

let code = urlParams.get("code");
// Send an AJAX request to a Django view
const xhr = new XMLHttpRequest();
xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        response = JSON.parse(xhr.responseText);
        if (response.exists) {
            // Code exists in the Game model, redirect to lobby_view
            console.log("working")
            populateMaxPlayers();
            fillGameInfo()
        } else {
            // Code does not exist in the Game model, do nothing
        }
    }
};

let username_header = document.getElementById("username");
let username = username_header.innerHTML;
console.log(username);
xhr.open('GET', `/game/get_game_data?code=${code}`);
xhr.send();

function populateMaxPlayers() {
    let data = response["data"];
    console.log(data)
    console.log(response["users"])

    let users = response["users"];
    users.forEach(user => {
        createPlayer(user);
    });
}

function createPlayer(name) {
    let container = document.getElementById("player-container");
    let players = document.createElement("div");
    players.classList.add("player");
    let icon = document.createElement("div");
    icon.classList.add("icon");

    let nameplate = document.createElement("div");
    nameplate.classList.add("name-plate")
    nameplate.innerHTML = name;

    players.appendChild(icon);
    players.appendChild(nameplate);

    container.appendChild(players);
}

function fillGameInfo() {
    let data = response["data"];
    let name = document.getElementById("name");
    name.innerHTML = data["game_name"];

    let code = document.getElementById("code");
    code.innerHTML = data["game_code"];
}
