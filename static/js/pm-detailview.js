const userName_id = JSON.parse(document.querySelector('#json-username').textContent)
const requestUser_id = JSON.parse(document.querySelector('#json-requestusername').textContent)
const privateMsgSocket = new WebSocket(`wss://${window.location.host}/ws/private-message/${requestUser_id}/${userName_id}/`)
privateMsgSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.is_request_user) {
        const startDiv = document.querySelector('.start-div');
        const container = document.createElement('div');
        container.classList.add('d-flex', 'flex-row', 'justify-content-start');
        const avatar = document.createElement('img');
        avatar.src = 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp';
        avatar.alt = 'avatar 1';
        avatar.style.width = '45px';
        avatar.style.height = '100%';
        container.appendChild(avatar);
        chatmessage = document.createElement('div');
        chatmessage.classList.add('person-first');
        container.appendChild(chatmessage);
        startDiv.appendChild(container);


        const message = document.createElement('p');
        message.classList.add('message-bubble', 'small', 'p-2', 'ms-3', 'mb-1', 'rounded-3');

        const timeSpan = document.createElement('span');
        timeSpan.classList.add('d-block', 'message-time');

        const currentDate = new Date();
        const formattedDate = currentDate.toLocaleString('en-US', {
            weekday: 'short',
            hour: 'numeric',
            minute: 'numeric',
            hour12: true
        });

        timeSpan.textContent = formattedDate;

        const messageContent = document.createTextNode(data.message);
        message.appendChild(timeSpan);
        message.appendChild(messageContent);

        chatmessage.appendChild(message);

        scroll();
    } else {
        const startDiv = document.querySelector('.start-div');
        const container = document.createElement('div');
        container.classList.add('d-flex', 'flex-row', 'justify-content-end', 'mb-4', 'pt-1');
        const personSecond = document.createElement('div');
        personSecond.classList.add('person-second');
        container.appendChild(personSecond);
        const message = document.createElement('p');
        message.classList.add('message-bubble', 'small', 'p-2', 'me-3', 'mb-1','text-white','bg-primary', 'rounded-3');

        const timeSpan = document.createElement('span');
        timeSpan.classList.add('d-block', 'message-time');

        const currentDate = new Date();
        const formattedDate = currentDate.toLocaleString('en-US', {
            weekday: 'short',
            hour: 'numeric',
            minute: 'numeric',
            hour12: true
        });

        timeSpan.textContent = formattedDate;

        const messageContent = document.createTextNode(data.message);
        message.appendChild(timeSpan);
        message.appendChild(messageContent);

        chatmessage.appendChild(message);

        personSecond.appendChild(message);
        const avatar = document.createElement('img');
        avatar.src = 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava4-bg.webp';
        avatar.alt = 'avatar 1';
        avatar.style.width = '45px';
        avatar.style.height = '100%';
        container.appendChild(avatar);
        startDiv.appendChild(container);


    }
    scroll();
}
privateMsgSocket.onclose = function (e) {
    console.log('socket closed')
}


const button = document.querySelector('#send-button')
button.addEventListener('click', (e) => {
    e.preventDefault()
    const messageInput = document.querySelector('#FormControlInput1');
    const message = messageInput.value;

    privateMsgSocket.send(JSON.stringify({
        'message': message,
        'userName_id': userName_id,
        'requestUser_id': requestUser_id
    }))
    messageInput.value = '';
})


function scroll(){
    const messageContainer = document.querySelector('.message-container');
    messageContainer.scrollTop =messageContainer.scrollHeight;
}

scroll();