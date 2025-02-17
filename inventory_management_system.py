import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this if your MySQL user is different
    password="dombby12##",  # Add your MySQL password here
    database="inventory_db"
)
cursor = db.cursor()

# Main Application Class
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        # Set the window size (width x height)
        self.root.geometry("800x600")  # This makes the window 800x600 pixels in size
        self.root.config(bg="#f0f8ff")  # Light pastel blue background

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.create_login_screen()

    # ------------------------ LOGIN SCREEN ------------------------ #
    def create_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Adding padding and spacing for a more spacious layout
        tk.Label(self.root, text="Username:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Entry(self.root, textvariable=self.username_var, font=("Arial", 14), bg="#e6f7ff").pack(pady=10)
        
        tk.Label(self.root, text="Password:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Entry(self.root, textvariable=self.password_var, show="*", font=("Arial", 14), bg="#e6f7ff").pack(pady=10)
        
        tk.Button(self.root, text="Login", command=self.login, font=("Arial", 14), bg="#80c7e0", fg="white").pack(pady=20)
        tk.Button(self.root, text="Signup", command=self.create_signup_screen, font=("Arial", 14), bg="#80c7e0", fg="white").pack(pady=10)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user:
            stored_password = user[2]  # password is the 3rd column in the table

            # Check if the password matches the stored password
            if stored_password == password:
                messagebox.showinfo("Success", "Login successful!")
                self.create_dashboard()
            else:
                messagebox.showerror("Error", "Invalid username or password")
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # ------------------------ SIGNUP SCREEN ------------------------ #
    def create_signup_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Username:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Entry(self.root, textvariable=self.username_var, font=("Arial", 14), bg="#e6f7ff").pack(pady=10)
        
        tk.Label(self.root, text="Password:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Entry(self.root, textvariable=self.password_var, show="*", font=("Arial", 14), bg="#e6f7ff").pack(pady=10)
        
        tk.Button(self.root, text="Signup", command=self.signup, font=("Arial", 14), bg="#80c7e0", fg="white").pack(pady=20)
        tk.Button(self.root, text="Back to Login", command=self.create_login_screen, font=("Arial", 14), bg="#80c7e0", fg="white").pack(pady=10)

    def signup(self):
        username = self.username_var.get()
        password = self.password_var.get()

        try:
            # Insert the user with the plain password into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            messagebox.showinfo("Success", "Signup successful!")
            self.create_login_screen()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

    # ------------------------ DASHBOARD ------------------------ #
    def create_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Inventory Management Dashboard", font=("Arial", 18), bg="#f0f8ff").pack(pady=20)
        tk.Button(self.root, text="Add Item", command=self.create_add_item_screen, font=("Arial", 14), bg="#80c7e0", fg="white", width=20).pack(pady=10)
        tk.Button(self.root, text="View Items", command=self.create_view_items_screen, font=("Arial", 14), bg="#80c7e0", fg="white", width=20).pack(pady=10)
        
        # Modify this button to log out
        tk.Button(self.root, text="Logout", command=self.logout, font=("Arial", 14), bg="#ffadad", fg="white", width=20).pack(pady=20)

    # ------------------------ LOGOUT ------------------------ #
    def logout(self):
        # Clear the username and password fields
        self.username_var.set("")
        self.password_var.set("")
        
        # Go back to the login screen
        self.create_login_screen()

    # ------------------------ ADD ITEM ------------------------ #
    def create_add_item_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.item_name_var = tk.StringVar()
        self.quantity_var = tk.StringVar()
        self.price_var = tk.StringVar()

        tk.Label(self.root, text="Item Name:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Entry(self.root, textvariable=self.item_name_var, font=("Arial", 14), bg="#e6f7ff").pack(pady=10)
        
        tk.Label(self.root, text="Quantity:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Entry(self.root, textvariable=self.quantity_var, font=("Arial", 14), bg="#e6f7ff").pack(pady=10)
        
        tk.Label(self.root, text="Price:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Entry(self.root, textvariable=self.price_var, font=("Arial", 14), bg="#e6f7ff").pack(pady=10)
        
        tk.Button(self.root, text="Add Item", command=self.add_item, font=("Arial", 14), bg="#80c7e0", fg="white", width=20).pack(pady=20)
        tk.Button(self.root, text="Back to Dashboard", command=self.create_dashboard, font=("Arial", 14), bg="#ffadad", fg="white", width=20).pack(pady=10)

    def add_item(self):
        name = self.item_name_var.get()
        quantity = self.quantity_var.get()
        price = self.price_var.get()

        cursor.execute("INSERT INTO inventory (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
        db.commit()
        messagebox.showinfo("Success", "Item added successfully!")
        self.create_dashboard()

    # ------------------------ VIEW ITEMS ------------------------ #
    def create_view_items_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Inventory Items", font=("Arial", 18), bg="#f0f8ff").pack(pady=20)
        columns = ("ID", "Name", "Quantity", "Price")
        tree = ttk.Treeview(self.root, columns=columns, show="headings", height=10)

        for col in columns:
            tree.heading(col, text=col)

        # Fetch items from the database
        cursor.execute("SELECT * FROM inventory")
        items = cursor.fetchall()

        # Insert each item into the Treeview
        for item in items:
            tree.insert("", tk.END, values=item)

        tree.pack(pady=20)

        # Delete button for selected item
        def on_delete_item():
            selected_item = tree.selection()  # Get the selected item
            if selected_item:
                item_id = tree.item(selected_item)['values'][0]  # The ID of the item
                self.delete_item(item_id)  # Delete the item using its ID
            else:
                messagebox.showerror("Error", "Please select an item to delete")

        tk.Button(self.root, text="Delete Selected Item", command=on_delete_item, font=("Arial", 14), bg="#ffadad", fg="white", width=20).pack(pady=10)
        tk.Button(self.root, text="Back to Dashboard", command=self.create_dashboard, font=("Arial", 14), bg="#ffadad", fg="white", width=20).pack(pady=10)

    # ------------------------ DELETE ITEM ------------------------ #
    def delete_item(self, item_id):
        # Deleting the item from the database
        cursor.execute("DELETE FROM inventory WHERE id=%s", (item_id,))
        db.commit()
        messagebox.showinfo("Success", "Item deleted successfully!")
        self.create_view_items_screen()  # Refresh the item list after deletion

# ------------------------ RUN APPLICATION ------------------------ #
root = tk.Tk()
app = InventoryApp(root)
root.mainloop()

root.protocol("WM_DELETE_WINDOW", lambda: (db.close(), root.destroy()))
