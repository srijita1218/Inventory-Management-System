# Inventory-Management-System
The Inventory Management System is a application that allows users to manage inventory items by performing the essential CRUD operations. It provides an interface for users to signup, login, and manage their items based on the user’s needs. It allows users to view all inventory items, create new items, and delete existing items from the inventory.
## Features
- **User Authentication**: Login and signup functionality to secure access.
- **Create Item**: Add new items to the inventory with essential details.
- **Read Item**: View the details of all inventory items or a specific item.
- **Update Item**: Edit the details of an existing inventory item.
- **Delete Item**: Remove items from the inventory.

## Technologies Used
- **Python**: Programming language used to build the application.
- **SQL**: Database management to store inventory data.
- **Tkinter**: Used for creating the GUI.
- **DBeaver**: Database management tool to interact with the database.

## Installation
### Requirements:
- Python 3.x
- A SQL database (MySQL or SQLite recommended)
- Tkinter (Python GUI library)

### Steps to run the project:
1. Clone the repository:
   ```bash
   git clone [https://github.com/srijita1218/Inventory-Management-System]


## Usage
### User Registration:

Open the application and click on the Sign Up button to create a new account.
Enter the required details (username, password) and submit the form.
User Login:

After signing up, log in using the credentials you just created.
Managing Inventory:

Once logged in, you will be able to:
Create New Items: Click on the "Add Item" button to input a new item (name, quantity, price, etc.).
View All Items: See a list of all items in the inventory with their details.
View Specific Item: Click on an item from the list to view its detailed information.
Update Item: Edit details of an existing inventory item.
Delete Item: Remove an item from the inventory when it's no longer required.
Database Schema
The system uses the following basic database schema for storing inventory and user data:

Users Table:
user_id (Primary Key, INT)
username (VARCHAR)
password (VARCHAR)
Inventory Items Table:
item_id (Primary Key, INT)
item_name (VARCHAR)
quantity (INT)
price (FLOAT)
added_by (Foreign Key referencing user_id)

## CONTACT
I am not familiar with creating repositories on GitHub so if there are any issues with the database please feel free to contact me. 
Email : srijita1218@gmail.com
GitHub : https://github.com/srijita1218
