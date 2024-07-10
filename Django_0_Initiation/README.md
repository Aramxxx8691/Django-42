# Initiation
## - ex00: Bash
This part of the script is a conditional statement that checks if a command-line argument is provided. If no argument is given, it displays a usage message and exits the script
- `if [ -z "$1" ]`: This checks if the first positional parameter/argument ($1) is empty (-z).
- `"Usage`: $0 <bit.ly URL>": The message to be printed after the name of the script ($0).

### Line 1: curl -sIl $1 | grep Location | cut -d ' ' -f 2
1. curl -sIl $1:
- `curl` is used to make an HTTP request.
- `-s` (silent mode): Suppresses progress output.
- `-I` (fetch headers only): Retrieves only the headers of the response.
- `-l` (lowercase L): Ensures correct handling of URLs.
2. | grep Location:
- `grep Location`: Filters the response headers to find the "Location" header, which indicates the URL to which the request is being redirected (if any).
3. | cut -d ' ' -f 2:
- `cut`: Processes the output of grep.
- `-d ' '`: Specifies the delimiter (a space character).
- `-f 2`: Selects the second field, which is the actual URL from the "Location" header.

### Line 2: curl -si -X GET $1 | grep "href" | cut -d \" -f 2
1. curl -si -X GET $1:
- `-i` (include headers): Includes the headers in the output along with the body of the response.
- `-X GET`: Specifies the HTTP method to use (GET in this case).
2. | grep "href":
- `grep "href"`: Searches the output for lines containing "href", which are usually HTML links.
3. | cut -d \" -f 2:
- `-d \"`: Specifies the delimiter (a double quote character).
- `-f 2`: Selects the second field, which is typically the URL or path found within the "href" attribute.

## - ex01: HTML and CSS Basics:
This exercise focuses on applying HTML and CSS basics while ensuring semantic HTML and separating style from content.
1. HTML Elements:
- `table`: Defines a table.
- `th`: Defines a table header cell.
- `td`: Defines a table data cell.
- `tr`: Defines a table row.
- `p`: Defines a paragraph.
- `ul`: Defines an unordered list.
- `ol`: Defines an ordered list.
- `li`: Defines a list item.
2. CSS Styling:
- Basic styling to adjust the appearance of these HTML elements, such as setting borders for tables, changing font styles, and adjusting spacing.

## - ex02: Forms and Input Elements:
This exercise focuses on creating and styling HTML forms, and linking JavaScript files:
1. HTML Elements:
- `form`: Defines a form for user input.
- `label`: Defines a label for an input element.
- `input`: Defines an input control.
- `br`: Defines a line break.
2. JavaScript Integration:
- Adding a <script> tag to link an external JavaScript file.
- Example: <script src="script.js"></script>

## - ex03: Recreating copy.html with External CSS and Image:
In this exercise, you will replicate a webpage based on the provided screenshot and CSS file. Your goal is to reproduce the layout and design as accurately as possible, using the provided CSS without modifications.
### Tasks:
1. Recreate copy.html Layout:
- `Objective`: Accurately recreate the content and structure of the provided copy.html file.
- `CSS File`: Use the provided style.css for styling without making any changes to it.
- `HTML Structure`: Ensure that your HTML reflects the design and structure shown in the screenshot. Maintain logical and semantic HTML practices.
2. Image Verification (Optional for Design Check):
- `Objective`: Use the page.png image to verify that your layout matches the provided design.
- `Image Use`: This image is for your personal reference to ensure your recreated page aligns with the design. It is not required to be included in the final HTML/CSS.

## - ex04: Script Placement and Alerts:
In this exercise, you will correctly place and import JavaScript files into your HTML document, ensuring that alerts are triggered as expected. You will also manage the inclusion of multiple JavaScript files without modifying them or adding additional JavaScript code.
### Tasks:
1. Script Placement:
- `Objective`: Place the provided JavaScript files in the correct project directory.
- `Requirement`: Ensure that these files are placed in a location where they can be accessed by your HTML document.
2. Creating snippets.html:
- `Objective`: Create an HTML file named snippets.html that imports the provided JavaScript files.
- `Script Tags`: Use <script> tags to include the four JavaScript files in the HTML document.
- `Alert Verification`: Ensure that the HTML file imports the scripts correctly and that alerts are triggered without any strange characters appearing.

## - ex05: W3C Validation and File Inclusion:
This exercise involves ensuring your HTML file adheres to W3C standards by fixing validation errors and ensuring all necessary files are correctly linked and included.
### Tasks:
1. W3C Validation:

- `Objective`: Edit the HTML file located in the ex05/ sub-folder of the d00.tar.gz tarball to ensure it passes W3C validation with no errors or warnings.
- `Validation Tool`: Use the [W3C Markup Validation Service](https://validator.w3.org/) to check the HTML file.
- `Editing Requirements`: Correct any errors or warnings reported by the W3C validator while preserving the file's content in its entirety.

2. File Inclusion Verification:
- `Objective`: Ensure that all necessary CSS, JavaScript, and audio files are correctly linked and included in the HTML file.
- `CSS Files`: Verify that all stylesheets are properly linked using <link> tags.
- `JavaScript Files`: Ensure all scripts are correctly linked using <script> tags.
- `Audio Files`: Check that any audio files are included using appropriate HTML tags (e.g., <audio>).
