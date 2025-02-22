class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def additem(self, quantity):
        self.quantity += quantity
        print(f"{quantity} {self.item_name}(s) added to cart.")

    def removeitem(self, quantity):
        if quantity <= self.quantity:
            print(f"{quantity} {self.item_name}(s) removed from cart.")
            self.quantity -= quantity
        else:
            print(f"Removed {quantity} {self.item_name}(s) from cart.")

    def total_price(self):
        return self.price * self.quantity


cart = []

while True:
    print("__Menu__")
    print("1. View cart")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. Checkout")
    print("5. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        if not cart:
            print("Cart is empty.")
        else:
            for index, item in enumerate(cart, start=1):
                print(f"{index}. {item.item_name} - ${item.price} x {item.quantity} = ${item.total_price()}")

    elif menu == "2":
        item_name = input("Enter item name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        existing_item = next((item for item in cart if item.item_name == item_name), None)
        if existing_item:
            existing_item.additem(quantity)
        else:
            new_item = CartItem(item_name, price, quantity)
            cart.append(new_item)
            print(f"Added {quantity} {item_name}(s) to cart.")
    
    elif menu == "3":
        item_name = input("Enter item name to remove: ")
        quantity = int(input("Enter quantity to remove: "))

        found = False
        for item in cart:
            if item.item_name == item_name:
                item.removeitem(quantity)
                if item.quantity == 0:
                    cart.remove(item)
                found = True
                break

        if not found:
            print("Item not found in cart.")

    elif menu == "4":
        total = sum(item.total_price() for item in cart)
        print(f"Total amount: ${total}")
        cart.clear()
        print("Thank you for shopping!")

    elif menu == "5":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please try again.")