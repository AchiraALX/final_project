document.addEventListener('DOMContentLoaded', function () {
    const socket = new WebSocket("ws://0:8000/sock");

    socket.onmessage = (event) => {
        const messages = document.getElementById("messages");
        const li = document.createElement("li");
        li.textContent = event.data;
        messages.appendChild(li);
    };

    function sendMessage() {
        const messageInput = document.getElementById("message");
        const message = messageInput.value;
        socket.send(message);
        messageInput.value = "";
    }
});

const my_sock = (event) => {
    const mySocket = new WebSocket('ws://0:8000/sock/achira')
}