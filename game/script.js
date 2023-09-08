// List of questions and names
let questions = [];
let names = [];

// Function to load questions from questions.txt
fetch('questions.txt')
    .then(response => response.text())
    .then(data => {
        questions = data.split('\n');
    });

// Function to load names from names.txt
fetch('names.txt')
    .then(response => response.text())
    .then(data => {
        names = data.split('\n');
    });

function pickRandom() {
    const randomQuestion = questions[Math.floor(Math.random() * questions.length)];
    const randomName = names[Math.floor(Math.random() * names.length)];

    document.getElementById("randomQuestion").textContent = randomQuestion;
    document.getElementById("randomName").textContent = randomName;
}
