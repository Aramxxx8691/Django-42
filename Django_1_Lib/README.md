# Lib
## - ex00: Geohashing
In this exercise, you will create a Python script named geohashing.py that calculates a geohash based on latitude, longitude, and a date. The program will include input validation and error handling.
### Objectives
- `Create a Script`: Develop geohashing.py to compute a geohash.
- `Handle Command-Line Arguments`: Accept latitude, longitude, and date as arguments.
- `Validate Inputs`: Ensure latitude, longitude, and date are valid.
- `Error Handling`: Display appropriate error messages for invalid inputs.
- `Output Geohash`: Simulate the geohashing process with a placeholder function.
### Instructions
1. Script Creation:
- Write a script named `geohashing.py`.
- Use the sys module to handle command-line inputs and `antigravity` as a placeholder for geohashing.
2. Input Parameters:
- `Latitude`: Float value between -90 and 90.
- `Longitude`: Float value between -180 and 180.
- `Date`: String in `YYYY-MM-DD` format.
3. Validation:
- `Date`: Validate the format and ensure the date is correct.
- `Latitude`: Check that latitude is within the valid range.
- `Longitude`: Check that longitude is within the valid range.
4. Error Handling:
- Handle incorrect number of arguments.
- Validate latitude, longitude, and date. Provide relevant error messages.
5. Geohashing Calculation:
- Simulate geohashing with a placeholder function.
6. Example Usage:
```
python geohashing.py 37.7749 -122.4194 2024-07-01
```
### Learning Points
- `Command-Line Arguments`: Understanding how to handle command-line inputs in Python.
- `Input Validation`: Ensuring inputs are valid and handling invalid cases.
- `Error Management`: Providing clear and informative error messages.
- `Geohashing Simulation`: Learning the basics of geohashing and simulating its process.

By completing this exercise, you will gain experience in handling command-line arguments, input validation, and error management in Python.


## - ex01: Path Library Setup and Usage
This exercise involves creating a bash script to install the `path.py` library and a Python program that uses this library to perform file operations.
### Objective
- `Shell Script Creation`: Develop a bash script to install the path.py library.
- `Python Program Development`: Create a Python program to use the installed library for file operations.
- `Error Handling and Logging`: Manage installation errors and log the process.
### Instructions
1. Shell Script:
- `Name`: The script must have a `.sh` extension.
- `Pip Version`: Display the pip version used.
- `Library Installation`:
- - Install the `path.py` development version from its GitHub repository.
- - Install the library in a folder named `local_lib` within the repository.
- - If the library already exists, replace it.
- `Logging`: Write installation logs to a `.log` file.
- `Execution`: Run the Python program if the installation is successful.
2. Python Program:
- `Import Path Module`: Import the `path` module from the `local_lib` folder.
- `File Operations`:
- - Create a folder and a file within this folder.
- - Write content to the file and read/display the content.
- `Constraints`: Follow specific rules for the Python script.
### Example Shell Script Usage
- `Display pip version`: Shows which version of pip is being used.
- `Create and activate virtual environment`: Sets up an isolated environment for package installation.
- `Install path.py`: Downloads and installs the path.py library from its GitHub repository into a specified folder.
- `Log installation process`: Records the installation process in a log file for later review.
Execute Python program: Runs a Python program if the library installation is successful.
### Learning Points
- `Shell Scripting`: Learn to create and execute shell scripts for setup and installation.
- `Python Imports`: Understand how to import modules from specific locations.
- `File Operations`: Gain experience in creating directories, writing to files, and reading from files.
- `Error Handling`: Learn to handle installation errors and log them appropriately.
By completing this exercise, you will gain experience in shell scripting, Python imports, file operations, and error management.

## - ex02: Wikipedia Request Tool
Create a Python program named `request_wikipedia.py` that takes a search string as a parameter and queries the Wikipedia API to fetch the relevant page content.
### Objective
- `Create a Python script`: Develop a `request_wikipedia.py` program to query the Wikipedia API.
- `File Handling`: Write the search result to a file named `name_of_the_search.wiki`.
- `Error Handling`: Ensure proper error handling for invalid inputs and request failures.
### Instructions
1. API Request:
- Accept a search string as a parameter.
- Query the Wikipedia API (English or French) to fetch the page content.
2. Result Handling:
- Write the fetched content to a file named `name_of_the_search.wiki` without spaces.
- Ensure the result is written even if the search string is misspelled.
3. Error Handling:
- Display relevant error messages for invalid inputs, request failures, or any other issues.
- Do not create a file in case of any errors.
4. Requirements:
- Include a requirements.txt file listing the necessary libraries (dewiki, requests).
### Example Usage
To run the script and fetch Wikipedia content, use the following command:
```
python3 request_wikipedia.py "Python programming"
```

This command will fetch the Wikipedia page for "Python programming" and write the content to a file named `Python_programming.wiki`.
### Learning Points
- `API Interaction`: Learn to interact with the Wikipedia API and handle JSON responses.
- `File Handling`: Gain experience in writing fetched content to a file with a specific naming convention.
- `Error Handling`: Understand how to manage errors and provide feedback in a script.

By completing this exercise, you will gain experience in API interaction, file handling, and error management in Python.

## - ex03: Roads to Philosophy
Create a Python program named `roads_to_philosophy.py` that takes a Wikipedia search term as a parameter and follows the first link in each article's introduction to test the "roads to philosophy" phenomenon.

### Objective
- `Create a Python script`: Develop a `roads_to_philosophy.py` program to follow Wikipedia links to the Philosophy page.
- `HTML Parsing`: Use the BeautifulSoup library to parse Wikipedia HTML pages and find the first valid link in the introduction.
- `Error Handling`: Manage errors such as invalid inputs, dead ends, and infinite loops gracefully.
### Instructions
1. Initial Request:
- Accept a search term as a parameter.
- Request the corresponding English Wikipedia page URL.
2. HTML Parsing:
- Use BeautifulSoup to parse the HTML page.
- Find any redirections and the main title of the page.
- Identify the first link in the introduction that leads to another Wikipedia article.
3. Recursion:
- Repeat the process with the new link until:
- - The link leads to the Philosophy page.
- - The page has no valid links (dead end).
- - The page leads to an already visited article (infinite loop).
4. Output:
- Print the visited articles and the total count if the Philosophy page is reached.
- Print appropriate messages for dead ends and infinite loops.
### Example Usage
To run the script and follow links from the specified Wikipedia page, use the following command:
```
python3 roads_to_philosophy.py "Python (programming language)"
```

This command will start from the "Python (programming language)" Wikipedia page and follow links until it reaches the Philosophy page, hits a dead end, or encounters an infinite loop.
### Learning Points
- `Web Scraping`: Learn to scrape and parse HTML content using the BeautifulSoup library.
- `Recursion`: Understand recursive function calls to repeatedly follow links.
- `Error Handling`: Gain experience in managing various error scenarios and providing user feedback.

By completing this exercise, you will gain experience in web scraping, recursion, and error handling in Python.

## - ex04: Django Setup Script
Create a script to set up a Django development environment with PostgreSQL support.

### Objective
- `Create a requirements.txt file`: Include the latest stable versions of Django and psycopg2.
- `Create a Shell Script`: Develop a script to create and configure a virtual environment for Django.
### Instructions
1. requirements.txt:
- Include the latest stable versions of Django and psycopg2.
```
Django>=3.2.3,<3.3
psycopg2-binary
```
2. Shell Script:
- The script should be named with a `.sh` extension.
- Create a Python 3 virtual environment named `venv`.
- Install the requirements from the `requirements.txt` file in the virtual environment.
- Activate the virtual environment upon completion.
### Example Usage
To run the script and set up the Django environment, use the following command:
```
./my_script.sh
```

This command will create the `venv` virtual environment, install the required packages, and activate the virtual environment.
### Learning Points
- `Virtual Environment`: Learn to create and manage Python virtual environments.
- `Package Management`: Understand how to specify and install packages using a requirements.txt file.
- `Shell Scripting`: Gain experience in writing and executing shell scripts to automate setup tasks.
By completing this exercise, you will be prepared for your Django framework training with a properly configured development environment.

## - ex05: Hello World with Django
In this exercise, you will create your first web page using Django that displays "Hello World!" in the browser at `http://localhost:8000/helloworld`.
### Objective
- `Follow and Adapt the Django Tutorial`: Set up a Django project and create a web page that displays "Hello World!".
### Instructions
1. Set up the Django Project:
- Create and activate a virtual environment.
- Install Django using the requirements.txt file.
2. Create the Django Project and Application:
- Use django-admin to start a new Django project named Django.
- Create a new application within the project named my_app.
3. Configure Django Settings:
- Add my_app to the INSTALLED_APPS list in settings.py.
- Update urls.py to include the URLs from my_app.
4. Define the Application URLs and Views:
- Create a urls.py file in my_app to define the URL pattern for helloworld.
- Create a view in views.py to render the helloworld template.
5. Create the Template:
- Create a templates directory within my_app.
- Add an HTML file helloworld.html in the templates directory that displays "Hello World!".
### Example Usage
`Important`: Ensure you run this inside the opened virtual environment created by our script. If you see `(venv)` in your terminal prompt, you are in the virtual environment. If not, or if you closed the terminal, activate the environment manually.
1. Activate the Virtual Environment:
```
source venv/bin/activate
```
2. Start the Django Development Server:
```
python3 manage.py runserver
```
3. Visit the Web Page:
- Open your browser and go to `http://localhost:8000/helloworld` to see the "Hello World!" message.
### Example Shell Script
The shell script provided performs the following actions:
1. Check Virtual Environment:
```
if [ -n "$VIRTUAL_ENV" ]; then
```
Ensures the script is running inside an activated virtual environment. If not, it exits with an error.
2. Create Django Project:
```
if [ -d "Django" ]; then
    echo "📁 Django project already exists."
else
    django-admin startproject Django
    cd Django
    django-admin startapp my_app
    echo "📁 Django project created."
fi
```
Checks if the Django project directory (`Django`) already exists. If not, it creates a new Django project and application. It also changes into the project directory and initializes the application.
3. Activate Virtual Environment:
```
exec "$SHELL"
```
Activates the virtual environment for the current shell session. If the virtual environment was not activated automatically, this ensures it is by starting a new shell session.
### Django Configuration
1. Modify `settings.py`:
- Add `'my_app'` to the INSTALLED_APPS list.
2. Modify `urls.py`:
- Include the application's URLs:
```
from django.urls import path, include
urlpatterns = [
    path('', include('my_app.urls')),
]
```
3. Create `urls.py` in `my_app`:
- Define the URL pattern for the "Hello World!" view:
```
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
]
```
4. Create `views.py` in `my_app`:
- Define the view to render the "Hello World!" page:
```
from django.shortcuts import render

def helloworld(request):
    return render(request, 'helloworld.html')
```
5. Create helloworld.html Template:
- Place this file in a `templates` directory within `my_app`:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

By completing this exercise, you will gain practical experience in setting up a Django project, configuring routing, and creating a simple web application.
