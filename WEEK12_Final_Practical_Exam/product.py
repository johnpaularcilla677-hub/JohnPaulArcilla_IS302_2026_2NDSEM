class Product:
    def __init__(self, JPA_product_id, JPA_name, JPA_price, JPA_quantity):
        self.__JPA_product_id = JPA_product_id
        self.__JPA_name = JPA_name
        self.__JPA_price = JPA_price
        self.__JPA_quantity = JPA_quantity

    def get_product_info(self):
        return f"{self.__JPA_product_id}, {self.__JPA_name}, {self.__JPA_price}, {self.__JPA_quantity}"

    def get_id(self):
        return self.__JPA_product_id

    def update_quantity(self, JPA_quantity):
        self.__JPA_quantity = JPA_quantity

        #JohnPaulArcilla