
# Getting data from textboxes
from pyscript import display, document

def get_name(e):
    document.getElementById('div1').innerHTML = ''

    book_members = ['athena alfaro', 'bela allas', 'lindsay esguerra']

    first_name = document.getElementById('fname').value.lower().strip()
    last_name = document.getElementById('lname').value.lower().strip()
    full_name = first_name + ' ' + last_name

    name_checker = full_name in book_members # True(1) or False(0)

    display_message = (f'Sorry {first_name.title()} {last_name.title()}, your name is not on the list.',f'{first_name.title()} {last_name.title()} is part of the Book Club.')
    display(display_message[name_checker], target='div1')
