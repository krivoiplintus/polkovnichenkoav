import math

n = int(input("Введите сторону квадрата: "))


def square(n):
    square = n*n
    return math.ceil(square)


result = square(n)
print(f"Площадь увадрата: {result}")
