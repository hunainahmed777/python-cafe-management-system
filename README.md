# Cafe Ordering System

## Introduction

This project is a simple console-based application for a cafe ordering system. It allows users to log in, view the menu, place orders, display the order, and generate the bill. The system is designed to ensure that only authenticated users can perform certain operations like placing orders and generating bills.

## Features

1. **User Authentication**: Users must log in with a predefined username and password.
2. **Menu Display**: Displays a list of available items and their prices.
3. **Order Placement**: Allows users to place orders by entering the item names.
4. **Order Display**: Displays the list of items ordered by the user.
5. **Bill Generation**: Calculates the total bill based on the items ordered.
6. **Exit Option**: Allows users to exit the application.

## Usage

### 1. Login
The user is prompted to enter a username and password. The correct credentials are:
- **Username**: `hunainahmed`
- **Password**: `okay`

### 2. Display Menu
Once logged in, users can view the menu which displays the items available and their respective prices.

### 3. Place Order
Users can place an order by specifying the number of items they wish to order and then entering the names of the items.

### 4. Display Order
Users can view the items they have ordered.

### 5. Generate Bill
Generates the total bill based on the items ordered.

### 6. Exit
Exits the application.

## Code Structure

### Global Variable
- `order_list`: Stores the list of items ordered by the user.

### Functions

1. **login()**:
   - Prompts for username and password.
   - Authenticates the user.

2. **Menu()**:
   - Displays the menu items and their prices.

3. **place_order()**:
   - Prompts the user to enter the number of items to order.
   - Takes item names as input and stores them in `order_list`.

4. **display_order()**:
   - Displays the items stored in `order_list`.

5. **generate_bill()**:
   - Calculates the total cost of items in `order_list` based on their prices in the menu.
   - Displays the total bill amount.

### Main Program Loop

- Provides a menu of options for the user to select.
- Handles user input and calls appropriate functions.
- Ensures user authentication before allowing access to certain functionalities.

## Example

Below is an example interaction with the application:

```
1) Login
2) Display Menu
3) Place order
4) Display order
5) Bill
6) Exit

/n select: 1
please enter the user name: hunainahmed
please enter the password: okay
Login successful

/n select: 2
{'Coffee': 3.00, 'Espresso': 2.50, 'Latte': 4.00, 'Cappuccino': 4.50, 'Tea': 2.00, 'Herbal Tea': 2.50, 'Hot Chocolate': 3.50, 'Chai Latte': 3.75, 'Iced Coffee': 3.25, 'Iced Tea': 2.75, 'Sandwich': 5.00, 'Panini': 5.50, 'Bagel': 2.00, 'Croissant': 2.75, 'Muffin': 2.50, 'Scone': 3.00, 'Cake': 4.00, 'Cookie': 1.50, 'Brownie': 2.25, 'Pancakes': 5.00}

/n select: 3
how many items do you want to order: 2
enter the item from menu: Coffee
enter the item from menu: Sandwich

/n select: 4
Your order:
Coffee
Sandwich

/n select: 5
your total bill is: 8.0

/n select: 6
exiting the program
```

## Conclusion

This project provides a basic framework for a cafe ordering system with user authentication, order management, and bill generation functionalities. It can be further extended with more features such as user registration, persistent storage, and a graphical user interface (GUI).
