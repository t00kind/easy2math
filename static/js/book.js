let url, elem = null
let elements = document.querySelectorAll('#sel');

for (elem in elements) {
    console.log(elem);
    if (elem.value == "None") {
        elem.setAttribute("disabled", "disabled");
    }
}

function dl(url) {
    if (url) {
        window.open(url, "_blank");
    }
}

