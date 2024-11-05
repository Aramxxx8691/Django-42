# Base
## - ex00: Static Page with Django
In this exercise, you will create your first static page using Django. The goal is to set up a Django project and application, and create a static page that displays information about Markdown syntax.

### Objective
- `Create a Virtual Environment`: Set up a Python virtual environment.
- `Install Django`: Install Django within the virtual environment.
- `Create a Django Project`: Start a new Django project named `d05`.
- `Create a Django Application`: Start an application named `ex00` within the project.
- `Create a Static Page`: Develop a static page at the URL `/ex00` with the title "Ex00: Markdown Cheatsheet" and display information about Markdown syntax.

### Instructions
1. Setup Virtual Environment:
- Create a Python virtual environment with the name `venv`.
- Install Django and create a `requirements.txt` file to list project dependencies.
2. Start Django Project and Application:
- Start a new Django project named `d05`.
- Within the `d05` project, create a new Django application named ex00.
3. Create the Static Page:
- Create a template named index.html inside the `ex00` application directory.
- This page should be accessible at `/ex00` and should contain information about the Markdown syntax.

### Example Shell Script
Here's a brief explanation of the shell script used to set up your Django environment and project:
1. Virtual Environment:
- Creates and activates a virtual environment named `venv`.
2. Install Dependencies:
- Installs Django and other dependencies listed in `requirements.txt`.
3. Create Django Project and Applications:
- Starts a new Django project named `d05` and applications named `ex00`, `ex01`, `ex02`, and `ex03`.
4. Check and Setup:
- If the Django project directory (`d05`) already exists, it will notify you and change to that directory.
- Otherwise, it creates the project and applications, and activates the shell.

`Note`: Ensure that your virtual environment is activated. If the virtual environment prompt (`venv`) is not visible, you can manually activate it with:
```
source venv/bin/activate
```

### Example Usage
1. Run Django Server:
- Start the Django development server with:
```
python manage.py runserver
```
2. Access the Page:
- Open your browser and go to `http://localhost:8000/ex00` to view the static page titled "Ex00: Markdown Cheatsheet."

### Django Configuration
1. Project Configuration:
- `d05/settings.py`: Ensure that your INSTALLED_APPS includes '`ex00`', '`ex01`', '`ex02`', and '`ex03`'.
2. Application Configuration:
- `ex00/urls.py`: Define the URL pattern to serve the static page:
```
from django.urls import path
from . import views 

urlpatterns = [
    path('ex00/', views.ex00),
]
```
- `ex00/views.py`: Create a view to render the static page:
```
from django.shortcuts import render

# Create your views here.
def ex00(request):
    return render(request, 'index.html')
```
- `ex00/templates/index.html`: Create the template for the static page with Markdown syntax information:

By completing this exercise, you will set up a Django project and application, create a static page, and understand how to configure URLs and views in Django.

## - ex01: Django Static Pages
In this exercise, you will extend the Django project by creating multiple static pages in the ex01 application. Each page will be styled and organized using a base template to follow Django’s DRY (Don't Repeat Yourself) principle.

### Objective
- `Create Static Pages`: Develop three distinct pages within the `ex01` application.
- `Use Templates`: Implement a base template to avoid repeating HTML code.
- `Include Styles`: Apply different CSS styles to the pages.

### Instructions
1. Setup Views and URLs:
- URLs Configuration: Define URL patterns for the pages in `ex01/urls.py`.
- Views Configuration: Create views to render the pages in `ex01/views.py`.
2. Create Templates:
- `base.html`: A base template with blocks for content, styles, and titles.
- `nav.html`: A navigation bar template to include on each page.
- `Page Templates`: Create templates for the three pages using the base template.
3. CSS Files:
- `style1.css`: Define text color as blue.
- `style2.css`: Define text color as red.
- Use `style1.css` for most pages, and `style2.css` for the "Template engine" page.
4. Static Files Collection:
- Ensure you run `collectstatic` during evaluation to collect static files.

By completing this exercise, you will understand how to set up multiple static pages using Django, leverage templates for common structures, and apply different styles to your pages.

## - ex02: Form Submission and Input History
n this exercise, you will create a Django application (ex02) that includes a form and a history log. The form will allow users to submit text entries, which will be stored in both a log file and displayed on the page.

### Objective
- `Create a Form`: Use Django’s form class to create a text input form.
- `Handle Submissions`: Process form submissions and save entries to a log file.
- `Display History`: Show a history of submissions on the page.
- `Persist Data`: Ensure that data persists between server restarts.

### Instructions
1. Setup Form and Views:
- `Form Creation`: Use django.forms.Form to create a form with a text field.
- `Views Configuration`: Implement views to handle form submissions and display history.
2. Configure Logging:
- `Log File`: Define the path to the log file in settings.py.
- `History Management`: Read from and write to the log file.
3. Create Template:
- `Template Layout`: Design a template with a form and a section to display the submission history.

### Django Configuration
- `d05/settings.py`: Add a setting for the log file path:
```
HISTORY_LOG_FILE = os.path.join(BASE_DIR, 'ex02', 'history.log')
```
- `ex02/forms.py`: Define a form with a single text input field:
- Define the form using Django’s `forms.Form` class.
- Implement views to handle form submissions and display the history.
- Create a template for rendering the form and displaying the history.

### Forms in Django
Django's forms.Form class simplifies the process of handling forms. Here's a brief overview:
- `Form Class`: Define form fields and validation logic in a class that inherits from forms.Form.
- `Field Types`: Django provides various field types like CharField, IntegerField, EmailField, etc.
- `Validation`: Automatically handles validation based on field types and custom validation methods.

### Migrations and Migrate
Migrations are Django's way of propagating changes made to your models into the database schema. Here’s a brief explanation:
- `Migrations`: Track changes to your models and create SQL scripts to apply these changes to the database.
- `migrate Command`: Applies and un-applies migrations to the database.
Common Commands:
- `python manage.py makemigrations`: Creates new migrations based on the changes detected in models.
- `python manage.py migrate`: Applies the migrations to the database.

`Note`: In this exercise, you do not need to create migrations for the `ex02` application because it does not involve any database models.

By completing this exercise, you will:
- Learn how to create and handle forms in Django.
- Understand how to manage and persist data using files.
- Gain experience in rendering dynamic content in templates.

## - ex03: Dynamic Color Shades Table

Create a final application `ex03`. Display a page containing a 4 columns x 51 lines table (one line will be dedicated to the column’s name).

### Objective
- `Create a Table`: Display a table with 4 columns and 51 lines.
- `Dynamic Shades`: Generate different color shades dynamically in the view.
- `CSS Styling`: Style the table cells with specific dimensions and background colors.

### Instructions
1. Setup Views and URLs:
- `URLs Configuration`: Define the URL pattern for the table in `ex03/urls.py`.
- `Views Configuration`: Create a view to generate color shades and render the table.
2. Generate Color Shades:
- `Color Calculation`: Compute 50 shades for each of the four colors (noir, rouge, bleu, vert).
- `Table Rows`: Dynamically construct the table rows and header.
3. Create Template:
- `HTML Layout`: Design a template to display the table with the dynamically generated shades.

### Django Configuration
- `d05/settings.py`: Ensure that your `INSTALLED_APPS` includes `ex00`, `ex01`, `ex02`, and `ex03`.
- `View Definition`: Implement the view to generate color shades and render the table.
- `Template Creation`: Create a template to display the dynamically generated table.

### Table Structure and Styling
- `Table Columns`: Each column will have a different color: noir, rouge, bleu, and vert.
- `Cell Dimensions`: Height: 40 pixels, Width: 80 pixels.
- `Background Colors`: Each cell will have a shade of the column’s color.
- `HTML Elements`:
  - `<th>` tags for column names.
  - `<tr>` tags for each table row.
  - `<td>` tags for each cell.

By completing this exercise, you will:

- Learn how to generate dynamic content in Django views.
- Understand how to create and style tables in HTML.
- Gain experience in using Django templates to render dynamic data.
