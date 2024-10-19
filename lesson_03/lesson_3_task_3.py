from address import Address
from mailing import Mailing

mail = Mailing(
    Address("100500", "Урюпинск", "Ленина", "2", "31"),
    Address("100600", "Упинск", "Крупской", "5", "13"),
    500,
    123456
    )

print(mail)
