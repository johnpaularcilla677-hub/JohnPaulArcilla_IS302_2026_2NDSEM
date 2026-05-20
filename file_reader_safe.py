while True:
    try:
        JPA = int(input("Enter a number: "))
        break

    except ValueError:
        print("Invalid input. Please enter a number.")

print("Valid number entered:", JPA)

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File does not exist")

    #JohnPaulArcilla