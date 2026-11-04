import math

def lettre_vers_nombre(c):
  return ord(c) - ord("A")


def nombre_vers_lettre(n):
  return chr(n + ord("A"))


def chiffrer(texte, a, b):
  texte_propre = nettoyer(texte)
  chiffre = ""
  for c in texte_propre:
    x = lettre_vers_nombre(c)
    y = (a * x + b) % 26
    chiffre += nombre_vers_lettre(y)
  return chiffre


def inverse_modulaire(a, n):
  for x in range(1, n):
    if (a * x) % n == 1:
      return x
  raise ValueError(f"Aucun inverse modulaire pour {a} modulo {n}")


def dechiffrer(texte, a, b):
  if math.gcd(a, 26) != 1:
    raise ValueError("Clé invalide : a et 26 ne sont pas premiers entre eux.")

  a_inv = inverse_modulaire(a, 26)
  dechiffre = ""
  for c in texte:
    y = lettre_vers_nombre(c)
    x = (a_inv * (y - b)) % 26
    dechiffre += nombre_vers_lettre(x)
  return dechiffre


def toutes_les_clefs(secret):
  resultats = []
  for a in range(1, 26):
    if math.gcd(a, 26) == 1:
      for b in range(26):
        try:
          clair = dechiffrer(secret, a, b)
          resultats.append(((a, b), clair))
        except ValueError:
          continue
  return resultats