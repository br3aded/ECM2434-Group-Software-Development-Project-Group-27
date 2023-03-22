// Author: Matthew Wood

const elem = document.getElementById('code');

let code = elem.innerHTML;
console.log(code)
// Send an AJAX request to a Django view

document.getElementById("next").addEventListener('click', () => {
    const xhr = new XMLHttpRequest();
    console.log("click")
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            response = JSON.parse(xhr.responseText);
            if (response.exists) {
                // Code exists in the Game model, redirect to lobby_view
                console.log("working")
                window.location.href = "/game/lobby/PZMMY"

            } else {
                // Code does not exist in the Game model, do nothing
            }
        }
    }
    xhr.open('GET', `/game/inc_gamestate?code=${code}`);
    xhr.send();
});

