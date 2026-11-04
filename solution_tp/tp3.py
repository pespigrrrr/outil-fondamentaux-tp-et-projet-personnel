import time 

def evaluer_naif(P, x):
    resultat= 0 
    for i in range(len(P)):      
        resultat+=P[i]*x**i  
    return resultat


def evaluer(P, x):
    resultat= 0
    for coef in P:
        resultat*=x+coef
    return resultat


for degre in (1000, 5000, 20000):
    P=[1]*(degre+1)
    
    debut = time.perf_counter()
    a=evaluer_naif(P,1.0001)
    fin = time.perf_counter()
    temps_evaluer_naif = fin - debut

    debut = time.perf_counter()
    b=evaluer(P,1.0001)
    fin = time.perf_counter()
    temps_evaluer = fin - debut
    

for degre in (200, 400, 800):
    P=[1]*(degre+1)
    
    debut = time.perf_counter()
    a=evaluer_naif(P,3)
    fin = time.perf_counter()
    temps_evaluer_naif = fin - debut

    debut = time.perf_counter()
    b=evaluer(P,3)
    fin = time.perf_counter()
    temps_evaluer = fin - debut
    
    
    
def deriv(P):
    resultat=[]
    for i in range(1,len(P)):
        resultat.append(P[i]*i)
    return resultat

P=[2, 3, 0, 5]
     
     
     
def dichotomie(f,a,b,tolerence=1e-12):
    fa, fb=f(a), f(b)
    if fa==0:
        return a
    if fb==0:
        return b
    if fa*fb > 0:
        raise ValueError("f(a) et f(b) doivent etre de signes opposes")
    while b-a > tolerance:
        milieu=(a + b)/2
        if f(a)*f(milieu) <= 0:
            b=milieu
        else:
            a=milieu
    return (a + b)/2



def f2(x):
   return x**2-2



def newton(P, depart, tolerance, max_ite=100):
    dP = deriver(P)              
    x = depart
    for ite in range(max_ite):
        d = evaluer(dP, x)
        if d == 0:
            raise ZeroDivisionError("Dérivée nulle : la méthode de Newton échoue.")
        x_suivant = x - evaluer(P, x) / d
        if abs(x_suivant - x) < tolerance:
            return x_suivant
        x = x_suivant
    raise ValueError("Pas de convergence après {max_ite} itérations.")
        


def newton_trace(P, depart, tours):
    dP = deriver(P)
    x = float(depart)
    trajet = [x]
    for tours in range(tours):
        pente = evaluer(dP, x)
        if pente == 0:
            break
        x = x - evaluer(P, x) / pente
        trajet.append(x)
    return trajet



def somme(P, Q):
    longueur = max(len(P), len(Q))
    P = P + [0] * (longueur - len(P))
    Q = Q + [0] * (longueur - len(Q))
    return [P[i] + Q[i] for i in range(longueur)]


def produit_poly(P, Q):
    if not P or not Q:
        return []
    R = [0] * (len(P) + len(Q) - 1)
    for i in range(len(P)):
        for j in range(len(Q)):
            R[i + j] += P[i] * Q[j]
    return R


def derivee_avant(f, x, h):
    return (f(x + h) - f(x)) / h



def derivee_centree(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)



def newton_general(f, depart, tolerance=1e-12, tours_max=100, h=1e-6):
    x = float(depart)
    for tour in range(tours_max):
        pente = derivee_centree(f, x, h)
        if pente == 0:
            raise ZeroDivisionError("pente nulle")
        suivant = x - f(x) / pente
        if abs(suivant - x) <= tolerance * max(1.0, abs(suivant)):
            return suivant, tour + 1
        x = suivant
    raise RuntimeError("pas de convergence")