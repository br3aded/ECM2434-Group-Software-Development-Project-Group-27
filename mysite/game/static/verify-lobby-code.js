// Author: Kelsey Holdgate, Matthew Wood

const enterCodeInput = document.getElementById('enter-code');
enterCodeInput.addEventListener('input', () => {
    let code = enterCodeInput.value;
    if (code.length >= 5) {
        
        // Send an AJAX request to a Django view
        code = code.toUpperCase()
        console.log(code);
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                if (response.exists) {
                    // Code exists in the Game model, redirect to lobby_view
                    window.location.href = `/game/lobby/${code}`;
                } else {
                    // Code does not exist in the Game model, do nothing
                }
            }
        };
        xhr.open('GET', `/game/add_user?code=${code}`);
        xhr.send();
    }
});