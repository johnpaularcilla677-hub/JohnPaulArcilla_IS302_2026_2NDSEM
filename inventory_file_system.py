JPA_product = input("Enter product name: ")
JPA_price = input("Enter price: ")

with open("inventory.txt", "a") as JPA_file:
    JPA_file.write(JPA_product + "," + JPA_price + "\n")

print("Product saved successfully")

#JohnPaulArcilla