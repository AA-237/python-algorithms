def calculate_volume(size, quantity):
    volume = (size/1000) * quantity
    return volume

    # calculating price from volume, package and base_price
def calculate_price(volume, package, base_price):
    price = volume * base_price
    if package.lower() == "pickup":
        return price
    else:
        return 1.2 * price

def bid(biding_price, price):
    if biding_price < price:
        status = "Rejected"
        message = "Price too low."
    else:
        status = "Approved"
        message = f"The approved price is {biding_price}"
    return status, message

def main():
    # Dictinary tfor each trash size, its volume and base price
    trash_sizes = {"bucket": (10, 100), "trash bag": (27, 300), "wheelbarrow": (80, 500)}  

    # input values
    package = input("Select a package (pickup / cleaning & pickup): ")
    storage_type = input("Select a trash storage type (bucket / trash bag / wheelbarrow): ")
    trash_quantity = int(input("Select the trash quantity: "))

    if storage_type in trash_sizes:
        trash_size, base_price = trash_sizes[storage_type]  
    else:
        print(f"Unknown trash type: {storage_type}")
        return

    volume = calculate_volume(trash_size, trash_quantity)
    price = calculate_price(volume, package, base_price)
    print(f"Suggested price is {int(price)}")

    biding_price = float(input("Enter your bidding price: "))  

    status, message = bid(biding_price, price)
    print(message)

if __name__ == "__main__":
    main()
