import math

A = int(input("Ingrese numero de tres cifras: "))

c3 = A % 10

c2 = int((A % 100) / 10)

c1 = int((A % 1000) / 100)

print(str(c3)+str(c2)+str(c1))