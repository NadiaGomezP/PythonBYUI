names = []
prices = []

action = ""

print()

print("Welcome to the Shopping Cart Program!")

while action != "6":
    print("\nPlease select one of the following:\n"
    "1. Add item\n"
    "2. View cart\n"
    "3. Remove item\n"
    "4. Compute total\n"
    "5. Higher price\n"
    "6. Quit\n")
    action = input("Please enter an action: ")

    if action == "1":
        add_item = input("What item would you like to add? ")
        add_price = float(input(f"What is the price of '{add_item.capitalize()}'? "))
        print(f"'{add_item.capitalize()}' has been added to the cart.")
        names.append(add_item)
        prices.append(add_price)
    
    elif action == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(names)):
            add_item = names[i]
            add_price = prices[i]
            print(f"{i+1}. {add_item.capitalize()} - ${add_price:.2f}")
    
    elif action == "3":
        index = int(input("Which item would you like to remove? "))
        if (index - 1) > i:
            print("Sorry, that is not a valid item number.")
        else:
            names.pop(index - 1)
            prices.pop(index - 1)
            print("Item removed.")
            
    elif action == "4":
        print(f"The total price of the items in the shopping cart is ${sum(prices):.2f}")

    elif action == "5":
        print(f"The higher price you have on your cart is $ {max(prices):.2f}")
    
    elif action == "6":
        print("Thank You. Goodbye\n") 
        
    else:
        print("Sorry. You have to choose a number between 1 to 5")






            


