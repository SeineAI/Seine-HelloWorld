import random

class InventoryItem:
    """Represents an item in inventory with name, quantity, and price."""

    def __init__(self, name, quantity, price):
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_price(self, new_price):
        """Update the price of the item if the new price is positive."""
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price

    def update_quantity(self, new_quantity, increment=True):
        """Update the item's quantity, either incrementing or decrementing."""
        if increment:
            self.quantity += new_quantity
        else:
            self.quantity -= new_quantity
        if self.quantity < 0:
            self.quantity = 0

class InventoryManagement:
    """Manages the inventory operations for an inventory system."""

    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        """Add an item to the inventory or update its quantity."""
        if name in self.items:
            self.items[name].update_quantity(quantity)
        else:
            self.items[name] = InventoryItem(name, quantity, price)

    def delete_item(self, name):
        """Delete an item from inventory by its name."""
        if name in self.items:
            del self.items[name]

    def update_item_price(self, name, new_price):
        """Update the price of an item in the inventory."""
        if name in self.items:
            self.items[name].update_price(new_price)

    def update_item_quantity(self, name, quantity, increment=True):
        """Update the quantity of an item in the inventory."""
        if name in self.items:
            self.items[name].update_quantity(quantity, increment)

    def get_inventory(self):
        """Return the current inventory as a dictionary."""
        return {name: (item.quantity, item.price) for name, item in self.items.items()}

    def load_items(self, filename):
        """Load items from a file into the inventory."""
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
            for line in lines:
                name, quantity, price = line.strip().split(',')
                self.add_item(name, int(quantity), float(price))
        except FileNotFoundError:
            print(f"Error: The file {filename} does not exist.")
        except ValueError:
            print("Error: Incorrect file format.")

    def save_items(self, filename):
        """Save the current inventory items to a file."""
        with open(filename, "w") as file:
            for name, item in self.items.items():
                file.write(f"{name},{item.quantity},{item.price}\n")

def simulate_operations():
    """Simulate inventory operations to demonstrate the system functionality."""
    inventory = InventoryManagement()
    inventory.add_item("Apple", 100, 0.5)
    inventory.add_item("Banana", 150, 0.3)
    inventory.add_item("Carrot", 200, 0.2)

    inventory.update_item_price("Banana", 0.25)
    inventory.update_item_quantity("Apple", 50, False)
    inventory.update_item_quantity("Carrot", 50)

    inventory.delete_item("Banana")

    inventory.load_items("inventory.txt")
    inventory.save_items("inventory_updated.txt")

    print(inventory.get_inventory())

simulate_operations()
