while True:
<<<<<<< HEAD
    column = int(input("Enter first number:  "))
    row = int(input("Enter second number:  "))
    search = int(input("Enter number to search:  "))
    if column < 1 or row < 1 or search < 1:
        break
    else:
        for i in range(1, column + 1):
            for j in range(1, row + 1):
=======
    columns = int(input("Enter number of columns:  "))
    rows = int(input("Enter number of rows:  "))
    search = int(input("Enter number to search:  "))
    if columns < 1 or rows < 1 or search < 1:
        break
    else:
        for i in range(1, columns + 1):
            for j in range(1, rows + 1):
>>>>>>> 8a53438ebf6e05271b233459517363c548c14995
                value = i * j
                if value == search:
                    print(f"[{value:3}]", end =" ")
                else:
                    print(f"{value:5}", end =" ")
            print()

    
