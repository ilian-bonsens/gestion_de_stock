import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="/5$JGF1d:yfTWKyJ",
    database="store"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM product")
results = cursor.fetchall()

fenetre = tk.Tk()
fenetre.geometry("1300x700")

# Créer un Frame pour contenir tous les widgets
frame = tk.Frame(fenetre)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(fenetre, text="Gestion des stocks")
label.pack()

# Ajouter un produit
label = tk.Label(frame, text="Ajouter un produit")
label.pack(pady=5)

def open_add_window():
    # Créer une fenêtre secondaire
    add_window = tk.Toplevel()
    add_window.title("Ajouter un produit")
    add_window.config(width=300, height=300)

    # Créer des champs d'entrée pour chaque information
    label_name = tk.Label(add_window, text="Nom")
    entry_name = tk.Entry(add_window)
    label_name.pack(pady=5)
    entry_name.pack(pady=5)

    label_description = tk.Label(add_window, text="Description")
    entry_description = tk.Entry(add_window)
    label_description.pack(pady=5)
    entry_description.pack(pady=5)

    label_price = tk.Label(add_window, text="Prix")
    entry_price = tk.Entry(add_window)
    label_price.pack(pady=5)
    entry_price.pack(pady=5)

    label_quantity = tk.Label(add_window, text="Quantité")
    entry_quantity = tk.Entry(add_window)
    label_quantity.pack(pady=5)
    entry_quantity.pack(pady=5)

    label_id_category = tk.Label(add_window, text="Id_category")
    entry_id_category = tk.Entry(add_window)
    label_id_category.pack(pady=5)
    entry_id_category.pack(pady=5)

    def add_product():
        # Récupérer les valeurs des champs d'entrée
        product_name = entry_name.get()
        product_description = entry_description.get()
        product_price = entry_price.get()
        product_quantity = entry_quantity.get()
        product_id_category = entry_id_category.get()

        # Insérer les valeurs dans la base de données
        cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)", (product_name, product_description, product_price, product_quantity, product_id_category))
        mydb.commit()

        # Récupérer l'id du produit inséré
        product_id = cursor.lastrowid

        # Afficher le produit ajouté dans le Treeview
        treeview.insert('', 'end', values=(product_id, product_name, product_description, product_price, product_quantity, product_id_category))
        print("Produit ajouté :", product_name)

        # Fermer la fenêtre secondaire
        add_window.destroy()

    # Créer un bouton pour ajouter le produit
    button_add = tk.Button(add_window, text="Ajouter", command=add_product)
    button_add.pack(pady=5)

# Créer un bouton pour ouvrir la fenêtre secondaire
button_open = tk.Button(frame, text="Ouvrir la fenêtre d'ajout", command=open_add_window)
button_open.pack(pady=5)


# Modifier un produit
# Supprimer le champ d'entrée et le label
label = tk.Label(frame, text="Modifier un produit")
# entry = tk.Entry(frame)
label.pack(pady=5)  # Ajouter de l'espace vertical
# entry.pack(pady=5)  # Ajouter de l'espace vertical

def open_modify_window():
    # Créer une fenêtre secondaire
    modify_window = tk.Toplevel()
    modify_window.title("Modifier un produit")
    modify_window.config(width=300, height=300)

    # Créer des champs d'entrée pour chaque information
    label_name = tk.Label(modify_window, text="Nom")
    entry_name = tk.Entry(modify_window)
    label_name.pack(pady=5)
    entry_name.pack(pady=5)

    label_description = tk.Label(modify_window, text="Description")
    entry_description = tk.Entry(modify_window)
    label_description.pack(pady=5)
    entry_description.pack(pady=5)

    label_price = tk.Label(modify_window, text="Prix")
    entry_price = tk.Entry(modify_window)
    label_price.pack(pady=5)
    entry_price.pack(pady=5)

    label_quantity = tk.Label(modify_window, text="Quantité")
    entry_quantity = tk.Entry(modify_window)
    label_quantity.pack(pady=5)
    entry_quantity.pack(pady=5)

    label_id_category = tk.Label(modify_window, text="Id_category")
    entry_id_category = tk.Entry(modify_window)
    label_id_category.pack(pady=5)
    entry_id_category.pack(pady=5)

    def modify_product():
        # Vérifier si la sélection est vide
        selection = treeview.selection()
        if len(selection) == 0:
            # Afficher un message d'erreur
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit dans le Treeview")
            return
        # Récupérer l'id du produit à modifier
        product_id = treeview.item(selection[0])['values'][0]
        # Récupérer les nouvelles valeurs des champs d'entrée
        new_name = entry_name.get()
        new_description = entry_description.get()
        new_price = entry_price.get()
        new_quantity = entry_quantity.get()
        new_id_category = entry_id_category.get()
        # Utiliser les nouvelles valeurs dans la requête SQL
        cursor.execute("UPDATE product SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s WHERE id = %s", (new_name, new_description, new_price, new_quantity, new_id_category, product_id))
        mydb.commit()
        # Mettre à jour les valeurs dans le Treeview
        treeview.item(selection[0], values=(product_id, new_name, new_description, new_price, new_quantity, new_id_category))
        # Remplacer product_name par new_name
        print("Produit modifié :", new_name)

        # Fermer la fenêtre secondaire
        modify_window.destroy()

    # Créer un bouton pour modifier le produit
    button_modify = tk.Button(modify_window, text="Modifier", command=modify_product)
    button_modify.pack(pady=5)

# Créer un bouton pour ouvrir la fenêtre secondaire
button_open = tk.Button(frame, text="Ouvrir la fenêtre de modification", command=open_modify_window)
button_open.pack(pady=5)

# Supprimer un produit
# Supprimer le champ d'entrée et le label

label = tk.Label(frame, text="Supprimer un produit")
# entry = tk.Entry(frame)
label.pack(pady=5)  # Ajouter de l'espace vertical
# entry.pack(pady=5)  # Ajouter de l'espace vertical

def delete_product():
    # Supprimer la ligne qui récupère le nom du produit à supprimer
    # product_name = entry.get()  # Récupérer le nom du produit à supprimer
    # Vérifier si la sélection est vide
    selection = treeview.selection()
    if len(selection) == 0:
        # Afficher un message d'erreur
        messagebox.showerror("Erreur", "Veuillez sélectionner un produit dans le Treeview")
        return
    # Récupérer l'id du produit à supprimer
    product_id = treeview.item(selection[0])['values'][0]
    # Supprimer le produit de la base de données
    cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
    mydb.commit()
    print("Produit supprimé :", product_id)
        # Supprimer le produit du Treeview
    treeview.delete(selection[0])

button = tk.Button(frame, text="Supprimer", command=delete_product)
button.pack(pady=5)


# Créer un Treeview pour afficher les données
treeview = ttk.Treeview(frame, columns=(0, 1, 2, 3, 4, 5), show="headings", height="6")
treeview.pack(pady=5)

# Définir les noms de colonnes pour votre table
treeview.heading(0, text="id")
treeview.heading(1, text="Nom")
treeview.heading(2, text="Description")
treeview.heading(3, text="Prix")
treeview.heading(4, text="Quantité")
treeview.heading(5, text="Id_category")

# Ajouter les données dans le Treeview
for row in results:
    treeview.insert('', 'end', values=row)

fenetre.mainloop()

