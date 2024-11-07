# Importation
import tkinter as tk

from tkinter import messagebox

import time


# Fonction récursive pour la factorisation en nombres premiers

def facteurs_premiers(n, div=2, limite=None):
    if n == 1:
        return []
    if div > limite:  # Si le diviseur dépasse la limite, on arrête
        return [n]  # Le reste est considéré comme un facteur
    if n % div == 0:
        return [div] + facteurs_premiers(n // div, div, limite)
    return facteurs_premiers(n, div + 1, limite)


# Fonction pour lancer la factorisation et mesurer les performances

def lancer_factorisation():
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
    entry_nombre.delete(0, tk.END)
    label_resultats.config(text="Facteurs premiers :")
    label_temps.config(text="Temps d'exécution :")
    scale_limite.set(100)  # Remettre la limite à 100 par défaut
    var_temps.set(0)  # Désactiver la case de temps


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


# Démarrage de la boucle principale de l'interface

root.mainloop()

