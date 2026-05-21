
    JPA = int(input("Enter a number: "))
    result = 100 / JPA
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
```

#JohnPaulArcilla