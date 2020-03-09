import babel.dates as bd
import babel.numbers as bn
import gettext

from datetime import date
from datetime import date, datetime, time

gettext.install('cli', localedir='locale')

if __name__ == '__main__':
    today = date.today()
    print(bd.format_date(today,"full"))

    number = 240000000000.32212
    print(bn.format_number(number))
    
    name = input(_('Input your name: '))
    print(_(f'Hello {name}')
