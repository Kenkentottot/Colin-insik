def conversion(dollar):
    Rupee = dollar * 88.15    
    Pound = dollar * 0.73   
    Yuan = dollar * 7.12    
    return Rupee, Pound, Yuan 

while True:
    user_input = input("Enter dollar ($) (* to exit): ")
    if user_input == "*":
        print("Bye")
        break
    
    dollars = user_input.strip().split('@')
    print("\nDollar ($)\tIndian Ruppe (R)\tBritish (Pound) \t China (Y)")
    
    for dollar in dollars:
        dollar = float(dollar)  
        Rupee, Pound, Yuan = conversion(dollar)
        print(f"{dollar:^12.2f}{Rupee:^12.2f}\t\t{Pound:^12.2f}\t\t{Yuan:^12.2f}")