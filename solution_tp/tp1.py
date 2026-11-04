import math


n = 2026
d = 7
quotient = n // d
reste = n % d
print(quotient, reste)                 
print(quotient * d + reste == n)


n = 123456789
print(n % 10)    
print(n // 10)


total = 0.0
for _ in range(1000):
    total = total + 0.1
print(total)         
print(total - 100)



def presque_egaux(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance

print(0.1 + 0.2 == 0.3)                  
print(presque_egaux(0.1 + 0.2, 0.3))     
print(presque_egaux(1.0, 1.5))           
print(math.isclose(0.1 + 0.2, 0.3))     

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
    

n = 100
total = 0
for i in range(1, n + 1):
    total = total + i
print(total)                
print(n * (n + 1) // 2)


def nombre_de_chiffres(n):
    compte = 1
    while n >= 10:
        n = n // 10
        compte = compte + 1
    return compte

print(nombre_de_chiffres(2026))      
print(nombre_de_chiffres(7))         
print(nombre_de_chiffres(0))         
print(nombre_de_chiffres(10 ** 60))


def heron(a, tolerance=1e-12):
    if a < 0:
        raise ValueError("pas de racine carrée réelle pour un nombre négatif")
    if a == 0:
        return 0.0, 0
    x = float(a)
    tours = 0
    while True:
        suivant = 0.5 * (x + a / x)
        tours = tours + 1
        if abs(suivant - x) <= tolerance * abs(suivant):
            return suivant, tours
        x = suivant

racine, tours = heron(2)
print(racine, math.sqrt(2), tours)                  
print(abs(racine - math.sqrt(2)) < 1e-12)


