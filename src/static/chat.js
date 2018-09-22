let socket = new WebSocket("ws://localhost:8080/chatsocket");
let username = prompt("Enter your name");

// Invoke on submit message
// Return false to cancel the default submit action
let sendMessage = () => {
    let messageInput = document.getElementById("message");
    let message = messageInput.value;
    let payload = {
        "message": message,
        "user": username
    }
    socket.send(JSON.stringify(payload));
    messageInput.value = "";
    return false;
}

// Create div element for new message
let createMessageBox = (msgDict) => {
    let messageBox = document.createElement("div");
    messageBox.innerHTML = msgDict.user + ": " + msgDict.message;
    return messageBox
}

// Parse event data and show new message
socket.onmessage = (evt) => {
    let messageDict = JSON.parse(evt.data);
    document.getElementById("messages").appendChild(createMessageBox(messageDict));
}
