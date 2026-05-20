```python id="z6wk83"
try:
    JPA1 = float(input("Enter first number: "))
    JPA2 = float(input("Enter second number: "))
    
    result = JPA1 / JPA2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid numeric input")
```

#JohnPaulArcilla