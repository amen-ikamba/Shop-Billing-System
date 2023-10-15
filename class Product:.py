class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self):
        name = input("Enter your name: ")
        product_name = input("Enter the name of the product: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))

        product = Product(product_name, price, quantity)
        self.products.append((name, product))

    def show_products(self):
        print("Product\t\tQuantity\tAmount")
        print("-----------------------------------")
        for name, product in self.products:
            amount = product.price * product.quantity
            print(f"{product.name}\t\t{product.quantity}\t\t{amount}")

    def generate_bill(self):
        total_amount = 0
        print("------- Bill -------")
        print("Name:", self.products[0][0])  # Assume the first product belongs to the client
        print("Product\t\tQuantity\tAmount")
        print("-----------------------------------")
        for name, product in self.products:
            amount = product.price * product.quantity
            total_amount += amount
            print(f"{product.name}\t\t{product.quantity}\t\t{amount}")
        print("-----------------------------------")
        print(f"Total Amount:\t\t\t{total_amount}")


# Usage example:
shop = Shop()

# Add products
add_more = True
while add_more:
    shop.add_product()
    choice = input("Do you want to add more products? (yes/no): ")
    if choice.lower() != "yes":
        add_more = False

# Show product list
shop.show_products()

# Generate bill
shop.generate_bill()

# Shop Billing Management System

products = []  # List to store product details


def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))

    products.append({'name': name, 'quantity': quantity})


def show_products():
    print("Product List:")
    print("-----------------------------")
    for product in products:
        print(f"Name: {product['name']}")
        print(f"Quantity: {product['quantity']}")
        print("-----------------------------")


def calculate_amount(product):
    price_per_unit = 10  # Set the price per unit of the product (can be modified as needed)
    return product['quantity'] * price_per_unit


def generate_bill(client_name):
    total_amount = 0

    print("Bill:")
    print("-----------------------------")
    print(f"Client Name: {client_name}")
    print("-----------------------------")
    for product in products:
        amount = calculate_amount(product)
        total_amount += amount
        print(f"Product: {product['name']}")
        print(f"Quantity: {product['quantity']}")
        print(f"Amount: {amount}")
        print("-----------------------------")

    print(f"Total Amount: {total_amount}")
    print("-----------------------------")


# Main program
client_name = input("Enter client name: ")

while True:
    print("1. Add Product")
    print("2. Show Products")
    print("3. Generate Bill")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        show_products()
    elif choice == '3':
        generate_bill(client_name)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# Shop Billing Management System

products = {
    'Dairy': ['Milk', 'Cheese', 'Yogurt', 'Butter', 'Cream'],
    'Meat/Poultry': ['Chicken', 'Beef', 'Pork', 'Lamb', 'Turkey'],
    'Seafood': ['Fish', 'Shrimp', 'Salmon', 'Tuna', 'Crab'],
    'Produce': ['Apples', 'Bananas', 'Oranges', 'Lettuce', 'Tomatoes', 'Carrots'],
    'Grains/Staples': ['Rice', 'Pasta', 'Bread', 'Flour', 'Oats'],
    'Breakfast/Cereals': ['Cereal', 'Oatmeal', 'Granola', 'Pancake Mix', 'Syrup'],
    'Snacks': ['Chips', 'Cookies', 'Crackers', 'Nuts', 'Popcorn'],
    'Beverages': ['Soda', 'Juice', 'Water', 'Coffee', 'Tea'],
    'Frozen Foods': ['Pizza', 'Ice Cream', 'Vegetables', 'Frozen Meals', 'Frozen Desserts'],
    'Canned Goods': ['Soups', 'Beans', 'Vegetables', 'Fruits', 'Tuna'],
    'Baking': ['Flour', 'Sugar', 'Baking Powder', 'Baking Soda', 'Vanilla Extract'],
    'Condiments/Sauces': ['Ketchup', 'Mustard', 'Mayonnaise', 'BBQ Sauce', 'Soy Sauce'],
    'Cleaning Supplies': ['Detergent', 'Dish Soap', 'Paper Towels', 'All-purpose Cleaner', 'Trash Bags'],
    'Personal Care': ['Shampoo', 'Toothpaste', 'Soap', 'Body Wash', 'Deodorant']
}


def display_product_groups():
    print("Product Groups:")
    print("------------------------------------")
    for group in products:
        print(group)
    print("------------------------------------")


def select_products():
    selected_products = []
    print("Available Product Groups:")
    print("------------------------------------")
    for group in products:
        print(group)
    print("------------------------------------")

    while True:
        group = input("Enter the name of the product group (or 'done' to finish): ")
        if group == 'done':
            break
        elif group not in products:
            print("Invalid product group. Please try again.")
            continue

        print(f"Available Products in {group}:")
        print("------------------------------------")
        for product in products[group]:
            print(product)
        print("------------------------------------")

        while True:
            product = input("Enter the name of the product (or 'done' to finish): ")
            if product == 'done':
                break
            elif product not in products[group]:
                print("Invalid product. Please try again.")
                continue

            quantity = int(input("Enter the quantity: "))
            selected_products.append({'name': product, 'quantity': quantity})
            print(f"{product} added to the cart with a quantity of {quantity}.")

    return selected_products


def calculate_amount(product):
    return product['quantity'] * 10  # Assuming each product costs $10


def generate_bill(client_name, products_bought):
    total_amount = 0

product_groups = {
    "Dairy": [
        {"name": "Milk", "price": 700, "quantity_measure": "liters"},
        {"name": "Cheese", "price": 1000, "quantity_measure": "grams"},
        {"name": "Yogurt", "price": 1000, "quantity_measure": "grams"}
    ],
    "Meat/Poultry": [
        {"name": "Chicken", "price": 15000, "quantity_measure": "kilograms"},
        {"name": "Beef", "price": 8000, "quantity_measure": "kilograms"},
        {"name": "Pork", "price": 6000, "quantity_measure": "kilograms"}
    ],
    "Produce": [
        {"name": "Apples", "price": 500, "quantity_measure": "pieces"},
        {"name": "Bananas", "price": 200, "quantity_measure": "pieces"},
        {"name": "Lettuce", "price": 1500, "quantity_measure": "pieces"}
    ]
}

discounts = [
    {"condition": 10000, "discount": 0.1},  # 10% discount for total amount >= 10000 FRW
    {"condition": 20000, "discount": 0.2},  # 20% discount for total amount >= 20000 FRW
    {"condition": 50000, "discount": 0.3}   # 30% discount for total amount >= 50000 FRW
]

membership_rewards = [
    {"condition": 5000, "reward": 500},     # 500 FRW reward for total amount >= 5000 FRW
    {"condition": 10000, "reward": 1000},   # 1000 FRW reward for total amount >= 10000 FRW
    {"condition": 20000, "reward": 2000}    # 2000 FRW reward for total amount >= 20000 FRW
]


def display_product_groups():
    print("\nAll Product Groups:")
    print("------------------------------------")
    for group in product_groups:
        print(group)
    print("------------------------------------")


def select_products():
    selected_products = []
    print("\nAvailable Product Groups In our stock:")
    print("------------------------------------")
    for group in product_groups:
        print(group)
    print("------------------------------------")

    while True:
        product_group = input("\nEnter the product group (or 'done' to get your Invoice): ")
        if product_group == 'done':
            break
        elif product_group not in product_groups:
            print("Invalid product group. Please try again.")
            continue

        print(f"Available Products in {product_group}:")
        print("------------------------------------")
        for index, product in enumerate(product_groups[product_group], start=1):
            print(f"{index}. {product['name']} - FRW{product['price']} per {product['quantity_measure']} ({get_abbreviation(product['quantity_measure'])})")
        print("------------------------------------")

        while True:
            selection = input("\nEnter the number of the product (or 'done' to go back to groups): ")
            if selection == 'done':
                break
            elif not selection.isdigit() or int(selection) < 1 or int(selection) > len(product_groups[product_group]):
                print("Invalid selection. Please try again.")
                continue

            product_index = int(selection) - 1
            quantity = int(input(f"\nEnter the quantity in {product_groups[product_group][product_index]['quantity_measure']} ({get_abbreviation(product_groups[product_group][product_index]['quantity_measure'])}): "))
            product = product_groups[product_group][product_index]
            selected_products.append({
                'name': product['name'],
                'quantity': quantity,
                'price': product['price'],
                'quantity_measure': product['quantity_measure']
            })
            print(f"\n{product['name']} added to the cart with a quantity of {quantity} {get_abbreviation(product['quantity_measure'])}.")

    return selected_products


def get_abbreviation(quantity_measure):
    abbreviations = {
        "liters": "L",
        "grams": "g",
        "kilograms": "kg",
        "pieces": "pcs"
    }
    return abbreviations.get(quantity_measure, "")


def calculate_amount(product):
    return product['quantity'] * product['price']


def apply_promotion(total_amount):
    for discount in discounts:
        if total_amount >= discount['condition']:
            return total_amount * (1 - discount['discount'])
    return total_amount


def apply_membership_reward(total_amount):
    for reward in membership_rewards:
        if total_amount >= reward['condition']:
            return total_amount - reward['reward']
    return total_amount


def generate_bill(customer_name, bought_products):
    total_amount = 0

    print("\n-------------------")
    print("      INVOICE      ")
    print("----------------------")
    print(f"Customer Name: Mr/Mrs {customer_name}")
    print("--------------------------------------")
    print("Products Bought:")
    print("----------------------------------------------------")
    print("Product Name   Quantity/Measurement   Amount (FRW)")
    print("----------------------------------------------------")

    for product in bought_products:
        amount = calculate_amount(product)
        total_amount += amount
        print(f"{product['name']:14} {product['quantity']:9} {get_abbreviation(product['quantity_measure']):13} {amount:13.2f}")

    print("----------------------------------------------------")
    print(f"Total Amount: {total_amount} FRW")
    print("---------------------------------")

    # Apply promotions and membership rewards
    discounted_amount = apply_promotion(total_amount)
    final_amount = apply_membership_reward(discounted_amount)

    print(f"\nDiscounted Amount: {discounted_amount} FRW")
    print(f"Final Amount: {final_amount} FRW")

    print(" \n----------- For Support Contact Us --------")
    print("  Tel:+250788888888 / +250781290000   ")
    print("  Email:Billingsystmsupport.info.com     ")
    print("------------------------------------------")
    print("\n----------------------")
    print("     Print Invoice      ")
    print("------------------------")
    print("\n--------------Thanks for Shopping with us ----------------------")


print("-------------------Welcome To Our Billing System -------------------")
customer_name = input("\nPlease Enter your Name: ")

display_product_groups()
selected_products = select_products()

generate_bill(customer_name, selected_products)

