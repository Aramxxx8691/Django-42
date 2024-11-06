# Sesions
## Project Overview
This project is a web application that allows users to share and vote on "Life Pro Tips." The application is built using Django and incorporates session management, user authentication, a tips model, and a permission system based on user reputation. Each exercise focuses on enhancing functionality or adding permissions to make the application more robust and engaging.

## Exercise 00: Anonymous Sessions
### Objective
Implement anonymous sessions with temporary usernames for users visiting the site.

### Instructions
1. Create a predefined list of usernames in `settings.py`.
2. Use Django’s session framework to assign a random username to each anonymous user.
3. Set the username to expire after 42 seconds and regenerate a new one.
4. Ensure that the username persists during the session and is displayed in the `<nav>` section of the homepage.
5. Implement JavaScript or AJAX to update the displayed username in real time without requiring a page reload.

### Learning Points
- Understanding Django’s session management.
- Using session data to store and retrieve user-specific information.
- Using JavaScript and AJAX for real-time page updates.

### Example Usage
When an anonymous user visits the homepage, they should be greeted with “Hello user!” followed by a temporary username that expires every 42 seconds.

### Explanation
- The primary goal of this exercise is to familiarize yourself with managing sessions in Django. By using session-based temporary usernames, we can simulate user identification even for users who aren't logged in.
- The JavaScript will handle the dynamic update of the username in the header, while the Django session will store the generated username and update it at regular intervals, ensuring the session persists during the visit.

## Exercise 01: User Creation
### Objective
Create a user registration and authentication system.

### Instructions
1. Create a registration form with fields for username, password, and password confirmation.
2. Validate that the username is unique and that the password confirmation matches the entered password.
3. Upon successful registration, automatically log the user in and redirect them to the homepage.
4. Create a login form with fields for username and password to authenticate users.
5. Add a "Log Out" link to the navigation bar, which logs out users and redirects to the homepage.
6. Ensure logged-in users cannot access the registration or login pages, redirecting them back to the homepage if they try.

### Learning Points
- Working with Django’s user authentication system.
- Handling form validation for user registration and login.
- Using Django’s authentication views for managing login/logout functionality.
- Understanding form handling in Django.

### Example Usage
When a user registers, they should be redirected to the homepage and logged in automatically. If a user tries to access the login or registration page while logged in, they should be redirected to the homepage.

### Explanation
- This exercise will guide you through building basic user authentication using Django’s built-in functionality.
- The key challenge here is ensuring that the registration and login systems work seamlessly, with the added feature of preventing logged-in users from accessing the login/registration pages.

## Exercise 02: Our Tips!
### Objective
Implement the core feature for creating and displaying tips.

### Instructions
1. Define a `Tip` model with fields for content, author, and the date the tip was created.
2. Create a form that allows logged-in users to submit tips.
3. Display all submitted tips on the homepage, showing the content, author, and creation date.
4. Make sure that only logged-in users can submit tips, and display a message if an anonymous user tries to submit a tip.

### Learning Points
- Working with Django models to create and store data.
- Understanding how to create forms using Django’s `ModelForm`.
- Using Django’s template system to display model data on the frontend.

### Example Usage
A logged-in user submits a tip that appears immediately on the homepage with the tip's content and the author's name.

### Explanation
- In this exercise, you will create a model to represent a tip and use Django’s `ModelForm` to handle user submissions. Displaying the tips on the homepage will require using Django’s template rendering system to loop through and display all tips from the database.

## Exercise 03: Votes
### Objective
Add voting functionality to tips and allow users to delete their tips.

### Instructions
1. Add upvote and downvote buttons to each tip, visible only to logged-in users.
2. Store the votes in a model that tracks which users voted and the type of vote (upvote or downvote).
3. Display the number of upvotes and downvotes for each tip.
4. Prevent users from voting multiple times on the same tip.
5. Allow users to delete their own tips.

### Learning Points
- Creating relationships between models using Django’s `ManyToManyField`.
- Implementing voting logic to track and update votes.
- Understanding how to prevent duplicate actions (e.g., duplicate voting) through validation.

### Example Usage
A user can upvote or downvote a tip. After voting, the tip's vote count should update, and the user can only vote once per tip.

### Explanation
- This exercise introduces the concept of tracking votes on each tip and updating the display based on user interactions. The `ManyToManyField` will allow you to track which users have voted on which tips, while additional validation will prevent multiple votes by the same user on the same tip.

## Exercise 04: Primary Use of Authorizations
### Objective
Restrict tip deletion permissions to specific users.

### Instructions
1. Modify the view logic to allow only the author of a tip to delete it.
2. Use Django’s admin interface to manage the permissions for deleting tips.
3. Ensure that other users (not the authors) cannot delete tips.

### Learning Points
- Understanding how to implement custom permissions in Django.
- Using Django’s admin interface to manage model-level permissions.
- Implementing authorization checks in views.

### Example Usage
When a user tries to delete a tip that they didn’t create, they should see an error or be redirected without the option to delete it.

### Explanation
- This exercise focuses on restricting actions to users with the correct permissions. By using Django’s built-in permission system, we can ensure that only the tip’s author is allowed to delete it.

## Exercise 05: Personalized Authorization
### Objective
Restrict downvoting functionality to authorized users.

### Instructions
1. Create a custom permission for downvoting functionality.
2. Ensure that only users with the permission can downvote tips.
3. Allow tip authors to downvote their own tips, even if they don’t have the general downvote permission.

### Learning Points
- Creating custom permissions in Django.
- Using permissions to control access to specific actions.
- Understanding how to apply custom permissions to specific views.

### Example Usage
A user without the downvote permission should not see the downvote button, except for their own tips where they should still be able to downvote.

### Explanation
- Custom permissions give you the flexibility to control which users can perform certain actions. In this case, we’ll create a permission to restrict who can downvote tips, but allow the authors of tips to downvote their own tips regardless of the general permission.

## Exercise 06: Automation and Reputation
### Objective
Implement a reputation system that determines user permissions based on their engagement.

### Instructions
1. Create a custom user model with a reputation score field.
2. Define rules for modifying the reputation score based on upvotes, downvotes, and tip deletions.
3. Set authorization thresholds based on the reputation score (e.g., 15 points for downvoting and 30 points for deleting tips).
4. Display the user’s reputation score next to their name on the homepage.

### Learning Points
- Creating custom user models in Django.
- Implementing a reputation-based permission system.
- Using signals to update user reputation based on actions (e.g., upvotes and downvotes).

### Example Usage
A user with 20 reputation points will be able to downvote tips. Once they reach 30 points, they can also delete tips.

### Explanation
- This exercise focuses on implementing a reputation system that tracks user activity and determines their privileges based on their engagement in the platform. The system uses signals to automatically adjust a user's reputation score based on interactions with tips (e.g., receiving upvotes or downvotes).

## Additional Notes
- `Testing and Validation`: Implement unit tests for each view and model change to verify functionality.
- `Real-time Updates`: Consider using WebSockets or AJAX for real-time updates on the homepage, especially for username updates, votes, and reputation scores.
