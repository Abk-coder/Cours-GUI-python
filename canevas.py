# Petit exercice utilisant la bibliothèque tkinter
from tkinter import *
from random import randrange
# --- définition des fonctions gestionnaires d'évènements


def drawline():
    "Tracé d'une ligne dans le canevas"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
    # modification des coordonnées pour la ligne suivante:
    y2, y1 = y2 + 10, y1-10


def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal = ['puple', 'cyan', 'maroon', 'green',
           'red', 'blue', 'orange', 'yellow']
    c = randrange(1, 4)  # génère un nombre aléatoire de 1 à 3
    coul = pal[c]


# ---------- Programme principal --------------
# Les variables suivantes seront utulisées de manière global:
x1, y1, x2, y2 = 10, 190, 190, 10  # coordonnées de la ligne
coul = 'dark green'  # couleur de la ligne

# Création du widget principal ("maître"):
fen1 = Tk()
# Création des widgets "esclaves"
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)
bout1 = Button(fen1, text='Quitter', command=fen1.quit)
bout1.pack(side=BOTTOM)
bout2 = Button(fen1, text='Tracer une ligne', command=drawline)
bout2.pack()
bout3 = Button(fen1, text='autre couleur', command=changecolor)
bout3.pack()
fen1.mainloop()  # démarrage du réceptionnaire d'évènements
fen1.destroy()  # destruction(ferméture) de la fenêtre
