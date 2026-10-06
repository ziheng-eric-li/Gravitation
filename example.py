import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numpy import random
from math import *
fig, ax = plt.subplots()


ax.axis('equal')
#ax.set(xlim=[-1, 1000], ylim=[-1,1000])

G = 1 #et pas 6.67430e-11
dt = 0.01 #Pas de temps
n = 5
#positions entre [-5, 5]
#masse entre [1, 4]
def K(m2): #Définition des constantes de la physique
    return G*m2

def d(P1, P2): #Définition de la distance entre deux points
    return sqrt((P1[0] - P2[0])**2 - (P1[1] - P2[1])**2)


masses = np.random.randint(1, 5, n)
pos = np.random.randint(-5, 6, (n, 2))
vitesse = np.zeros((n, 2))
position = np.concatenate(pos, vitesse)


def get_new_position(position, vitesse):
    Pos1 = position[:, np.newaxis, :]
    Pos2 = position[np.newaxis, :, :]
    diff = Pos1 - Pos2
    diff = np.square(diff)
    dist = np.sum(diff, axis = 2)
    dist = np.sqrt(dist)


    Vit1 = positions[1]

    

    return [[Xs[0]+1, Xs[1]-1], [Ys[0]+1, Ys[1]+1]]

scat = ax.scatter(positions[0], positions[1])


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global positions
    positions = get_new_position(positions)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(positions).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100)
plt.show()