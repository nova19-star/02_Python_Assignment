# Write a python program to if a number is positive or negative or zero using ternary operator

num = float(input("Enter a number: "))
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print("The number is:",result)
