Ukayukay = {0: "underwear",
            1: "tank top",
            2: "jacket"}
Ukayukay_len = len(Ukayukay)
print(f"Matrix size: {Ukayukay_len}")
for key,value in Ukayukay.items():
    print("Shopping items",key,":",value)
print()
print(f"You have {Ukayukay_len} items in the cart")
while(True):
    user = input("What would you like to do [C]hange items [R]emove [D]isplay  S[earch] ?").upper()
    match user:
        case "C":
            user_input = input("Enter key to search: ")
            if user_input.isdigit():
                user_input = int(user_input)
                if user_input in Ukayukay.keys():
                    print(f"Found {Ukayukay.get(user_input)}")
                    Ukayukay.pop(user_input)
                    new_value = input("Enter value: ").lower()
                    Ukayukay.update({user_input:new_value})
                else:
                    print("Im sorry not in the cart")
            else:
                print("Error try to input a key")
        case "R":
            user_input = input("Enter key to remove: ")
            if user_input.isdigit():
                user_input = int(user_input)
                print(f"The key {user_input} with value {Ukayukay.get(user_input)} has been deleted")
                Ukayukay.pop(user_input)
            else:
                print("Key not found please input a key")
        case "D":
            print("Key \t Value")
            for key,value in Ukayukay.items():
                print(f"{key}\t{value}")
        case "S":
            user_input = input("Enter item to search: ")
            if user_input.isdigit():
                user_input = int(user_input)
                value = Ukayukay.get(user_input)
                if user_input in Ukayukay.keys():
                    print(f"Found {Ukayukay.get(user_input)} item")
                else:
                    print("Im sorry not in cart")
            elif user_input.lower() in Ukayukay.values():
                    print(f"Found {user_input.lower()} item")
            else:
                print("Im sorry not in cart")
        case "*":
            print("Bye!")
            break
        case _:
            print("Error try again")
                            










          