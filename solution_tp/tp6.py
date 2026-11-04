import math
import random


def vecteur(A, B):
  return (B[0] - A[0], B[1] - A[1])


def produit_scalaire(u, v):
  return u[0] * v[0] + u[1] * v[1]


def norme(u):
  return math.sqrt(u[0] ** 2 + u[1] ** 2)


def angle(u, v):
  produit = produit_scalaire(u, v)
  nouveaux_denominomateurs = norme(u) * norme(v)
  if nouveaux_denominomateurs == 0:
    return 0.0

  cos_theta = produit / nouveaux_denominomateurs
  cos_theta = max(-1.0, min(1.0, cos_theta))
  return math.degrees(math.acos(cos_theta))


def determinant(u, v):
  return u[0] * v[1] - u[1] * v[0]


def distance_point_droite(P, A, B):
  AB = vecteur(A, B)
  AP = vecteur(A, P)
  return abs(determinant(AB, AP)) / norme(AB)


def orientation(A, B, C):
  AB = vecteur(A, B)
  AC = vecteur(A, C)
  det = determinant(AB, AC)
  if det > 0:
    return 1
  elif det < 0:
    return -1
  else:
    return 0



def aire(polygone):
  n = len(polygone)
  somme = 0
  for i in range(n):
    x1, y1 = polygone[i]
    x2, y2 = polygone[(i + 1) % n]
    somme += x1 * y2 - x2 * y1
  return abs(somme) / 2.0


def se_coupent(A, B, C, D):
  o1 = orientation(A, B, C)
  o2 = orientation(A, B, D)
  o3 = orientation(C, D, A)
  o4 = orientation(C, D, B)
  return (o1 * o2 < 0) and (o3 * o4 < 0)


def intersection(A, B, C, D):
  if not se_coupent(A, B, C, D):
    return None
  AB = vecteur(A, B)
  CD = vecteur(C, D)
  AC = vecteur(A, C)
  det = determinant(AB, CD)
  if det == 0:
    return None
  t = determinant(AC, CD) / det
  return (A[0] + t * AB[0], A[1] + t * AB[1])


def dedans(P, polygone):
  n = len(polygone)
  px, py = P
  intersections = 0
  for i in range(n):
    A = polygone[i]
    B = polygone[(i + 1) % n]
    ax, ay = A
    bx, by = B
    if (ay > py) != (by > py):
      x_intersection = ax + (py - ay) * (bx - ax) / (by - ay)
      if px < x_intersection:
        intersections += 1
  return intersections % 2 == 1



def aire_monte_carlo(polygone, N=200000):
  xs = [p[0] for p in polygone]
  ys = [p[1] for p in polygone]
  xmin, xmax = min(xs), max(xs)
  ymin, ymax = min(ys), max(ys)
  aire_boite = (xmax - xmin) * (ymax - ymin)

  compteur = 0
  for _ in range(N):
    p = (random.uniform(xmin, xmax), random.uniform(ymin, ymax))
    if dedans(p, polygone):
      compteur += 1
  return aire_boite * (compteur / N)


ef zone_de(P, zones):
  for idx, zone in enumerate(zones):
    if dedans(P, zone):
      return idx
  return None