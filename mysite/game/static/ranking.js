// Input fields
var field1 = document.getElementById("1");
var field2 = document.getElementById("2");
var field3 = document.getElementById("3");

const fields = [field1, field2, field3]

// Pictures

var pic1 = document.getElementById("a1");
var pic2 = document.getElementById("a1");
var pic3 = document.getElementById("a1");

// Ranking

function sort() {
    let values = []
    fields.forEach(elem => {
        values.push(elem.value);
    })
    window.location.href = `/game/results?a=${values[0]}&b=${values[1]}&c=${values[2]}`;
}
