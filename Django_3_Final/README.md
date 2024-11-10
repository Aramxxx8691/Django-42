Exercice 00: AjAX my formulah!
Create a new project named d09. In this project, create an application named account.
The goal of this exercise is to design a connection/disconnection system communicating only thanks to AJAX.
In this application , you will implement the 127.0.0.1:8000/account URL that must lead to a page that can have two diffrent behaviors depending on the context:
• The user is not connected: the page must display a standard connection form (login, password). The thing is the communication with the server must only use AJAX and must be a POST type to get connected.
If the form is not valid, the error(s) must appear on the page.
Of the form is valid, it must disapear and adopt a new behavior.
This, of course, without the page being refreshed.
• The user is connected already: the page must display the following text: "Logged as <user>", <user> being replaced by the name used by the user to get connected as well as Logout button allowing disconnection.
This button must communicate with the server via AJAX and the ’POST’ method.
Once logged out, the text and button must not show on the page anymore and the latter must adopt the other behavior.
The page must never have been refreshed.
If the page is ’manually’ refreshed, it must return to the behavior it had before refreshing (that does not include the error displaying).
You can use bootstrap.
AuthenticationForm, for free!

Exercice 01: Basic chat
Create an application named ’chat’.
In this application, you must create a page displaying 3 links. Each of them must lead to a different ’chatrooms’.
The names of these rooms must be in database. You must create a suitable model.
Each of these links must lead to another page containing a standard functional chat.
Each chat must have the following specification:
• It must use ’jquery’ as sole frontend library as well as the Websockets to communicate with the server.(no AJAX)
• It’s only available to connected users.
• The name of the chat must appear somewhere.
• Several users must be able to connect (just in case...).
• A user can post a message (you had guessed, right?).
• A message sent by a user must be visible by all the users who have joined the chatroom (everyone knows what a chatroom is, right? Haven’t you read that preamble?).
• Messages must appear in the bottom and be displayed in ascending order (that one’s for you, by the heater, right.), along with the name of the user that posted them.
• Messages must not disappear. A message must not replace a previous one. The messages order must not change.
• When a user joins the chatroom, the message ’<username> has joined the chat’ must appear for all users to see, including the one who just joined. <username> is replaced by said user’s name of course.

Exercice 02: History
In this exercise, you will improve your chat adding a message history to it.
When a new user joins the chatroom, they must see the last three messages that have been posted on this chatroom, top down, oldest to newest.
Once again, you can only use JQuery as frontend libraries and Websockets to communicate with the server.

Exercice 03: Userlist
In this exercise, you will improve your chat again adding a connected userlist, this time. AND it will update by itself.
When the user joins the chatroom, he must be able to access the list of connected users (and he must appear in the list).
This userlist must be clearly set aside the messages list (other <div> or other html container).
When a user joins a chatroom, their name must appear in the list, along with other connected users.
When a user leaves the chatroom, their name must disappear from the list of connected users and the message ’<username> has left the chat’ must appear after the posted messages. (<username> will be the name of the user who just left)
Once again, you can only use JQuery as frontend libraries and Websockets to communicate with the server.
Before anything, try to build a functional logic. We’re not looking
for optimization... yet.

Exercise 04: Scroll
Make your chat presentable setting your message list in a fixed size container. If the number of messages exceed the container, they must disappear on top and a scroll bar must appear on the side.

