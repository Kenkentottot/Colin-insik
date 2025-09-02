while True:
    columns = int(input("Enter number of columns:  "))
    rows = int(input("Enter number of rows:  "))
    search = int(input("Enter number to search:  "))
    if columns < 1 or rows < 1 or search < 1:
        break
    else:
        for i in range(1, columns + 1):
            for j in range(1, rows + 1):
                value = i * j
                if value == search:
                    print(f"[{value:3}]", end =" ")
                else:
                    print(f"{value:5}", end =" ")
            print()

    
