class Book:
    def __init__(self, title, author, ISBN, price, stock):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price
        self.stock = stock

    def update_stock(self, amount):
        if amount < 0:
            print("Error: Stock amount cannot be negative.")
        else:
            self.stock += amount

    def sell_book(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"{quantity} copies of {self.title} sold.")
        else:
            print("Not enough stock to sell")

    def set_price(self, new_price):
        if new_price < 0:
            print("Error: New price should not be negative.")
        else:
            self.price = new_price

class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.ISBN == book.ISBN:
                print("Book already exists in inventory.")
                return
        self.books.append(book)

    def remove_book(self, ISBN):
        self.books = [book for book in self.books if book.ISBN != ISBN]

    def find_book_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def find_book_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        return found_books

    def update_stock(self, ISBN, amount):
        found = False
        for book in self.books:
            if book.ISBN == ISBN:
                book.update_stock(amount)
                found = True
        if not found:
            print("Book not found in inventory.")

    def sell_book(self, ISBN, quantity):
        for book in self.books:
            if book.ISBN == ISBN:
                book.sell_book(quantity)
                return
        print("Book not found in inventory.")

    def list_inventory(self):
        if len(self.books) == 0:
            print("Inventory is empty.")
        else:
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, Price: {book.price}, Stock: {book.stock}")

# Sample usage
inventory = Inventory()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789", 20.5, 50)
book2 = Book("1984", "George Orwell", "987654321", 15.0, 100)

inventory.add_book(book1)
inventory.add_book(book2)

book3 = Book("To Kill a Mockingbird", "Harper Lee", "123123123", -5, 30)
inventory.add_book(book3)

inventory.sell_book("123456789", 3)
inventory.update_stock("987654321", 20)

# Print inventory
inventory.list_inventory()

