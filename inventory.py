def Inventory():
    items = []
    item_prices = {}

    print("===== INVENTORY MENU =====")
    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] Exit")

    while True:
        try:
            choice = int(input("Choice: "))

            if choice == 1:
                item_name = input("Enter item name: ")

                if not item_name.strip():
                    print("Name can't be empty")
                    continue
                
                if item_name in items:
                    print(f"Item {item_name} already exists")
                    continue

                try:
                    price = float(input("Enter price: "))

                    if price < 0:
                        print("Price must be positive")
                        continue
                    items.append(item_name)
                    item_prices[item_name] = price

                    print("Item added successfully!")
                except ValueError:
                    print("Invalid! Enter a number for price")
                    continue
            
            elif choice == 2:
                item_name = input("Enter item name to update: ")

                if item_name not in items:
                    print("Item not found in the inventory.")
                    continue

                try:
                    new_price = float(input("Enter new price: "))

                    if new_price < 0:
                        print("Price must be positive")
                        continue

                    item_prices[item_name] = new_price
                    print("Price updated successfully!")
                except ValueError:
                    print("Invalid! Enter a number for price")
                    continue
            elif choice == 3:
                print("Exiting system...")
                break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again")
                    

if __name__ == "__main__":
    Inventory()
