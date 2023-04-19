def f(x):
    return ((1-0.001)**x)*5000


x = 0.00
objetivo = 5000
tolerancia = 750

while abs(f(x) - objetivo) > tolerancia:
    x += 0.01
    print(x)

print("El valor aproximado de x es:", round(x, 4))