import math

x1, y1 = [float(w) for w in input().split()]
x2, y2 = [float(w) for w in input().split()]

distancia = (x2 - x1)**2 + (y2 - y1)**2

raiz = math.sqrt(distancia)

print(f"{raiz:.4f}")