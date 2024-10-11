from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+79001111111"),
    Smartphone("Simens", "E35", "+79002222222"),
    Smartphone("HTC", "One", "+790033333333"),
    Smartphone("iPhone", "14Pro", "+79004444444"),
    Smartphone("Honor", "10i", "+79005555555")
]

for smartphone in catalog:
    print(f"{smartphone.brent} - {smartphone.model}. {smartphone.number}")
