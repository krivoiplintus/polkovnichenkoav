class Address:

    def __init__(self, postnumber, city, streat, house, appart):
        self.postnumber = postnumber
        self.city = city
        self.streat = streat
        self.house = house
        self.appart = appart

    def __str__(self):
        return f"{self.postnumber}, {self.city}, {self.streat}, {self.house}, {self.appart}"
