function decode() {
    fetch('/decode/{{ filename }}')
        .then(response => response.text())
        .then(data => {
            document.getElementById('decoded-text').textContent = data;
        });
}

function extract() {
    fetch('/extract/{{ filename }}')
        .then(response => response.text())
        .then(data => {
            document.getElementById('extracted-text').textContent = data;
        });
}
