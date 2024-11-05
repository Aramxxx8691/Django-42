# Starting
## - ex00: Python Variable Types
In this exercise, you will create a Python script named `var.py` that demonstrates various Python data types and their corresponding type outputs. This exercise will help you understand how to work with different data types and how to display their types using Python.

### Objective:
- Define a function named `my_var` in the `var.py` script.
- Declare variables of different types within this function.
- Print each variable's value and type in a specified format.

### Tasks:
1. Variable Declaration:
In the `var.py` script, declare several variables with different types.
2. Print Statements:
For each variable, print its value and its type using Python's built-in type() function.
3. At the end of the `var.py` script, include the following code to call the `my_var` function:
```
if __name__ == '__main__':
    my_var()
```
- `Purpose`: This construct is used to ensure that the `my_var` function is only executed when the script is run directly, not when it is imported as a module in another script.
- `__name__`: This special built-in variable gets assigned the name of the module in which it appears.
- If the script is run directly (e.g., python3 var.py), `__name__` is set to `__main__`.
- The if `__name__` == `__main__`: condition checks if the script is being executed directly. If true, it calls the `my_var` function.
- If the script is imported into another module, `__name__` is set to the module’s name, and the `my_var` function will not be called automatically.

### Example Usage:
When running python3 var.py from the command line, the if `__name__` == `__main__`: block ensures that the my_var function is executed, displaying the types of the declared variables. However, if `var.py` is imported into another script, the `my_var` function will not execute unless explicitly called.

### Learning Points:
- `Data Types`: Understand how Python categorizes and displays different data types.
- `Type Checking`: Learn to use the type() function to determine the type of a variable.
- `Conditional Execution`: Explore how if `__name__` == `__main__`: controls script execution based on its context (direct execution or import).

By completing this exercise and understanding the if `__name__` == `__main__`: construct, you'll gain insights into handling Python's data types and managing script execution based on how the script is run.

## - ex01: Reading and Displaying Numbers from a File
 In this exercise, you will create a Python script named numbers.py that reads numbers from a file and displays them in a specific format. The numbers will be read from a file named numbers.txt, which contains numbers from 1 to 100 separated by commas.

### Objective:
- Create a Python script named `numbers.py` that opens the `numbers.txt` file, reads the numbers it contains, and displays each number on a new line.

### Tasks:
1. File Handling:
- Open the numbers.txt file for reading.
2. Processing Content:
- Read the entire content of the file.
- Replace commas with new line characters to format the output correctly.
3. Printing Results:
- Print the processed content so that each number appears on a separate line.
4. Function Implementation:
- Define a function named numbers to perform the above tasks.

### Explanation:
1. File Handling:
- Use Python’s file handling methods to open and read the content of numbers.txt.
2. Processing Content:
- Utilize string methods to replace commas with newline characters to format the output.
3. Printing Results:
- Ensure the numbers are printed, each on a new line.

### Learning Points:
- `File Handling`: Learn how to open, read, and process files in Python.
- `String Manipulation`: Understand how to manipulate and format strings to meet output requirements.

By completing this exercise, you'll gain experience in reading from files, processing content, and understanding how to format and display output in Python.

## - ex02: Converting List of Tuples to a Dictionary
In this exercise, you will create a Python script named var_to_dict.py that processes a list of tuples and converts it into a dictionary. Each tuple contains a musician's name and their birth year. Your script will then format and display this dictionary, grouping musicians by their birth year.

### Objective:
- Create a Python script named `var_to_dict.py` that converts a list of tuples into a dictionary where the year is the key and the musician's name(s) are the value(s).
- Display the dictionary in a clear and formatted manner.

### Tasks:
1. Data Conversion:
- Convert the list of tuples into a dictionary using the year as the key and the musician's name as the value.
- Handle cases where multiple musicians share the same birth year by combining their names into a single entry.
2. Display Results:
- Print each key-value pair in the format `year : musician(s)`.

### Explanation:
1. Data Conversion:
- Dictionary Comprehension: This method is used to create a dictionary from the list of tuples. Dictionary comprehensions allow you to build a dictionary in a single, concise line. The key is the year, and the value is the name of the musician. When multiple musicians have the same birth year, their names are combined into a single entry, demonstrating how to aggregate data in a dictionary format.
2. Display Results:
- The dictionary is printed, with each year followed by the corresponding musician(s). This shows how to format and present data in a readable manner.

### Learning Points:
- Dictionary Comprehension: Learn to create dictionaries from lists using dictionary comprehensions. This technique helps in efficiently transforming and organizing data.
- Data Aggregation: Understand how to aggregate and display data in a formatted manner, especially when dealing with multiple entries for the same key.

By completing this exercise, you'll gain skills in converting data structures and formatting outputs based on specific requirements.

## - ex03: Displaying Capital Cities Based on State
In this exercise, you will create a Python script named capital_city.py that takes a state name as a command-line argument and displays the corresponding capital city. If the provided state name is unknown or if there are incorrect numbers of arguments, appropriate messages should be displayed.

### Objective:
- Write a Python script that takes a state name as an argument and displays its capital city.
- Handle cases where no arguments or too many arguments are provided.
- Display an "Unknown state" message if the state is not recognized.

### Tasks:
1. Command-Line Argument Handling:
- Check the number of arguments provided to the script.
- Ensure that exactly one argument is provided; otherwise, the script should exit without doing anything.
2. State to Capital Mapping:
- Use predefined dictionaries to map state names to their abbreviations and then map these abbreviations to capital cities.
- Look up the provided state name in the dictionary and print the corresponding capital city if found.
3. Error Handling:
- Print "Unknown state" if the provided state is not in the dictionary.
- Ensure that no output is generated if the number of arguments is incorrect.

### Explanation:
1. Command-Line Argument Handling:
- The script uses sys.argv to access command-line arguments. By checking the length of sys.argv, the script determines if exactly one argument is present. If not, the script exits without performing any further actions.
2. State to Capital Mapping:
- `states`: Maps state names to their abbreviations.
- `capital_cities`: Maps state abbreviations to their respective capital cities.
- The script first looks up the state abbreviation from the states dictionary and then retrieves the capital city from the capital_cities dictionary.
3. Error Handling:
- If the state provided is not found in the states dictionary, the script prints "Unknown state". This ensures that the user is informed when an invalid state is entered.

### Learning Points:
- Command-Line Argument Handling: Learn how to handle and validate command-line arguments in Python.
- Dictionary Lookup: Understand how to use dictionaries for efficient data retrieval and mapping.
- Error Messaging: Explore how to provide meaningful error messages based on input conditions.

By completing this exercise, you will gain experience in handling command-line arguments, working with dictionaries, and managing script execution based on user input.

## - ex04: Finding State by Capital City
In this exercise, you will create a Python script named state.py that performs the inverse operation of the previous exercise. Instead of taking a state as input and displaying its capital city, this script will take a capital city as input and display the corresponding state. The behavior should be similar to the previous exercise, handling cases where the capital city is not found or when incorrect inputs are provided.

### Objective:
- Create a Python script named state.py that opens the states and capital_cities dictionaries.
- Find and display the state corresponding to a given capital city.

### Tasks:
1. Dictionary Initialization:
- Copy the provided states and capital_cities dictionaries into the script.
2. Capital City Lookup:
- Implement a function to find the state associated with the provided capital city.
- If the capital city is not found, display "Unknown capital city".
3. Command-Line Argument Handling:
- Ensure the script processes exactly one command-line argument.
- Handle cases with no argument or multiple arguments appropriately.

### Explanation:
1. Dictionary Lookup:
- Use a function to search through the capital_cities dictionary to get the state abbreviation.
- Use another function to find the state name from the abbreviation.
2. Handling Unknown Capital Cities:
- Print "Unknown capital city" if the capital city is not present in the dictionaries.
3. Command-Line Arguments:
- Check for exactly one argument to ensure proper functionality.

### Example Usage:
When running python3 state.py Salem, the script will output Oregon. If the provided capital city is not found, like Paris, the script will output Unknown capital city.
 
## - ex05: Handling Multiple Queries
In this exercise, you will create a Python script named all_in.py that takes a comma-separated string of queries and determines if each query corresponds to a state, a capital city, or neither. The script should handle case insensitivity and ignore extra spaces. If there are multiple commas in succession or invalid input formats, the script should not produce output.

### Objective:
- Create a Python script named all_in.py that processes a comma-separated string of queries and identifies each as a state, capital city, or neither.

### Tasks:
1. String Processing:
- Split the input string by commas and remove extra spaces.
- Filter out empty strings that result from multiple consecutive commas.
2. Query Handling:
- For each query, check if it matches a state, capital city, or neither.
- Print the appropriate message for each query based on the dictionaries.
3. Command-Line Argument Handling:
- Ensure the script processes exactly one argument.
- Handle cases with no argument or multiple arguments appropriately.

### Explanation:
1. String Splitting and Stripping:
- Use split() and strip() methods to clean and prepare the input string for processing.
2. Dictionary Lookup:
- Use existing functions to find states and capital cities, then print the results in the required format.
3. Handling Invalid Formats:
- Ensure that invalid formats, such as multiple consecutive commas or extra spaces, are handled by filtering and processing the input properly.

## - ex06: Generating a Sorted List of Musicians
In this exercise, we will create a Python script that sorts and displays musicians based on their birth years. The task is to sort them by year in ascending order, and if multiple musicians share the same birth year, sort them alphabetically.

### Objective:
- Create a Python program that displays the names of musicians sorted by birth year and alphabetically for similar years.

### Tasks:
1. Sorting the Dictionary:
- Convert the dictionary into a list of tuples (musician, year).
- Sort this list first by birth year (ascending) and then alphabetically by name for those 2.with the same year.
2. Displaying Results:
- Print each musician's name, sorted as described, one name per line without showing the year.

### Explanation:
- To sort by multiple criteria, we use Python’s sorted() function with a custom sorting key. In this case, the first sorting criterion is the birth year, and the second one is the musician's name in case of a tie in the birth year.
- The sorting function looks like this:
```
sorted(d.items(), key=lambda x: (x[1], x[0]))
```
This sorts first by the year (x[1]) and then by the name (x[0]).

By completing this exercise, you practice sorting and handling dictionary data in Python. The musicians are displayed in ascending order by birth year, and ties are broken alphabetically by name.

## - ex07: Generating a Periodic Table in HTML
In this exercise, you'll create a Python script that reads element data from a text file and generates an HTML file representing a periodic table. Each element should be displayed in a "box" with its attributes listed.

### Objective:
- Read data from `periodic_table.txt`.
- Generate an HTML file `periodic_table.html` representing the periodic table with a specified layout.
- Ensure the HTML is valid and readable in any browser.

### Tasks:
1. Read and Parse Data:
- Parse each line of the input file to extract element details such as name, atomic number, symbol, and atomic mass.
2. Generate HTML:
- Create HTML content where each element is displayed in a "box".
- Each box contains the element’s name as an `<h4>` tag and its attributes listed in an unordered list (`<ul>`).
3. Write HTML to File:
- Save the generated HTML content to `periodic_table.html`.

### Example Code Breakdown:
- `parse_element(line)`: Parses a line of the input file and extracts element attributes.
- `generate_html(elements)`: Creates the HTML structure using the element data.
- Writes the generated HTML content to `periodic_table.html`.

### Code Explanation:
1. Parsing Function (parse_element):
- Reads each line, splits by =, and further splits by , to extract attributes.
- Builds a dictionary for each element.
2. HTML Generation (generate_html):
- Uses multi-line strings to create HTML structure.
- Iterates over the list of elements, formatting each element into HTML `<div>` tags.
3. Main Function (periodic_table):
- Reads the input file, parses the data, generates HTML, and writes it to `periodic_table.html`.

#### Example Usage:
- `Command`: python generate_periodic_table.py periodic_table.txt
- `Output`: Generates periodic_table.html with formatted element information.

By completing this exercise, you will practice working with file input/output, HTML generation, and CSS styling, ensuring that the periodic table is correctly formatted and visually appealing.