# Personal Finance Manager - Frontend Only (Tkinter)
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# Global transaction list
transactions = []

# Function to add transaction
def add_transaction():
    amount = amount_entry.get()
    category = category_var.get()
    
    if not amount or not category:
        messagebox.showerror("Error", "Please enter all fields!")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    transactions.append((amount, category))
    transaction_list.insert("", "end", values=(amount, category))
    amount_entry.delete(0, tk.END)

# Function to generate pie chart
def show_chart():
    if not transactions:
        messagebox.showinfo("Info", "No transactions available for chart.")
        return

    categories = {}
    for amount, category in transactions:
        categories[category] = categories.get(category, 0) + amount
    
    labels = categories.keys()
    sizes = categories.values()
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Spending by Category")
    plt.show()

# Create main window
root = tk.Tk()
root.title("Personal Finance Manager")

# Input section
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Category:").grid(row=1, column=0, padx=10, pady=5)
category_var = tk.StringVar()
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=["Food", "Rent", "Transport", "Entertainment", "Other"])
category_dropdown.grid(row=1, column=1, padx=10, pady=5)
category_dropdown.current(0)

tk.Button(root, text="Add Transaction", command=add_transaction).grid(row=2, column=0, columnspan=2, pady=10)

# Transaction list
tk.Label(root, text="Transactions:").grid(row=3, column=0, columnspan=2, pady=5)
transaction_list = ttk.Treeview(root, columns=("Amount", "Category"), show="headings")
transaction_list.heading("Amount", text="Amount")
transaction_list.heading("Category", text="Category")
transaction_list.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Chart button
tk.Button(root, text="Show Chart", command=show_chart).grid(row=5, column=0, columnspan=2, pady=10)

# Run app
root.mainloop()
