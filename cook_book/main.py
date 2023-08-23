import tkinter as tk
from generator import generate_recipes

import random 

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Náhodný výběr jídla")
root.geometry("400x300")

# Barva pozadí
root.configure(bg="#E6F2F5")  # Lehce modrá barva

# Vytvoření popisku
label = tk.Label(root, text="Vítejte v kuchařce", font=("Helvetica", 25, "bold"), bg="white")
label.pack(pady=(30, 10))  # Odsazení z vrchu

# Funkce pro zobrazení náhodného receptu
def show_random_recipe():
    random_recipe = random.choice(generate_recipes())
    recipe_name.config(text=random_recipe["name"])
    ingredients.config(text=", ".join(random_recipe["ingredients"]))


# Vytvoření tlačítka
button = tk.Button(root, text="Vyber náhodný recept", font=("Helvetica", 15), command=show_random_recipe, bg="#FF5733")
button.pack(pady= 15) # Odsazení od nápisu "Vítejte v kuchařce"

# Vytvoření popisku pro zobrazení názvu receptu a ingrediencí
recipe_name = tk.Label(root, text="", font=("Helvetica", 16))
recipe_name.pack()
ingredients = tk.Label(root, text="", font=("Helvetica", 14))
ingredients.pack(pady=(10, 0))

# Načtení seznamu receptů
recipes = generate_recipes()

# Spuštění hlavní smyčky pro zobrazení GUI
root.mainloop()