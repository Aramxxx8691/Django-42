# Final

## Exercise 00: AJAX my formulah!
### Objective:
In this exercise, we create a login system that communicates with the server using AJAX. The page will display two behaviors based on the user's authentication state:
- If the user is not logged in, a standard login form (username, password) will be displayed. The form will submit via AJAX (POST) to validate the user's credentials.
- If the user is logged in, the page will display a message showing the logged-in user and a logout button, both of which will also communicate with the server via AJAX (POST) to log the user out.

### Instructions:
1. Create a Django project: Name it `d09`.
2. Create an application named `account`.
3. Design the page:
- The URL `127.0.0.1:8000/account` will display the connection form or logged-in user message depending on the user's authentication state.
- On a successful login, the form should disappear and the logged-in user information should be displayed without refreshing the page.
- If the user clicks the logout button, they should be logged out and the page should revert to displaying the login form, again without refreshing.
4. Form validation:
- Use AJAX to submit the login form and handle errors or success responses.
- On success, remove the login form and display the "Logged as <username>" text with a logout button.
- On logout, the "Logged as" text and logout button should disappear, reverting to the login form.
5. Error Handling: Display validation errors (if any) in the form, and ensure no page refresh occurs.
6. Use Bootstrap for styling.

## Tools/Technologies Used:
- Django
- AJAX (jQuery)
- Bootstrap
- Django's AuthenticationForm

## Exercise 01: Basic chat
### Objective:
Create a simple chat application using Websockets to handle real-time communication between users. The system will include multiple chatrooms, with users able to post messages that are visible to all users in the chatroom.

### Instructions:
1. Create an application named `chat`.
2. Database Model:
- Define a model to store chatroom names.
- The database should contain at least 3 different chatrooms.
3. Frontend:
- Use only jQuery as the frontend library.
- Use Websockets for communication between the server and the clients.
4. Chat Functionality:
- Display a list of available chatrooms on the main page.
- Each chatroom link should lead to its own chat page.
- On the chat page:
  - The name of the chatroom should be displayed.
  - Users can post messages, which will be visible to all connected users.
  - Messages must appear in ascending order at the bottom of the chatroom.
  - When a user joins, display a message indicating the user has joined the chat (e.g., "<username> has joined the chat").
5. User Authentication:
- Only authenticated users should be able to access the chatrooms.
6. WebSocket Communication:
- Messages must be sent and received via Websockets without using AJAX.

## Exercise 02: History
### Objective:
Enhance the chat from Exercise 01 by adding message history. When a new user joins a chatroom, they should see the last three messages posted in that chatroom.

### Instructions:
1. Display Message History:
- When a user joins the chatroom, they should see the last 3 messages posted.
- These messages should be displayed in reverse order (top-down, oldest to newest).
2. WebSocket Communication:
- Continue using Websockets for message broadcasting and reception.
- Ensure that new messages are added below the previous messages without replacing them.

## Exercise 03: Userlist
### Objective:
Add a connected user list to the chatroom. The user list should update automatically when a user joins or leaves the chatroom.

### Instructions:
1. User List Display:
- Show a list of connected users, which should be displayed separately from the message list.
2. Dynamic Updates:
- When a user joins the chatroom, their name should appear in the connected users list.
- When a user leaves the chatroom, their name should be removed from the list.
- Display a message ("<username> has left the chat") when a user leaves.
3. Real-time Updates:
- Use Websockets to dynamically update the user list and message list in real-time.

## Exercise 04: Scroll
### Objective:
Improve the chat interface by adding scrolling functionality to the message container. If the number of messages exceeds the container's height, older messages should be hidden, and a scrollbar should appear.

### Instructions:
1. Fixed Container for Messages:
- Set a fixed height for the message container.
2. Message Overflow:
- If the number of messages exceeds the container's height, messages should scroll, with the newest messages appearing at the bottom.
3. Scroll Behavior:
- When the message container overflows, the scrollbar should appear on the side, and older messages should be pushed up, disappearing from view.