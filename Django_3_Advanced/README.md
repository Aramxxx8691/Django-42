# Advanced
## Project Overview
The Advanced project consists of a series of exercises designed to build a comprehensive Django web application. Each exercise introduces new concepts and features for the application, focusing on user interaction, article management, authentication, and testing.

## Exercise 00: Model Building - Generic Class
### Objective
Create and structure models to handle articles and user interactions with these articles.

### Instructions
1. Implement the `Article` and `UserFavouriteArticle` models with the specified fields and relationships.
2. Override the `__str__` method in each model to return meaningful identifiers.
3. Use Django’s generic views (excluding direct inheritance from `View`) to implement:
- `Articles`: Display an HTML table of all articles.
- `Home`: Redirects to the Articles page.
- `Login`: A POST form for user login, with error messages.
4. Populate the database with sample data (at least five articles from three users).

### Learning Points
- Basic model structure and relationships in Django.
- Use of generic views for CRUD operations.
- Handling user authentication and redirects in Django.

### Example Usage
When a user navigates to the homepage, they should be redirected to the Articles page where they can view article titles and authors in a tabular format.

### Explanation
This exercise introduces basic Django model creation and the use of generic views for standard functionalities without custom CSS.

## Exercise 01: Generic Class Again
### Objective
Extend functionality to allow logged-in users to interact with articles, view details, and manage favorite articles.

### Instructions
1. Implement Publications to show articles for the logged-in user.
2. Add Detail view to show each article’s content.
3. Create Logout link and a Favourites page for users’ favorite articles.

### Learning Points
- Expanding on generic views to customize user experiences.
- Authentication-based access to specific content.

### Example Usage
Authenticated users can navigate to the Publications page to view their articles and mark certain articles as favorites.

### Explanation
In this exercise, we expand generic views for user-specific content and session-based access control.

## Exercise 02: Generic Class - CreateView
### Objective
Introduce user registration and content creation functionalities.

### Instructions
1. Implement a Register form allowing new users to sign up.
2. Create a Publish form for logged-in users to submit new articles.
3. Add functionality to Add to Favourite directly from an article’s detail view.

### Learning Points
- Use of `CreateView` to handle new data entries.
- Managing foreign key fields in forms for relational integrity.

### Example Usage
Logged-in users can create articles via the Publish form, and registered users can add articles to their favorites.

### Explanation
This exercise introduces user-generated content and registration functionalities using Django’s `CreateView`.

## Exercise 03: Template Tags and Filters
### Objective
Enhance the user interface with a universal navigation menu and dynamic content filtering.

### Instructions
1. Add a menu accessible from every page of the site.
2. Use template tags and filters to:
- Limit synopsis display to 20 characters.
- Sort articles by date.
- Show the time since publication.

### Learning Points
- Customizing templates with Django template tags and filters.
- Creating a dynamic menu based on user login state.

### Example Usage
The menu changes based on the user’s login status, providing links to appropriate views.

### Explanation
This exercise enhances user experience by introducing template logic and conditional display elements.

## Exercise 04: Bootstrap
### Objective
Apply Bootstrap styling to improve the application’s user interface.

### Instructions
Use Bootstrap to style the menu and other key elements as per the provided layout guide.


### Learning Points
- Integrating Bootstrap with Django templates for responsive design.
- Enhancing user experience through consistent styling.

### Example Usage
Navigate through the site to see Bootstrap-styled menus and forms.

### Explanation
This exercise focuses on front-end styling using Bootstrap to make the app visually appealing and user-friendly.

## Exercise 05: Internationalization
### Objective
Enable multilingual support for specific sections of the site.

### Instructions
1. Translate all content in the Articles functionality and the menu.
2. Create a language switcher on the page that toggles languages based on URL prefix (e.g., `en`, `fr`).

### Learning Points
- Configuring multilingual support in Django.
- Using URL prefixes for dynamic language switching.

### Example Usage
A user can switch languages by clicking on the language toggle, which updates the page content.

### Explanation
This exercise makes the site accessible to a broader audience by adding multilingual support.

## Exercise 06: Testing
### Objective
Implement test cases to validate the app's behavior, including user permissions and favorites functionality.

### Instructions
1. Create tests to verify view access based on user authentication.
2. Ensure users cannot add duplicate favorites or access the registration form once logged in.

### Learning Points
- Writing effective tests for user permissions and data integrity.
- Using Django’s testing framework to validate application behavior.

### Example Usage
Run the test suite to confirm all functionality works as expected without error.

### Explanation
This final exercise ensures application reliability through comprehensive testing of user interactions and data constraints.

## Helper Commands
The following Django commands assist with creating and compiling translation files for different languages:

- Create translation files: Generates .po files for the specified language code.

```
django-admin makemessages -l hy
django-admin makemessages -l ru
django-admin makemessages -l fr
```

  - Replace `-l <language code>` with the language code you need. For example:
   - `-l hy` for Armenian
   - `-l ru` for Russian
   - `-l fr` for French
- Compile translation files: Compiles all `.po` files into binary `.mo` files, making translations ready for use in the project.

```
django-admin compilemessages
```

Make sure to run these commands whenever there are updates to translatable text in the project templates or code. This ensures your translations are up-to-date and available in the application.
