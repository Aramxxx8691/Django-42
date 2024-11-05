$(document).ready(function () {
    // WebSocket for global chat
    const globalChatSocket = new WebSocket(
        // 'ws://' + window.location.host + '/ws/chat/global/'
        'ws://localhost:6352/ws/chat/global/'
    );

    globalChatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const message = '<b>' + data.user + ':</b> ' + data.message;
        $('#global-chat-log').append('<div>' + message + '</div>');
    };

    $('#chat-message-submit').click(function () {
        const messageInput = $('#chat-message-input');
        const message = messageInput.val();
    
        if (chatSocket.readyState === WebSocket.OPEN) {
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInput.val('');  // Clear input after sending
        } else {
            console.error('WebSocket is not open. Ready state is ' + chatSocket.readyState);
        }
    });

    // Handle private chatrooms
    const roomName = $('#room_name').text().trim();  // Use trim() to avoid any spaces
    if (roomName) {
        const privateChatSocket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
        );

        privateChatSocket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            const message = '<b>' + data.user + ':</b> ' + data.message;
            $('#chat-log').append('<div>' + message + '</div>');
        };

        $('#chat-message-submit').click(function () {
            const messageInput = $('#chat-message-input');
            const message = messageInput.val();
            privateChatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInput.val('');  // Clear input after sending
        });
    }

    // Redirect to private chatroom
    $('#enter-chatroom').on('click', function() {
        const selectedRoom = $('#existing-chatroom').val();
        if (selectedRoom) {
            window.location.href = '/en/chat/' + selectedRoom + '/';
        } else {
            console.log('No room selected');
        }
    });
});
