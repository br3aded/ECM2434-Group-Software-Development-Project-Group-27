const url = window.location.search;
const urlParams = new URLSearchParams(url);

a = urlParams.get("a");
b = urlParams.get("b");
c = urlParams.get("c");

const results = [a,b,c];

var first = results.indexOf('1');
var second = results.indexOf('2');
var third = results.indexOf('3');

const positions = [first, second, third];

const names = ["matthew", "m", "g"];
console.log(results);
console.log(first,second,third);

var images = {
    '0': 'a',
    '1': 'b',
    '2': 'c',
}

function populateRanking() {
    let container = document.getElementById("player-container");
    for (let x = 0; x < 3; x++) {
        let wrapper = document.createElement("div");
        wrapper.classList.add("player");

        let ranking = document.createElement("div");
        ranking.classList.add("name-plate");
        ranking.innerHTML = `#${x+1}`;

        let image = document.createElement("div");
        image.classList.add(`res-icon`);
        image.classList.add(`${images[positions[x]]}`)

        let name = document.createElement("div");
        name.classList.add("name-plate");
        name.innerHTML = names[x];

        wrapper.appendChild(ranking);
        wrapper.appendChild(image);
        wrapper.appendChild(name);
        container.appendChild(wrapper);
    }
}

populateRanking();