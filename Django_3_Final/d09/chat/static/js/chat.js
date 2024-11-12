$(document).ready(function () {
    const currentUser = $('#room_name').data('user-name');  // Get the current user's username

    // Global chat WebSocket connection
    function connectGlobalChatSocket() {
        const globalChatSocket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/global/'
        );

        globalChatSocket.onopen = function () {
            console.log("Connected to global chat WebSocket.");
        };

        globalChatSocket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            const message = '<b>' + data.user + ':</b> ' + data.message;
            $('#global-chat-log').append('<div>' + message + '</div>');
        };

        globalChatSocket.onerror = function (error) {
            console.error("WebSocket error:", error);
        };

        globalChatSocket.onclose = function () {
            console.log("Global chat WebSocket closed. Reconnecting...");
            setTimeout(connectGlobalChatSocket, 1000); // Retry connection after 1 second
        };

        $('#global-chat-message-submit').click(function () {
            const messageInput = $('#global-chat-message-input');
            const message = messageInput.val();

            if (globalChatSocket.readyState === WebSocket.OPEN) {
                globalChatSocket.send(JSON.stringify({
                    'message': message
                }));
                messageInput.val('');  // Clear input after sending
            } else {
                console.error('Global WebSocket is not open. Ready state is ' + globalChatSocket.readyState);
            }
        });
    }

    connectGlobalChatSocket();

    // Private chat WebSocket connection
    const roomName = $('#room_name').text().trim();

    function connectPrivateChatSocket(roomName) {
        if (!roomName) return;

        const privateChatSocket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
        );

        privateChatSocket.onopen = function () {
            console.log("Connected to private chat room:", roomName);
        };

        privateChatSocket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            const messageType = data.message_type;  // Check the message type

            if (messageType === 'join_message') {
                // Only show join message to users who are not the one joining
                if (data.user !== currentUser) {
                    $('#chat-log').append('<div class="text-muted"><em>' + data.message + '</em></div>');
                }
            } else if (messageType === 'user_message') {
                // Display regular user message
                const message = '<b>' + data.user + ':</b> ' + data.message;
                $('#chat-log').append('<div>' + message + '</div>');
            }
        };

        privateChatSocket.onerror = function (error) {
            console.error("Private chat WebSocket error:", error);
        };

        privateChatSocket.onclose = function () {
            console.log("Private chat WebSocket closed. Reconnecting...");
            setTimeout(() => connectPrivateChatSocket(roomName), 1000);
        };

        $('#chat-message-submit').click(function () {
            const messageInput = $('#chat-message-input');
            const message = messageInput.val();

            if (privateChatSocket.readyState === WebSocket.OPEN) {
                privateChatSocket.send(JSON.stringify({
                    'message': message
                }));
                messageInput.val('');  // Clear input after sending
            } else {
                console.error('Private WebSocket is not open. Ready state is ' + privateChatSocket.readyState);
            }
        });
    }

    connectPrivateChatSocket(roomName);

    // When a user enters a new room
    $('#enter-chatroom').on('click', function() {
        const selectedRoom = $('#existing-chatroom').val();
        if (selectedRoom) {
            window.location.href = '/en/chat/' + selectedRoom + '/';
        } else {
            console.log('No room selected');
        }
    });
});
