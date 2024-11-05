# SQL
## - ex00: Create Movies Table (psycopg2)

### Objective
- Create a PostgreSQL Table: In this exercise, you will create a SQL table named ex00_movies using the psycopg2 library within a Django application.

### Instructions
1. Set Up the Django Application:
- Create a new Django application named ex00.
2. Define the View:
- Implement a view that handles requests at the URL `http://127.0.0.1:8000/ex00/init`. This view will connect to the PostgreSQL database and execute a command to create the `ex00_movies table`.

3. SQL Table Specifications:
The table must have the following fields:
- `title`: Unique, variable character chain (64-byte maximum size), non-null.
- `episode_nb`: Full, primary key (automatically generated).
- `opening_crawl`: Text field, can be null, with no size limit.
- `director`: Variable character chain (32-byte maximum size), non-null.
- `producer`: Variable character chain (128-byte maximum size), non-null.
- `release_date`: Date field (without time), non-null.

4. Error Handling:
- Ensure the view returns "OK" if the table creation is successful.
- If there is an error during the database connection or table creation, return an error message describing the problem.

### Example Usage
`Important`: Make sure you run this within your Docker environment.

1. Start the Docker Containers:
```docker-compose up```

2. Visit the URL:
- Open your browser and navigate to `http://127.0.0.1:8000/ex00/init` to trigger the table creation.

### Explanation
- `Connecting to the Database`: Use the psycopg2 library to establish a connection to the PostgreSQL database with the credentials specified in your `.env` file.
- `Creating the Table`: Write an SQL command to create the `ex00_movies` table with the defined specifications, ensuring that the table is created only if it doesn’t already exist.
- `Returning Responses`: Implement response handling in your view to provide feedback on the operation's success or failure, including detailed error messages for debugging.

## - ex01: Create Movies Model (Django ORM)
### Objective
- Define a Django Model: In this exercise, you will create a Django model named `Movies` that represents a table in your PostgreSQL database, implementing the same structure as the `ex00_movies` table from the previous exercise.

### Instructions
1. Set Up the Django Application:
- Create a new Django application named ex01.

2. Define the Movies Model:
In the models.py file of the ex01 application, create a model named Movies with the following fields:
- `title`: A unique variable character field with a maximum length of 64 bytes, which cannot be null.
- `episode_nb`: An integer field that serves as the primary key.
- `opening_crawl`: A text field that can be null, with no size limit.
- `director`: A variable character field with a maximum length of 32 bytes, which cannot be null.
- `producer`: A variable character field with a maximum length of 128 bytes, which cannot be null.
- `release_date`: A date field (without time) that cannot be null.

3. Override the `__str__` Method:
- Redefine the `__str__` method in the Movies model to return the `title` attribute, providing a human-readable representation of the model instances.

4. Create a View to Confirm Creation:
- Implement a view that responds with "Movies model created!" when accessed at the URL `http://127.0.0.1:8000/ex01`.

5. Run Migrations:
- Ensure to create and apply migrations for your new model by running the appropriate commands in your Docker container.

### Example Usage
`Important`: Make sure you run this within your Docker environment.
1. Start the Docker Containers:
```
docker-compose up
```
2. Apply Migrations:
- Open a terminal in your Docker container and run:
```
python3 manage.py makemigrations ex01
python3 manage.py migrate
```
3. Visit the URL:
- Open your browser and navigate to `http://127.0.0.1:8000/ex01` to confirm the model creation.

### Explanation
- `Django Model Definition`: This section will leverage Django's ORM to define the structure of the Movies table within the database using a Python class.
- `Primary Key and Uniqueness`: The model ensures the episode_nb serves as a primary key while enforcing uniqueness for the title.
- `Human-Readable Representation`: By overriding the __str__ method, the model provides a meaningful string representation that can be helpful for debugging and displaying instances in the admin interface.

## Comparing ex00 and ex01
|  Feature | ex00: psycopg2 (SQL) | ex01: Django ORM |
| :---------: | :---------------------------: | :---------------------------: |
| Database Management | Requires direct SQL commands and manual table creation | Django automates table creation via `models.py` |
| Data Validation | Limited, requires explicit checks in SQL | Built-in validation based on model field specifications |
| Error Handling | Custom error handling with try-except blocks | Django handles many errors and provides model validation |
| Flexibility | SQL commands allow precise control over queries and schemas | Django ORM abstracts SQL, providing flexibility in code |
| Code Reusability | Requires repeating SQL code for each operation | Models are reusable across views and applications |
| Ease of Use | More code-intensive; requires knowledge of SQL syntax | Simplified; Django abstracts SQL and automates operations |

## - ex02: Manage Movies Table (psycopg2)
### Objective
- Extend database functionality by creating a Django application that allows you to create, populate, and display records in a PostgreSQL table named `ex02_movies` using the psycopg2 library.

### Instructions
1. Set Up the Django Application
- Create a new Django application named `ex02` within your project.
2. Create Views for Table Management
Implement the following views for interacting with the `ex02_movies` table:
- Table Creation (`/ex02/init`):
  - This view should create a table named `ex02_movies` with specifications identical to the ex00_movies table, including fields for `title`, `episode_nb`, `opening_crawl`, `director`, `producer`, and `release_date`.
  - On success, it should display "OK". If there is an error, the error message should be displayed.
- Table Population (`/ex02/populate`):
  - This view should populate the `ex02_movies` table with specific Star Wars movie records.
  - Each record must include an `episode_nb`, `title`, `director`, `producer`, and `release_date`.
  - For each successful insertion, it should display "OK". If an error occurs, the error message should be displayed.
- Table Display (`/ex02/display`):
  - This view should retrieve and display all records from the `ex02_movies` table in an HTML table format, with columns for all fields.
  - If there is no data available or an error occurs, it should display "No data available".
3. SQL Table Specifications
The `ex02_movies` table must have the following fields:
- `title`: Unique, variable character chain (64-byte maximum size), non-null.
- `episode_nb`: Integer, primary key.
- `opening_crawl`: Text field, nullable.
- `director`: Variable character chain (32-byte maximum size), non-null.
- `producer`: Variable character chain (128-byte maximum size), non-null.
- `release_date`: Date field, non-null.
4. Error Handling
Ensure each view provides clear and meaningful feedback:
- Display "OK" for successful operations.
- If an error occurs during table creation, insertion, or data retrieval, return an error message for debugging.

### Example Usage
Important: Ensure your Docker environment is up and running.
1. Start Docker Containers:
```
docker-compose up
```
2. Table Creation:
- Visit `http://127.0.0.1:8000/ex02/init` to create the table. Expect "OK" if successful.
3. Populate Table:
- Visit `http://127.0.0.1:8000/ex02/populate` to insert records into the table. Expect "OK" for each successful insertion.
4. Display Data:
- Visit `http://127.0.0.1:8000/ex02/display` to view the table content in an HTML table. If the table is empty or there’s an error, you should see "No data available".

### Explanation
- `Database Connection`: Utilize psycopg2 to establish a connection to PostgreSQL, with credentials configured in your `.env` or Django settings.
- `Table Operations`: For each view, write SQL commands to interact with the `ex02_movies` table as required.
- `Response Handling`: Each view should provide clear feedback, allowing users to understand the result of their actions, whether successful or erroneous.

## - ex03: Create and Populate Movies Table (psycopg2)
### Objective
- Build a Django model for the `Movies` table, mirroring the structure from `ex01`.
- Populate this table with specific Star Wars movie data using a view accessible via a specified URL.
- Display all data in an HTML table view if available; otherwise, show an appropriate message.

### Instructions
1. Create a New Django Application:
- Set up a new Django app named ex03.
2. Define the Movies Model:
In `models.py`, create a model named `Movies` with the following fields:
- `title`: Unique, character field with a maximum length of 64 characters, non-null.
- `episode_nb`: Integer, primary key.
- `opening_crawl`: Text field, nullable, with no size limit.
- `director`: Character field with a maximum length of 32 characters, non-null.
- `producer`: Character field with a maximum length of 128 characters, non-null.
- `release_date`: Date field (no time component), non-null.
3. Create the Populate View:
- Add a view in `views.py` at `http://127.0.0.1:8000/ex03/populate`.
- Use Django ORM to insert multiple rows into the `Movies` table with the specified Star Wars movie details.
- Display "OK" for each successful insertion or an error message if an insertion fails.
4. Create the Display View:
- Define a view at `http://127.0.0.1:8000/ex03/display` to fetch all entries in the `Movies` table and render them in an HTML table format.
- If no data exists or an error occurs, display "No data available."
5. HTML Template for Display View:
- Design an HTML template to list all the movie records in a tabular format, including null fields.

### Example Usage
1. Run the Server:
Start the Django server, preferably within a Docker environment, to ensure compatibility.
```
docker-compose up
```
2. Populate the Table:
- Navigate to `http://127.0.0.1:8000/ex03/populate` in your browser to insert the Star Wars movies.
3. Display the Table Data:
- Visit `http://127.0.0.1:8000/ex03/display` to view the inserted movies. If the table is empty, the page will show "No data available."

### Explanation
- `Database Interaction`: Use Django’s ORM for data handling, including insertion and retrieval.
- `View Structure`:
  - The `populate` view manages insertion and provides feedback on success or error.
  - The `display` view retrieves all records and renders them in a neatly styled HTML table, with placeholder text if data is absent.
- `Error Handling`: Ensure that each insertion in populate either confirms success or details an error to help with debugging.

## Comparing ex02 and ex03
|  Feature | ex02 | ex03 |
| :---------: | :---------------------------: | :---------------------------: |
| Model | Identical in both ex02 and ex03 | Identical in both ex02 and ex03 |
| Populate view | Inserts movies; returns "OK" or error | Inserts specific episodes; returns "OK" or error |
| Display view | Displays all movies | Displays all movies |
| remove view | Allows removal of movies | Not included |
| Main URLs | /populate, /display, /remove | /populate, /display |

## - ex04: Create, Populate, Display, and Remove Movies (Django ORM)
### Objective
- Create a table for the `Movies` database in PostgreSQL.
- Populate this table with specific Star Wars movie data through a view accessible via a specified URL.
- Display all data in an HTML table view, or display an appropriate message if the table is empty.
- Enable users to delete individual movie records from the database.

### Instructions
1. Create a New Django Application:
- Set up a new Django app named `ex04`.
2. Define SQL Table Creation View:
Create a view at `http://127.0.0.1:8000/ex04/init` to initialize a table named `ex04_movies` in PostgreSQL with the following columns:
- `title`: Unique character field, max length 64, non-null.
- `episode_nb`: Integer, primary key.
- `opening_crawl`: Text field, nullable.
- `director`: Character field, max length 32, non-null.
- `producer`: Character field, max length 128, non-null.
- `release_date`: Date field, non-null.
If successful, the view should return "OK"; otherwise, it displays an error message.
3. Populate the Movies Table:
- Add a view at `http://127.0.0.1:8000/ex04/populate` to insert multiple rows into `ex04_movies` using predefined Star Wars movie data.
- This view should display "OK" for each successful insertion and an error message if any insertion fails.
4. Display Movies:
- Create a view at `http://127.0.0.1:8000/ex04/display` to retrieve all entries from `ex04_movies` and render them in an HTML table format.
- If the table is empty or an error occurs, the page should display "No data available."
5. Delete a Movie:
- Define a view at `http://127.0.0.1:8000/ex04/remove` that displays a dropdown list of all movie titles in the `ex04_movies` table.
- Allow users to select and delete a movie title, updating the dropdown list with available options after each deletion.
- If there are no movies to delete, the page should show "No data available."

### Example Usage
1. Run the Server:
- Start the Django server, ideally within a Docker environment for PostgreSQL compatibility:
```
docker-compose up
```
2. Initialize the Database Table:
- Navigate to `http://127.0.0.1:8000/ex04/init` to create the `ex04_movies` table.
3. Populate the Table:
- Go to `http://127.0.0.1:8000/ex04/populate` in your browser to insert the predefined movie entries.
4. Display the Table Data:
- Visit `http://127.0.0.1:8000/ex04/display` to view the list of movies in an HTML table. If the table is empty, the page displays "No data available."
5. Remove a Movie Entry:
- Navigate to `http://127.0.0.1:8000/ex04/remove`, select a movie title from the dropdown list, and delete the record. The dropdown list updates accordingly.

### Explanation
1. Database Interaction:
- Uses raw SQL commands to initialize the table, populate data, retrieve records, and delete records. This approach ensures flexibility when working directly with PostgreSQL.
2. View Structure:
- `Initialization (init)`: Sets up the table structure in the PostgreSQL database.
- `Population (populate)`: Inserts data into the table, with feedback on success or failure for each entry.
- `Display (display)`: Retrieves and renders data in an HTML table, including null fields if present.
- `Deletion (remove)`: Provides an option to delete individual records, updating the dropdown menu dynamically.
3. Error Handling:
- Ensures that errors in table creation, data insertion, data retrieval, or deletion are captured and clearly displayed, assisting in debugging.

## - ex05: Create, Populate, Display, and Remove Movies (psycopg2)
### Objective
In this exercise, we will create a Django app named ex05 that includes a model for movies and implements various views to manage movie data through specified URLs.

### Instructions
1. Create the Django Application:
- Initialize a new Django app named `ex05`.
2. Define the Movies Model:
Inside the `models.py` file, create a model named `Movies` with the following fields:
- `title`: A unique character field with a maximum length of 64 characters.
- `episode_nb`: An integer that serves as the primary key.
- `opening_crawl`: A text field that can be nullable.
- `director`: A character field with a maximum length of 32 characters.
- `producer`: A character field with a maximum length of 128 characters.
- `release_date`: A date field that cannot be null.
3. Implement the Populate View:
Create a view that allows data insertion for the Movies model. This view should:
- Reinstate any deleted movie data from a predefined list.
- Return a page displaying "OK" for each successful insertion or an error message for any failures.
4. Implement the Display View:
- Develop a view that retrieves all entries in the Movies table and displays them in an HTML table format.
- If there are no entries available, the page should display "No data available."
5. Implement the Remove View:
- Create a view that displays an HTML form containing a dropdown list of movie titles and a submit button named "remove."
- When the form is submitted, the selected movie should be deleted from the database. The form should then redisplay with the updated list of remaining titles.
- If no titles are available or an error occurs, the page should display "No data available."

### Example Usage
1. Run the Server:
- Start the Django development server to test the application.
2. Populate the Movies Table:
- Access the designated URL to populate the Movies table with predefined data.
3. Display the Movie Data:
- Visit the appropriate URL to view all movie entries in a structured format.
4. Remove a Movie Entry:
- Navigate to the designated URL to select a movie from the dropdown and delete it. The updated list of titles will be displayed after submission.

### Explanation
1. Database Interaction:
- This app utilizes Django’s Object-Relational Mapping (ORM) to handle all data operations, including insertion, retrieval, and deletion of movie records.
2. View Structure:
- The populate view manages the initial data insertion, providing user feedback on the process.
- The display view retrieves and presents all movies, ensuring to communicate when no data is available.
- The remove view allows users to delete a specific movie and refreshes the list dynamically.
3. Error Handling:
- Each view includes error handling mechanisms to catch issues during database operations, ensuring informative messages are displayed to users when necessary.

## Comparing ex04 and ex05
|  Feature | ex04 | ex05 |
| :---------: | :---------------------------: | :---------------------------: |
| Model Structure | Movies model with title, episode number, opening crawl, director, producer, and release date | Identical Movies model with the same structure as in ex04 |
| Populate View | Inserts predefined Star Wars movies into the database | Reinserts deleted movies and adds predefined data to the Movies table |
| Display View | Fetches and displays all movie entries in an HTML table | Similar functionality to ex04, showing all entries in a table or "No data available" |
| Remove View | Not included | Provides a form to delete selected movie titles from the database |
| Error Handling | Displays error messages for failed insertions | Displays error messages for both failed insertions and deletions |
| URL Endpoints | /ex04/populate and /ex04/display | /ex05/populate, /ex05/display, and /ex05/remove |
| User Interaction | Basic data insertion and display | Adds functionality for users to remove movies dynamically via a form |

## - ex06: Retrieve, Update, and Delete Characters and Planets (psycopg2)

### Objective
In this exercise, we will create a Django app named `ex06` that includes models for characters and planets. We will implement views to retrieve, update, and delete character and planet data through specified URLs.

### Instructions
1. Create the Django Application:
- Initialize a new Django app named `ex06`.
2. Define Models for Characters and Planets: In `models.py`, create two models: `Character` and `Planet` with the following fields:
`Character` model:
- `name`: A unique character field with a maximum length of 64 characters.
- `birth_year`: A character field for representing the birth year of the character.
- `gender`: A character field with a maximum length of 16 characters.
- `homeworld`: A foreign key linking to the `Planet` model.
3. `Planet` model:
- `name`: A unique character field with a maximum length of 64 characters.
- `climate`: A character field with a maximum length of 32 characters.
- `diameter`: An integer field representing the diameter of the planet.
3. Implement the Retrieve View:
- Develop a view that displays all characters and their corresponding homeworld information in an HTML table.
- If no characters are available, the page should display "No data available."
4. Implement the Update View:
- Create a view that allows users to update a character’s information.
- The view should display a form pre-filled with the character's current details and allow modifications.
- Upon successful update, the page should display "Update successful" or an appropriate error message for failures.
5. Implement the Delete View:
- Create a view with an HTML form containing a dropdown list of character names and a "delete" submit button.
- When submitted, the selected character is removed from the database, and the form refreshes with the updated list of characters.
- If no characters remain, display "No data available."

### Example Usage
1. Run the Server:
- Start the Django development server to test the application.
2. View Characters and Planets:
- Access the specified URL to see all character entries with their associated homeworlds displayed in a table.
3. Update Character Information:
- Visit the designated URL, select a character, modify their details in the form, and submit to update the information.
4. Delete a Character Entry:
- Navigate to the specified URL, select a character from the dropdown, and delete them from the database. The list of characters will update after submission.

### Explanation
1. Database Management:
- This app uses Django’s ORM for managing character and planet records, supporting efficient retrieval, updates, and deletions.
2. View Functionality:
- The retrieve view presents a comprehensive list of characters with their homeworld details, ensuring the user knows if no data is present.
- The update view provides a form-based interface for editing character details, enhancing user interaction and allowing updates directly from the page.
- The delete view enables easy removal of a character while dynamically refreshing the list to display remaining entries.
3. Error Handling:
- Each view includes error-handling mechanisms to manage potential issues, such as nonexistent entries or update conflicts, ensuring the user receives helpful feedback in case of errors.

## - ex07: Manage Movies with Automatic Timestamps (Django ORM)

### Objective
In this exercise, we will create a Django app named `ex07` to manage movie records with automatic timestamps. The app will include a model for movies, views to populate, display, and update movie data, and a form to modify selected fields.

### Instructions
1. Create the Django Application:
- Initialize a new Django app named `ex07`.
2. Define the Movies Model: In models.py, create a Movies model with the following fields:
- `title`: A unique character field with a maximum length of 64 characters.
- `episode_nb`: An integer serving as the primary key.
- `opening_crawl`: A text field that can be nullable.
- `director`: A character field with a maximum length of 32 characters.
- `producer`: A character field with a maximum length of 128 characters.
- `release_date`: A date field that cannot be null.
- `created_at`: A datetime field that is automatically set to the current date and time when the record is created.
- `updated_at`: A datetime field that is automatically set to the current date and time when the record is created and automatically updates with each modification.
3. Implement the Populate View:
- Create a view that inserts predefined movie data into the Movies model.
- This view should return a page displaying "OK" for each successful insertion or an error message for any failures.
4. Implement the Display View:
- Develop a view that retrieves and displays all entries in the Movies table in an HTML table format.
- If there is no data available or an error occurs, the page should display "No data available."
5. Implement the Update View:
- Create a view that manages a form allowing users to select a movie from a dropdown list and edit its opening_crawl field.
- Upon form submission, the selected movie’s opening_crawl field should update with the entered text, and the page should display "Update successful."
- If there is no available data or an error occurs, the page should display "No data available."

### Example Usage
1. Run the Server:
- Start the Django development server to test the application.
2. Populate the Movies Table:
- Access the designated URL (`127.0.0.1:8000/ex07/populate`) to insert predefined data into the Movies table.
3. Display the Movie Data:
- Visit the display URL (`127.0.0.1:8000/ex07/display`) to view all movies in a structured format.
4. Update the Opening Crawl Field:
- Navigate to the update URL (`127.0.0.1:8000/ex07/update`), select a movie, enter new text for opening_crawl, and submit the form. A success message will display upon successful update.

### Explanation
1. Model Design:
- The Movies model includes fields for each attribute of a movie, along with `created_at` and `updated_at` fields. These timestamp fields automatically update when a record is created or modified, making it easier to track changes.
2. View Structure:
- The `populate` view initializes the data, providing feedback on each insertion's success or failure.
- The `display` view retrieves and presents all movies, ensuring the user knows if no data is available.
- The `update` view provides a form-based interface to modify a movie's `opening_crawl` field, allowing for a simple and interactive update experience.
3. Error Handling:
- Each view contains error-handling mechanisms to manage potential issues, such as missing data or database conflicts, and to ensure informative feedback for users.

This setup enables basic CRUD operations on movie data, demonstrating how to utilize Django’s ORM for managing models with automatic timestamps.

## Comparing ex06 and ex07
|  Feature | ex06 | ex07 |
| :---------: | :---------------------------: | :---------------------------: |
| Model | Basic movie fields without timestamps | Extended movie fields with `created_at` and `updated_at` timestamps |
| Populate View | Populates the Movies table with predefined data | Populates the Movies table with predefined data (same as `ex06`) |
| Display View | Displays movies in an HTML table | Displays movies in an HTML table with the same format as `ex06` |
| Update View | Allows updating the opening_crawl field using a form | Allows updating the `opening_crawl` field using a form, with automatic `updated_at` timestamp changes |
| Timestamps |Not available in the model | Includes `created_at` (auto-set on creation) and `updated_at` (auto-updates on modification) |
| Error Handling | Displays "No data available" on errors or empty data | Displays "No data available" on errors or empty data (similar to `ex06`) |

## - ex08: Planets and People Database Management

This Django app, `ex08`, provides a web interface to manage and display data related to planets and people, using data from `planets.csv` and `people.csv`. The app includes three main views for initializing the database, populating tables, and displaying data with specific requirements.

### Objectives
- Create database tables to store information about planets and people, including relationships.
- Populate tables using data from CSV files.
- Provide a sorted, filtered display of the data through a web interface.

### URLs and Views
The following URLs are accessible through this app:
1. 127.0.0.1:8000/ex08/init
- Purpose: Initializes the database by creating the required tables.
- Tables Created:
  - ex08_planets: Fields:
    - `id`: Primary key, serial.
    - `name`: Unique, varchar(64), non-null.
    - `climate`: Varchar.
    - `diameter`: Integer.
    - `orbital_period`: Integer.
    - `population`: Bigint.
    - `rotation_period`: Integer.
    - `surface_water`: Real.
    - `terrain`: Varchar(128).
  - ex08_people: Fields:
    - `id`: Primary key, serial.
    - `name`: Unique, varchar(64), non-null.
    - `birth_year`: Varchar(32).
    - `gender`: Varchar(32).
    - `eye_color`: Varchar(32).
    - `hair_color`: Varchar(32).
    - `height`: Integer.
    - `mass`: Real.
    - `homeworld`: Varchar(64), foreign key referencing `ex08_planets.name`.
- Response:
  - Returns "OK" if tables are successfully created.
  - If an error occurs, returns a message detailing the problem.
2. 127.0.0.1:8000/ex08/populate
- Purpose: Populates the `ex08_planets` and `ex08_people` tables with data from `planets.csv` and `people.csv`, respectively.
- `Functionality`:
  - Reads data from each CSV file.
  - Attempts to insert each record into its respective table.
- `Response`:
  - Displays "OK" for each successful insertion.
  - If an error occurs during insertion, it displays an error message identifying the record and the issue.
3. 127.0.0.1:8000/ex08/display
- `Purpose`: Displays a sorted list of people, including their names, homeworlds, and homeworld climate.
- `Data Requirements`:
  - Displays all characters’ names, their homeworld, and homeworld climate where climate is either "windy" or "moderately windy."
  - The list is sorted alphabetically by character name.
- `Response`:
  - Displays a table with the required data.
  - If no data is available, returns "No data available."

### Usage Guide
1. Initialize Tables
- Access `127.0.0.1:8000/ex08/init` to create the necessary tables. The view ensures that tables are created if they do not already exist.
- Success message: "OK."
2. Populate Data
- Use `127.0.0.1:8000/ex08/populate` to populate the tables with data from the provided CSV files (`planets.csv` and `people.csv`).
- The view checks each record and inserts data, displaying "OK" for success and identifying any errors encountered.
3. Display Data
- Access `127.0.0.1:8000/ex08/display` to view the sorted list of characters, homeworlds, and climates.
- If no data is available, or an error occurs, the view simply displays "No data available."

### Explanation
1. Model Design:
- The `Planets` and `People` models have been created to represent planets and individuals, with `People` linked to `Planets` by a foreign key on the `homeworld` field, establishing a many-to-one relationship. This design supports data integrity by associating people with existing planets.
2. View Structure:
- The `init` view sets up the database tables and handles any creation errors.
- The `populate` view loads data from CSV files into the database, with feedback on each insertion to track successes and errors.
- The `display` view retrieves and shows filtered results, presenting only people from planets with specified climate conditions.
3. Error Handling:
- Each view includes error management to handle issues like duplicate entries and invalid foreign keys. Users receive clear messages about any errors that arise.

This setup allows streamlined data import, filtering, and display, showcasing Django's ORM capabilities for managing related models efficiently.

## - ex09: People and Planets Database (Django ORM)

### Objectives
Create a Django app named ex09 with two models (Planets and People) to represent planets and individuals in a fictional universe. The app should support data display in a table, showcasing people, their homeworld, and the climate of that homeworld.

### Requirements
1. Planets Model: Fields:
- `name`: Unique, max length of 64 characters, required.
- `climate`: Text field.
- `diameter`: Integer.
- `orbital_period`: Integer.
- `population`: Big integer.
- `rotation_period`: Integer.
- `surface_water`: Float.
- `terrain`: Text field.
- `created`: Auto-set datetime for record creation.
- `updated`: Auto-updated datetime for each record modification.
String Representation: Displays `name`.
2. People Model: Fields:
- `name`: Required, unique, max length of 64 characters.
- `birth_year`: Max length of 32 characters.
- `gender, eye_color, hair_color`: Max length of 32 characters.
- `height`: Integer.
- `mass`: Float.
- `homeworld`: Foreign key referencing Planets model's name field.
- `created`: Auto-set datetime for record creation.
- `updated`: Auto-updated datetime for each record modification.
String Representation: Displays `name`.
3. Views and Templates:
- The `display` view (accessible at `/ex09/display`) shows a table with each person's name, homeworld, and climate.
- If no data is available, a message is displayed with a command to load initial data.

### Usage
1. Model Setup:
- Implement models in `models.py` with Django’s ORM, using fields as described above.
- Set `__str__()` methods for meaningful representations in Django admin and query results.
2. Data Loading:
- To populate the database, run:
```
python manage.py loaddata ex09/ex09_initial_data.json
```
- This command will insert the initial data from `ex09_initial_data.json`, pre-populating the `Planets` and `People` tables with records for display.
3. Views and Templates:
- In `views.py`, the display view retrieves all People records, sorted alphabetically by name.
- In `display.html`, an HTML table shows each person’s `name`, `homeworld`, and `climate`, or a message with data load instructions if the database is empty.

### Explanation
1. Model Design:
- The `Planets` model represents each planet with details like climate, population, and terrain. The `People` model represents each person, including a foreign key (`homeworld`) linking them to their respective planet, ensuring data consistency.
2. View Structure:
- The `display` view retrieves all People records and displays them in a table format, sorted by name for easy readability. The view uses `select_related` for efficient foreign key lookups of `homeworld`.
3. Error Handling:
- If no data exists, the view displays a message with a command to load initial data from `ex09_initial_data.json`. This ensures users have guidance on setting up the initial dataset for testing or display.

This setup offers a straightforward display and data loading process, leveraging Django’s ORM for efficient model handling and foreign key management.

## Comparing ex08 and ex09
|  Feature | ex08 | ex09 |
| :---------: | :---------------------------: | :---------------------------: |
| Models | Single model: `Movies` with fields specific to movie attributes | Two models: `Planets` and `People`, representing planets and individuals with various interrelated fields |
| Primary Focus | CRUD operations on movie data (e.g., `title`, `director`, `release_date`) | Displaying characters with linked homeworld data and additional attributes (e.g., `climate`, `population`, `height`) |
| Foreign Key Use | Not used; no foreign key relationships | People model contains a foreign key to Planets, linking each character to a homeworld |
| Data Population | Direct insertion of movie data with a populate view | Uses loaddata command to insert initial data from JSON (`ex09_initial_data.json`) file |
| Data Display | Displays all movies in a simple list view | Displays all characters with their homeworlds and climates in a table view, sorted by character name |
| Dynamic Fields | Uses a form-based update view to modify `opening_crawl` for each movie | Does not involve form-based updates; focuses on displaying relational data between characters and planets |
| Timestamp Management | `created_at` and `updated_at` fields auto-set for `Movies` model | created and updated fields for both Planets and People, allowing for tracking record creation and modification |
| Empty Data Handling | Shows an empty state message when no movie records exist | Displays a message instructing the user to load initial data if no records are available |
| Template Style | Basic list style for displaying movie data | Tabular display with styling for characters, homeworlds, and climates |

## - ex10: Django App with Many-to-Many Relationships

### Objective
In this exercise, you will create a new Django app named `ex10`, which incorporates all previous exercises. The app consists of three models: `Planets`, `People`, and `Movies`, with a focus on establishing a many-to-many relationship between `People` and `Movies`. The application allows users to search for characters based on various criteria, displaying relevant results in a user-friendly format.

### Instructions
1. Set Up the Django App: Create a new Django app named `ex10` within your project.
2. Define Models:
- `Planets Model`: Stores information about different planets, including attributes like climate, diameter, and population.
- `People Model`: Stores details about characters, linking each character to a homeworld through a foreign key.
- `Movies Model`: Represents films and includes a many-to-many relationship with the `People` model.
3. Load Initial Data: Use the provided `ex10_initial_data.json` file to populate the models with sample data. Reference this file in your `views.py` instead of using the `loaddata` command.
4. Implement Search Functionality:
- Create a view to handle user searches via the URL: `127.0.0.1:8000/ex10`.
- Include a search form with fields for filtering results based on movie release dates, planet diameters, and character genders.
5. Run the Application: Start the Django development server and access the search interface.

### Learning Points
- Understand the implementation of many-to-many relationships in Django, enabling multiple characters to be associated with multiple movies.
- Gain experience with Django's ORM for querying related data across multiple models.
- Learn to create dynamic search forms and handle user input to filter results effectively.
- Understand the use of initial data fixtures to populate the database for testing and development purposes.
- Explore Django's templating system to render search results in a structured HTML format.

### Example Usage
After running the Django server, navigate to `127.0.0.1:8000/ex10`. You can:
- Enter a minimum and maximum release date to filter movies.
- Specify a minimum planet diameter to find relevant planets.
- Select a character gender from the dropdown list to narrow down character results.

Upon submission, the application will display the results in a table format. If no matches are found, a message stating "Nothing corresponding to your research" will be displayed.

### Explanation
#### Models
1. Planets: Fields:
- `id`: Primary key (auto-generated).
- `name`: Unique name of the planet.
- `Various characteristics`: climate, diameter, orbital_period, population, rotation_period, surface_water, terrain.
- `Timestamps`: created, updated.
2. People: Fields:
- `id`: Primary key (auto-generated).
- `name`: Unique name of the character.
- `Personal attributes`: birth_year, gender, eye_color, hair_color, height, mass.
- `homeworld`: Foreign key referencing the `Planets` model.
3. Movies: Fields:
- `title`: Unique title of the movie.
- `episode_nb`: Episode number of the film (unique).
- `opening_crawl`: The opening text of the film.
- `characters`: Many-to-many relationship with the People model.
- `Additional details`: director, producer, release_date.

### View Functionality
A view is created to handle user searches. The form includes the following fields:
- Movies Minimum Release Date: Date input.
- Movies Maximum Release Date: Date input.
- Planet Diameter Greater Than: Numeric input.
- Character Gender: Dropdown list populated with distinct gender values from the People model.

### Search Logic
Upon form submission, the app performs the following:
- Validates the input fields.
- Searches for characters that match the specified criteria:
  - Gender matches the selected option.
  - Film release date falls within the specified range.
  - Homeworld's diameter is greater than or equal to the specified value.

### HTML Template
The results are rendered in the display.html template, which structures the output in a user-friendly format, including a table displaying:
- Character’s name
- Gender
- Film title
- Homeworld name
- Homeworld diameter

### Code Overview
- `models.py`: Defines the Planets, People, and Movies models with necessary relationships.
- `forms.py`: Contains the SearchForm class, managing form validation and dropdown population for character genders.
- `views.py`: Handles the logic for searching and displaying characters based on user input, reading initial data from the ex10_initial_data.json file, populating models, and processing the search form.

### Sample Data
Include the `ex10_initial_data.json` file in your project directory to ensure your models are populated correctly. The file should contain structured data matching the expected model formats.

### Running the Application
1. Ensure you have Django installed and set up correctly.
2. Create the `ex10` app in your Django project.
3. Define the models as specified above.
4. Add the view and form logic to your application.
5. Populate your database using the provided `ex10_initial_data.json`.
6. Run the server and navigate to `127.0.0.1:8000/ex10` to access the search functionality.

### Conclusion
This exercise reinforces understanding of Django models, form handling, and many-to-many relationships. The combination of previous exercises into this app provides a comprehensive overview of working with related data in Django.

## Helper Commands for Docker
This section provides helpful commands to manage your PostgreSQL container and run necessary operations within your Django application.

1. Enter the PostgreSQL Container
To access the PostgreSQL database running in a Docker container, use the following command:
```
docker exec -it postgres psql -U djangouser -d postgres
```
2. Run the SQL Command
Once inside the PostgreSQL terminal, you can run SQL commands. For example, to describe the structure of the `ex00_movies` table, enter:
```
\d ex00_movies
```
3. Exit the psql Terminal
To exit the PostgreSQL terminal, simply use the following command:
```
\q
```
4. Full Command for Table Description
You can also run the command to describe the ex00_movies table directly from your terminal without entering the PostgreSQL shell:

```
docker exec -it postgres psql -U djangouser -d djangotraining -c "\d ex00_movies"
```
5. Load Initial Data
To load initial data into your database, you can run:

```
docker-compose run --rm d05 sh -c "python manage.py loaddata ex09/ex09_initial_data.json"
```
6. Clean Up Unused Docker Resources
To clean up unused Docker volumes, use:

```
docker volume prune -f
```
To clean up unused Docker images, containers, and networks, run:

```
docker system prune -f -a
```
