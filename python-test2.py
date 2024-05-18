import random

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price

    def update_quantity(self, new_quantity, increment=True):
        if increment:
            self.quantity += new_quantity
        else:
            self.quantity -= new_quantity
            if self.quantity < 0:
                self.quantity = 0

class InventoryManagement:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name].update_quantity(quantity)
        else:
            self.items[name] = InventoryItem(name, quantity, price)

    def delete_item(self, name):
        if name in self.items:
            del self.items[name]

    def update_item_price(self, name, new_price):
        if name in self.items:
            self.items[name].update_price(new_price)

    def update_item_quantity(self, name, quantity, increment=True):
        if name in self.items:
            self.items[name].update_quantity(quantity, increment)

    def get_inventory(self):
        return {name: (item.quantity, item.price) for name, item in self.items.items()}

    def load_items(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                name, quantity, price = line.split(',')
                self.add_item(name, int(quantity), float(price))

    def save_items(self, filename):
        with open(filename, "w") as file:
            for name, item in self.items.items():
                file.write(f"{name},{item.quantity},{item.price}\n")

def simulate_operations():
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
