while True:
    column = int(input("Enter first number:  "))
    row = int(input("Enter second number:  "))
    search = int(input("Enter number to search:  "))
    if column < 1 or row < 1 or search < 1:
        break
    else:
        for i in range(1, column + 1):
            for j in range(1, row + 1):
                value = i * j
                if value == search:
                    print(f"[{value:3}]", end =" ")
                else:
                    print(f"{value:5}", end =" ")
            print()

    