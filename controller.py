from create_csv import create_csv as c_csv
from xml_creator import create_xml as cx
from html_creater import create_html as c_html
from read_file import read_file as rf
from search_contact import search_contact as sc
from view import add_contact as add_c
from view import select_action as sa
from view import search_contact as sc_view


def work_with_book():
    select_action = sa()
    if select_action == 1:
        add_contact = add_c()
        c_csv(add_contact)
        cx(add_contact)
        values = rf()
        c_html(values)
    else:
        search_contact = sc_view()
        print('Результат запроса -> ')
        print(sc(search_contact))
