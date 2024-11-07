# Importation

import time

import tkinter as tk

from tkinter import messagebox


# Fonction de décompostion en facteurs premiers

def facteurs_premiers(n :int, div=2) ->int:
    """
        Fonction récursive renvoyant la décompositons en nombres premiers à
        multiplier pour reconsistuer un entier n

        Input : n = nombre à décomposer

        Output : décomposition en nombres premiers
    """
    # Condition d'arrêt : Si n = 1, on a fini la factorisation
    if n == 1:

        return []

    # Si n est divisible par le diviseur actuel
    if n % div == 0:

        return [div] + facteurs_premiers(n // div, div)

    # Sinon on augmente le diviseur et continue la récursion
    return facteurs_premiers(n, div + 1)



# Fonction appelée lors de l'appui sur le bouton de factorisation

def lancer_factorisation():

    try:


        # Récupérer le nombre entré par l'utilisateur
        nombre = int(entry_nombre.get())

        if nombre <= 0:

            raise ValueError("Le nombre doit être positif et supérieur à 0.")


        # Mesurer le temps de début
        start_time = time.time()


        # Calculer les facteurs premiers
        resultats = facteurs_premiers(nombre)


        # Calculer le temps pris
        temps_execution = time.time() - start_time


        # Afficher les résultats et le temps dans les widgets dédiés
        label_resultats.config(text=f"Facteurs premiers : {resultats}")
        label_temps.config(text=f"Temps d'exécution : {temps_execution:.6f} secondes")

    except ValueError as e:

        messagebox.showerror("Erreur", f"Entrée invalide : {e}")


# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Facteurisation en Nombres Premiers")


# Champs de saisie pour le nombre
label_instruction = tk.Label(root, text="Entrez un nombre entier à factoriser :")
label_instruction.pack(pady=5)

entry_nombre = tk.Entry(root, width=20)
entry_nombre.pack(pady=5)


# Bouton pour lancer la factorisation
bouton_factoriser = tk.Button(root, text="Lancer la factorisation", command=lancer_factorisation)
bouton_factoriser.pack(pady=10)


# Labels pour afficher les résultats
label_resultats = tk.Label(root, text="Facteurs premiers :")
label_resultats.pack(pady=5)

label_temps = tk.Label(root, text="Temps d'exécution :")
label_temps.pack(pady=5)


# Lancer la boucle de l'interface
root.mainloop()
