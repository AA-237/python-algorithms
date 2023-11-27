def cal_volume(size, quantity):
    volume = (size/1000) * quantity
    return volume


def cal_price(volume, package, base_price):
    price = volume * base_price
    if package.lower() == "pickup":
        return price
    else:
        return 1.2 * price
    


def bid(biding_price, price):
    if biding_price < price:
        status = 0
        message = f"Price too low for this quantity"
    else:
        status = 1
        message = f"The approved price is {price}"
        return status, message
    

def main():
    trash_sizes = {"bucket": 10, "trash bag": 27, "wheelbarrow": 80}

    package = input("Select your package (pickup / cleaning and pickup): ")
    trash_size = (input("Select a trash size(bucket / trash bag / wheelbarrow): "))
    trash_quantity = int(input("Input the trash quantity: "))

    if trash_size in trash_sizes:
        trash_type = trash_sizes[trash_size]
    else:
        print(f"Unknow trash size")
        return

    biding_price = float(input("Enter your bidding price: "))



    if trash_quantity > 1:
        volume = cal_volume(trash_size, trash_quantity)
        price = cal_price(volume, package)
        status, message = bid(biding_price, price)
        print(message)
    elif trash_quantity == 1:
        volume = trash_size / 1000
        price = cal_price(volume, package)
        status, message = bid(biding_price, price)
        print(message)
    else:
        print("Please set a trash quantity")

if __name__ == "__main__":
    main()