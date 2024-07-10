import sys

def parse_element(line):
    element = {}
    parts = line.split(' = ')
    element['name'] = parts[0].strip()

    attributes = parts[1].split(', ')
    for attributes in attributes:
        key, value = attributes.split(':')
        element[key.strip()] = value.strip()
    return element

def periodic_table(input_file, output_file):
    elements = []
    try:
        with open(input_file, 'r') as file:
            for line in file:
                elements.append(parse_element(line))
    except FileNotFoundError:
        print('File not found')
        return
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid black; padding: 10px; text-align: left; }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>Element</th>
            <th>Symbol</th>
            <th>Atomic Number</th>
            <th>Atomic Mass</th>
            <th>Electrons</th>
        </tr>
"""

    for element in elements:
        html_content += f"""
        <tr>
            <td>{element['name']}</td>
            <td>{element['small']}</td>
            <td>{element['number']}</td>
            <td>{element['molar']}</td>
            <td>{element['electron']}</td>
        </tr>
"""

    html_content += """
    </table>
</body>
</html>
"""

    with open(output_file, 'w') as file:
        file.write(html_content)
    print('The file has been generated')

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        periodic_table(input_file, output_file)
    else:
        print('Usage: python my_sort.py input_file output_file')