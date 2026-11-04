import time

def diviseurs(n):
    resultat = []
    for d in range(1, n + 1):
        if n % d == 0:
            resultat.append(d)
    return resultat

print(diviseurs(28))
print(diviseurs(97))


def pgcd_naif(a, b):
    meilleur = 1
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            meilleur = d
    return meilleur

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(pgcd_naif(1071, 462), pgcd(1071, 462))


def est_premier_naif(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def est_premier(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

print(est_premier_naif(97), est_premier_naif(91))                 
print(est_premier(97), est_premier(91), est_premier(2), est_premier(1))



def duree(fonction, argument):
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter() - debut



def crible(limite):
    est_premier_tab = [True] * (limite + 1)
    est_premier_tab[0] = False
    if limite >= 1:
        est_premier_tab[1] = False
    d = 2
    while d * d <= limite:
        if est_premier_tab[d]:
            for multiple in range(d * d, limite + 1, d):
                est_premier_tab[multiple] = False
        d += 1
    return [n for n in range(limite + 1) if est_premier_tab[n]]



def facteurs(n):
    resultat = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n = n // d
        d += 1
    if n > 1:
        resultat.append(n)
    return resultat

f = facteurs(360)
produit = 1
for x in f:
    produit *= x
print(f, produit)        
print(facteurs(14)) 



def fibonacci_recursif(n):
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)



def fibonacci(n):
    precedent, courant = 0, 1
    for _ in range(n):
        precedent, courant = courant, precedent + courant
    return precedent


def euclide_etendu(a, b):
    if b == 0:
        return a, 1, 0
    g, u, v = euclide_etendu(b, a % b)
    return g, v, u - (a // b) * v

g, u, v = euclide_etendu(1071, 462)
print(g, u, v, 1071 * u + 462 * v == g)    
print(euclide_etendu(5, 26))



def puissance_mod_naive(a, e, n):
    resultat = 1
    for _ in range(e):
        resultat = resultat * a % n
    return resultat



def puissance_mod(a, e, n):
    resultat = 1
    a = a % n
    while e > 0:
        if e % 2 == 1:
            resultat = resultat * a % n
        a = a * a % n
        e = e // 2
    return resultat

a, e, n = 7, 10**7, 1_000_003
print(puissance_mod(a, e, n), pow(a, e, n))