inventory_file = "inventory.txt"
total_money_earned=0
def read():
    try:
        with open(inventory_file, "r") as file:
            inventory_data = file.readlines()
            inventory = []
            for line in inventory_data:
                item_id, name, price, quantity = line.strip().split(",")
                inventory.append({
                    'id': item_id,
                    'name': name,
                    'price': float(price),
                    'quantity': int(quantity)
                })
        return inventory
    except FileNotFoundError:
        return []

def write(inventory):
    with open(inventory_file, "w") as file:
        for item in inventory:
            file.write(f"{item['id']},{item['name']},{item['price']},{item['quantity']}\n")

def add_item(item_id, name, each_price, quantity):
    inventory = read()
    new_item = {
        'id': item_id,
        'name': name,
        'price': each_price,
        'quantity': quantity
    }
    inventory.append(new_item)
    write(inventory)
    print(f"Item '{name}' added to inventory.")

def show():
    inventory = read()
    if len(inventory) == 0:
        print("Inventory is empty.")
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        add_item(item_id, name, price, quantity)
        return 
    print("\nCurrent Merchandise Inventory:")
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}")

def update(item_id, name, each_price, quantity):
    inventory = read()
    for item in inventory:
        if item['id'] == item_id:
            item['name'] = name
            item['price'] = each_price
            item['quantity'] = quantity
            write(inventory)
            print(f"Item with ID '{item_id}' updated.")
            return
    print(f"Item with ID '{item_id}' not found in inventory.")

def delete(item_id):
    inventory = read()
    updated_inventory = [item for item in inventory if item['id'] != item_id]
    if len(updated_inventory) < len(inventory):
        write(updated_inventory)
        print(f"Item with ID '{item_id}' deleted from inventory.")
    else:
        print(f"Item with ID '{item_id}' not found in inventory.")

def add_to_inventory():
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    add_item(item_id, name, price, quantity)

def sell_sports_merchandise(item_id, quantity_sold):
    inventory = read()
    global total_money_earned
    for item in inventory:
        if item['id'] == item_id:
            if item['quantity'] >= quantity_sold:
                item['quantity'] -= quantity_sold
                total_money_earned += item['price'] * quantity_sold
                write(inventory)
                print(f"{quantity_sold} units of item '{item_id}' sold.")
            else:
                print(f"Insufficient quantity of item '{item_id}' in inventory.")
            return
    print(f"Item with ID '{item_id}' not found in inventory.")

def track_merchandise_sales():
    inventory = read()
    global total_money_earned
    remaining_items = [(item['id'], item['quantity']) for item in inventory]
    if not remaining_items:
        print("Inventory is empty.")
        return
    print(f"Total Money Earned: {total_money_earned}/-")
    print("Remaining Items in Inventory after selling:")
    for item_id, quantity in remaining_items:
        print(f"ID: {item_id}, Quantity: {quantity}")

while True:
    print("SPORTS MERCHANDISE SALES")
    print("1. INVENTORY")
    print("2. SELLING") 
    print("3. TRACK")
    print("4. EXIT")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("1. List Inventory")
        print("2. Add Item to Inventory")
        print("3. Update Item in Inventory")
        print("4. Delete Item from Inventory")

        choice2 = input("Enter your choice: ")
        if choice2 == "1":
            show()
        elif choice2 == "2":
            add_to_inventory()
        elif choice2 == "3":
            item_id = input("Enter item ID to update: ")
            name = input("Enter updated item name: ")
            price = float(input("Enter updated item price: "))
            quantity = int(input("Enter updated item quantity: "))
            update(item_id, name, price, quantity)
        elif choice2 == "4":
            item_id = input("Enter item ID to delete: ")
            delete(item_id)
    elif choice == 2:
        print("1. Sell Item")
        item_id = input("Enter item ID to sell: ")
        quantity_sold = int(input("Enter quantity to sell: "))
        sell_sports_merchandise(item_id, quantity_sold)
    elif choice == 3:
        track_merchandise_sales()
    elif choice == 4:
        break
