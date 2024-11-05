import sys

def parse_element(line):
    element = {}
    parts = line.split(' = ')
    element['name'] = parts[0].strip()
    
    attributes = parts[1].split(', ')
    for attribute in attributes:
        key, value = attribute.split(':')
        element[key.strip()] = value.strip()
        
    return element

def generate_html(elements):
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
    <link rel="stylesheet" href="periodic_table.css">
</head>
<body>
"""
    for element in elements:
        html_content += f"""
        <div class="element">
            <h4>{element['name']}</h4>
            <ul>
                <li>No {element['number']}</li>
                <li>{element['small']}</li>
                <li>{element['molar']}</li>
                <li>{element['electron']}</li>
            </ul>
        </div>
"""

    html_content += """
</body>
</html>
"""
    return html_content

def periodic_table(input_file):
    elements = []
    try:
        with open(input_file, 'r') as file:
            for line in file:
                elements.append(parse_element(line))
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return

    html_content = generate_html(elements)

    output_file = "periodic_table.html"
    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f"✅ HTML file '{output_file}' has been generated successfully.")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        periodic_table(input_file)
    else:
        print("❌ Usage: python periodic_table.py <input_file>")
