def create_xml(data):
    # surname, name, phone_number, time =
    xml = '<xml>\n'
    xml += f'    <surname units = "">{data["surname"]}</surname>\n'
    xml += f'    <name units = "">{data["name"]}</name>\n'
    xml += f'    <phone_number units = "">{data["phone_number"]}</phone_number>\n'
    xml += f'    <time units = "">{data["time"]}</time>\n'
    xml += f'</xml>\n'

    with open('data.xml', 'a', encoding='utf-8') as page:
        page.write(xml)

    return xml
