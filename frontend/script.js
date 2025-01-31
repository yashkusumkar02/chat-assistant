function sendQuery() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;
    const chatBox = document.getElementById("chat-box");
    
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById("user-input").value = "";

    fetch("/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p><strong>Assistant:</strong> ${data.response}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error("Error:", error);
        chatBox.innerHTML += `<p><strong>Assistant:</strong> Something went wrong.</p>`;
    });
}

function sendSuggestion(question) {
    document.getElementById("user-input").value = question;
    sendQuery();
}