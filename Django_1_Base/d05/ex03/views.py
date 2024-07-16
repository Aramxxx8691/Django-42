from django.shortcuts import render

def ex03(request):
    r = 255 / 50
    # Generate shades for each color
    shades = {
        "noir": ["#{:02x}{:02x}{:02x}".format(int(255 - i * r), int(255 - i * r), int(255 - i * r)) for i in range(51)],
        "rouge": ["#{:02x}{:02x}{:02x}".format(255, int(255 - i * r), int(255 - i * r)) for i in range(51)],
        "bleu": ["#{:02x}{:02x}{:02x}".format(int(255 - i * r), int(255 - i * r), 255) for i in range(51)],
        "vert": ["#{:02x}{:02x}{:02x}".format(int(255 - i * r), 255, int(255 - i * r)) for i in range(51)]
    }

    # Construct table rows and header dynamically
    header_row = '<tr><th>Noir</th><th>Rouge</th><th>Bleu</th><th>Vert</th></tr>'
    table_rows = ''
    for i in range(51):
        table_rows += '<tr>'
        table_rows += f'<td style="background-color: {shades["noir"][i]}"></td>'
        table_rows += f'<td style="background-color: {shades["rouge"][i]}"></td>'
        table_rows += f'<td style="background-color: {shades["bleu"][i]}"></td>'
        table_rows += f'<td style="background-color: {shades["vert"][i]}"></td>'
        table_rows += '</tr>'
    
    context = {
        "header_row": header_row,
        "table_rows": table_rows
    }
    
    return render(request, 'ex03.html', context)
