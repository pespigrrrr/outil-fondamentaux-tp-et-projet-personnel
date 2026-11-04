import matplotlib.pyplot as plt
import numpy as np


def evaluer(P, x):
  """Évalue le polynôme P au point x."""
  res = 0
  for coef in reversed(P):
    res = res * x + coef
  return res


def deriver(P):
  """Renvoie le polynôme dérivé de P."""
  return [i * P[i] for i in range(1, len(P))]


def newton_trace(P, depart, max_etapes=5):
  """Calcule la liste des approximations successives (trajet) de Newton[cite: 3]."""
  dP = deriver(P)
  x = float(depart)
  trajet = [x]
  for _ in range(max_etapes):
    pente = evaluer(dP, x)
    if pente == 0:
      break
    x_suivant = x - evaluer(P, x) / pente
    trajet.append(x_suivant)
    x = x_suivant
  return trajet


def tracer_convergence_newton(P, intervalle, depart, max_etapes=5):
  """Trace la courbe de P et dessine les tangentes successives de Newton."""
  a, b = intervalle
  x = np.linspace(a, b, 400)
  y = [evaluer(P, xi) for xi in x]

  plt.figure(figsize=(9, 7))
  plt.plot(x, y, label="P(x)", color="royalblue", linewidth=2)
  plt.axhline(0, color="black", linewidth=1, linestyle="--")

  # Trajectoire de Newton
  trajet = newton_trace(P, depart, max_etapes)

  # Tracé géométrique des étapes de Newton
  for i in range(len(trajet) - 1):
    x_actuel = trajet[i]
    y_actuel = evaluer(P, x_actuel)
    x_suivant = trajet[i + 1]

    # Point sur la courbe (x_n, P(x_n))
    plt.scatter([x_actuel], [y_actuel], color="crimson", zorder=5)

    # Ligne pointillée verticale pour relier l'axe des abscisses au point sur la courbe
    plt.plot([x_actuel, x_actuel], [0, y_actuel], color="gray", linestyle=":", alpha=0.6,)

    # Tangente menant de (x_actuel, y_actuel) vers l'axe des abscisses en (x_suivant, 0)
    plt.plot([x_actuel, x_suivant], [y_actuel, 0], color="orange", linestyle="--", linewidth=1.5,)

  # Affichage du dernier point approché
  x_final = trajet[-1]
  plt.scatter([x_final], [evaluer(P, x_final)], color="forestgreen", zorder=5, label="Approximation finale",)

  plt.title("Visualisation géométrique des itérations de la méthode de Newton")
  plt.xlabel("x")
  plt.ylabel("P(x)")
  plt.grid(True, linestyle=":", alpha=0.7)
  plt.legend()
  plt.show()