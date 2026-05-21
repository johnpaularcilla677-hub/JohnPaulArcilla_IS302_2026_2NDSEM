from product import Product
from inventory_manager import add_product, view_products


def search_product():

    JPA_product_id = input("Enter Product ID: ")

    try:
        with open("products.txt", "r") as file:
            for line in file:
                JPA_data = line.strip().split(",")

                if JPA_data[0] == JPA_product_id:
                    print("Product Found:", line)
                    return

        print("Product not found")

    except FileNotFoundError:
        print("Inventory file not found")


while True:

    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("1 Add Product")
    print("2 View Products")
    print("3 Search Product")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        try:
            JPA_product_id = input("Enter Product ID: ")
            JPA_name = input("Enter Product Name: ")
            JPA_price = float(input("Enter Price: "))
            JPA_quantity = int(input("Enter Quantity: "))

            JPA = Product(JPA_product_id, JPA_name, JPA_price, JPA_quantity)

            add_product(JPA)

            print("Product added successfully")

        except ValueError:
            print("Invalid input")

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        break

    else:
        print("Invalid option")

        #JohnPaulArcilla