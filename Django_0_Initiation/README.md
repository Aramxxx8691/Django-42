# Initiation
## - ex00
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

## - ex01
## - ex02
## - ex03
## - ex04
## - ex05