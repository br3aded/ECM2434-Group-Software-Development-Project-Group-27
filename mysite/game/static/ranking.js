const elem = document.getElementById('code');

let code = elem.innerHTML;
console.log(code)
// Send an AJAX request to a Django view

document.getElementById("add").addEventListener('click', () => {
    const xhr = new XMLHttpRequest();
    console.log("click")
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            response = JSON.parse(xhr.responseText);
            if (response.exists) {
                // Code exists in the Game model, redirect to lobby_view
                console.log("working")
                

            } else {
                // Code does not exist in the Game model, do nothing
            }
        }
    }

    // Promises may be a better solution

    let elem = document.getElementById("container");
    let counter = 0;

    function makeAjaxCall() {
    let child = elem.children[counter];
    let c = child.querySelector("#name");

    let p = child.querySelector("#points");

    if (c) {
        console.log(c.innerHTML);
        console.log(counter)
        xhr.open('GET', `/game/add_points?code=${code}&user=${c.innerHTML}&points=${p.value}&counter=${counter}`);
        xhr.send();
    }
    counter++;
    if (counter < elem.children.length) {
        setTimeout(makeAjaxCall, 200);
    }

    }

    makeAjaxCall()
});

