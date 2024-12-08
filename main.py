# Importation
import tkinter as tk

from tkinter import messagebox

import time

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

# Fonction récursive pour la factorisation en nombres premiers

def facteurs_premiers(n, div=2, limite=None):
    
    """
    Effectue la factorisation en nombres premiers d'un entier donné.

    Arguments :
        n (int): Nombre à factoriser.
        div (int): Diviseur initial pour la recherche des facteurs (par défaut 2).
        limite (int, optional): Valeur maximale que le diviseur peut atteindre.

    Return :
        list: Liste des facteurs premiers de n.

    Exemple:
        >>> facteurs_premiers(100, div=2, limite=10)
        [2, 2, 5, 5]
    """
   
    if n == 1:
        return []
    if div > limite:  # Si le diviseur dépasse la limite, on arrête
        return [n]  # Le reste est considéré comme un facteur
    if n % div == 0:
        return [div] + facteurs_premiers(n // div, div, limite)
    return facteurs_premiers(n, div + 1, limite)


# Fonction pour lancer la factorisation et mesurer les performances

def lancer_factorisation():
    
    """
    Lance la factorisation du nombre entré par l'utilisateur et affiche les résultats.

    - Récupère le nombre et la limite maximale de diviseur depuis les widgets.
    - Mesure le temps d'exécution si l'option est activée.
    - Affiche les résultats et le temps d'exécution dans l'interface.

    Exceptions:
        ValueError: Si l'utilisateur entre un nombre invalide ou négatif.

    Return :
        None
    """

    try:
        # Récupérer le nombre entré par l'utilisateur
        nombre = int(entry_nombre.get())
        limite = int(scale_limite.get())
        
        if nombre <= 0:
            raise ValueError("Le nombre doit être positif et supérieur à 0.")
        
        # Mesurer le temps de début si l'option est activée
        start_time = time.time() if var_temps.get() else None
        
        # Calculer les facteurs premiers
        resultats = facteurs_premiers(nombre, div=2, limite=limite)
        
        # Calculer le temps pris si l'option est activée
        temps_execution = (time.time() - start_time) if start_time else None
        
        # Afficher les résultats dans les widgets dédiés
        label_resultats.config(text=f"Facteurs premiers : {resultats}")
        
        # Afficher le temps d'exécution si la case est cochée
        if var_temps.get() and temps_execution is not None:
            label_temps.config(text=f"Temps d'exécution : {temps_execution:.6f} secondes")
        else:
            label_temps.config(text="Temps d'exécution : désactivé")
    
    except ValueError as e:
        messagebox.showerror("Erreur", f"Entrée invalide : {e}")


# Fonction pour réinitialiser les champs

def reset():

    """
    Réinitialise tous les champs et widgets de l'interface.

    - Efface le champ d'entrée du nombre.
    - Réinitialise les labels de résultats et de temps.
    - Réinitialise la limite du diviseur à sa valeur par défaut.
    - Désactive l'option de mesure du temps.

    Return :
        None
    """

    entry_nombre.delete(0, tk.END)
    label_resultats.config(text="Facteurs premiers :")
    label_temps.config(text="Temps d'exécution :")
    scale_limite.set(100)  # Remettre la limite à 100 par défaut
    var_temps.set(0)  # Désactiver la case de temps

# Fonction pour tracer la courbe de complexité
def tracer_complexite():

    """
    Génère et affiche la courbe de complexité théorique \( O(\sqrt{n}) \).

    - Utilise une gamme de nombres (valeurs_n) comme taille d'entrée.
    - Calcule \( O(\sqrt{n}) \) pour chaque valeur de n.
    - Trace la courbe à l'aide de Matplotlib.

    Return :
        None
    """

    # Générer une gamme de nombres pour représenter la taille du nombre à factoriser
    valeurs_n = [10,100,1000,10000]  # Plage de nombres, ajustable
    
    # Calculer la complexité théorique O(√n) pour chaque valeur de n
    complexite = [np.sqrt(n) for n in valeurs_n]
    
    # Effacer le graphique précédent et tracer la nouvelle courbe
    ax.clear()
    ax.plot(valeurs_n, complexite, color='purple', label="Complexité O(√n)")
    ax.set_title("Complexité théorique de la factorisation récursive")
    ax.set_xlabel("Valeur de n")
    ax.set_ylabel("Complexité O(√n)")
    ax.legend()
    graphique.draw()



# Création de la fenêtre Tkinter

root = tk.Tk()
root.title("Facteurisation en Nombres Premiers")


# Widgets de l'interface graphique


# 1. Label pour les instructions

label_instruction = tk.Label(root, text="Entrez un nombre entier à factoriser :")
label_instruction.pack(pady=5)

# 2. Entry pour entrer le nombre à factoriser

entry_nombre = tk.Entry(root, width=20)
entry_nombre.pack(pady=5)

# 3. Scale pour définir la limite maximale du diviseur

label_limite = tk.Label(root, text="Limite maximale pour le diviseur :")
label_limite.pack(pady=5)
scale_limite = tk.Scale(root, from_=2, to=500, orient=tk.HORIZONTAL)
scale_limite.set(100)  # Valeur par défaut de la limite
scale_limite.pack(pady=5)

# 4. Checkbutton pour activer/désactiver l'affichage du temps d'exécution

var_temps = tk.IntVar()
check_temps = tk.Checkbutton(root, text="Afficher le temps d'exécution", variable=var_temps)
check_temps.pack(pady=5)

# 5. Boutons pour lancer la factorisation et réinitialiser

bouton_factoriser = tk.Button(root, text="Lancer la factorisation", command=lancer_factorisation)
bouton_factoriser.pack(pady=10)

bouton_reset = tk.Button(root, text="Réinitialiser", command=reset)
bouton_reset.pack(pady=5)

# Labels pour afficher les résultats et le temps d'exécution

label_resultats = tk.Label(root, text="Facteurs premiers :")
label_resultats.pack(pady=5)

label_temps = tk.Label(root, text="Temps d'exécution :")
label_temps.pack(pady=5)

# Bouton pour afficher la courbe de complexité
bouton_complexite = tk.Button(root, text="Afficher la courbe de complexité", command=tracer_complexite)
bouton_complexite.pack()

# Graphique de la complexité avec Matplotlib
fig, ax = plt.subplots()
graphique = FigureCanvasTkAgg(fig, master=root)
graphique.get_tk_widget().pack()




# Démarrage de la boucle principale de l'interface

root.mainloop()

