num1 = int(input("Enter first number:  "))
num2 = int(input("Enter second number:  "))
search = int(input("Enter number to search:  "))
for i in range(1, num1 + 1):
    for j in range(1, num2 + 1):
        value = i * j
        if value == search:
            print(f"[{value:3}]", end =" ")
        else:
            print(f"{value:5}", end =" ")
    print()
    