while True:
    try:
        JPA = int(input("Enter a number: "))
        break

    except ValueError:
        print("Invalid input. Please enter a number.")

print("Valid number entered:", JPA)

#JohnPaulArcilla