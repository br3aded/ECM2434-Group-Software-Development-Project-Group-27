// Author: Kelsey Holdgate, Matthew Wood

const enterCodeInput = document.getElementById('enter-code');
enterCodeInput.addEventListener('input', () => {
    let code = enterCodeInput.value;
    if (code.length >= 5) {
        console.log(code);
        // Send an AJAX request to a Django view
        
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                if (response.exists) {
                    // Code exists in the Game model, redirect to lobby_view
                    window.location.href = '/game/lobby?code=' + code;
                } else {
                    // Code does not exist in the Game model, do nothing
                }
            }
        };
        xhr.open('GET', `/game/get_game_data?code=${code}`);
        xhr.send();
    }
});