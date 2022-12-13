def create_html(data):
    html = '<!DOCTYPE html>\n'
    html += '<html>\n'
    html += '<head>\n'
    html += '<meta charset="UTF-8">\n'
    html += '<title>Справочник</title>\n'
    html += '<link rel="stylesheet" type="text/css" href="style.css">\n'
    html += '</head>\n'
    html += '<body>\n'
    html += '   <table class="table">\n'
    html += '       <tr>\n'

    for value in data[0].split(','):
        html += f'           <th>{value.capitalize()}</th>\n'

    html += '       </tr>\n'

    for row in data[1:]:
        if row != '':
            html += '       <tr>\n'

            for td in row.split(','):
                html += f'          <td>{td}</td>\n'

            html += '       </tr>\n'

    html += '   </table>\n'
    html += '</body>\n'
    html += '</html>\n'

    with open('index.html', 'w', encoding='utf-8') as page:
        page.write(html)
