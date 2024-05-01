import control
import numpy as np
import matplotlib.pyplot as plt

# Inserisco la costante di tempo

tau = input("Inserire la costante di tempo tau: ")
tau = float(tau)

k = input("Ampiezza del gradino di tensione: ")
k = float(k)

# Definisco numeratore e denominatore della F.D.T. inserendo i coefficienti dei polinomi al numeratore e al denominatore:
# numeratore = 1
# denominatore = tau*s + 1

Numeratore = [1]
Denominatore = [tau, 1]

# Definisco ora la F.D.T.

F = control.tf(Numeratore, Denominatore)
print('F(s) =', F)

# Calcolo la risposta al gradino unitario u(t) in un intervallo di tempo coerente con la costante di tempo del sistema:

start = 0
stop = 5*tau
punti_di_calcolo = 1000

t = np.linspace(start, stop, punti_di_calcolo)
t, y = control.step_response(k*F, t)

# disegno la risposta nel tempo y(t)

plt.plot(t, y)
plt.title("Risposta al gradino del circuito RC:")
plt.grid()
plt.show()

# Calcolo i poli del sistema

p = control.poles(F)
print('poli', p)



