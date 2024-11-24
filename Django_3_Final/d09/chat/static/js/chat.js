$(document).ready(function () {
    const roomName = $('#room_name').text().trim();
    const chatLog = $('#chat-log');
    function scrollToBottom() {chatLog.scrollTop(chatLog[0].scrollHeight);}
    
    function connectPrivateChatSocket(roomName) {
        if (!roomName) return;
        const privateChatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');
        privateChatSocket.onopen = function () {console.log("Connected to private chat room:", roomName);};
        privateChatSocket.onerror = function (error) {console.error("Private chat WebSocket error:", error);};
        privateChatSocket.onclose = function () {
            console.log("Private chat WebSocket closed. Reconnecting...");
            setTimeout(() => connectPrivateChatSocket(roomName), 1000);
        };
        // Handle 'Send' button for private chat
        $('#chat-message-submit').click(function () {
            const messageInput = $('#chat-message-input');
            const message = messageInput.val();
            if (privateChatSocket.readyState === WebSocket.OPEN) {
                privateChatSocket.send(JSON.stringify({
                    'message': message
                }));
                messageInput.val('');
                scrollToBottom();
            }
            else {console.error('Private WebSocket is not open. Ready state is ' + privateChatSocket.readyState);}
        });
    }
    connectPrivateChatSocket(roomName);
    // Handle entering a chatroom from the home page
    $('#enter-chatroom').on('click', function() {
        const selectedRoom = $('#existing-chatroom').val();
        if (selectedRoom) {
            $.ajax({
                url: '/chat/' + selectedRoom + '/',
                type: 'GET',
                success: function(response) {
                    window.location.href = '/chat/' + selectedRoom + '/';
                },
                error: function() {
                    alert('Selected room does not exist.');
                }
            });
        }
        else {console.log('No room selected');}
    });
    // Add error message for "Create Chatroom" button click
    $('#create-chatroom-form').on('submit', function(e) {
        const roomName = $('#chatroom-name').val().trim();
        const errorMessageElement = $('#chatroom-error-message');
        // Reset error message if any
        errorMessageElement.text('').hide();
        // Check if room name contains a space
        if (roomName.includes(' ')) {
            // Prevent form submission
            e.preventDefault();
            // Show the error message with Bootstrap classes
            errorMessageElement.text('No spaces allowed in the chatroom name')
                .removeClass('alert-success')
                .addClass('alert alert-danger')
                .show();
        }
        else {console.log('Creating chatroom: ' + roomName);}
    });
});
