class Product_jpa:
    def __init__(self_jpa, name_jpa, price_jpa, quantity_jpa):
        self_jpa.__name = name_jpa
        self_jpa.__price = price_jpa
        self_jpa.__quantity = quantity_jpa

    def get_product_info_jpa(self_jpa):
        print("Product:", self_jpa.__name)
        print("Price:", self_jpa.__price)
        print("Quantity:", self_jpa.__quantity)

    def update_quantity_jpa(self_jpa, new_quantity_jpa):
        if new_quantity_jpa >= 0:
            self_jpa.__quantity = new_quantity_jpa

    def update_price_jpa(self_jpa, new_price_jpa):
        if new_price_jpa > 0:
            self_jpa.__price = new_price_jpa

# Example usage
product_jpa = Product_jpa("Laptop", 45000, 10)
product_jpa.get_product_info_jpa()
