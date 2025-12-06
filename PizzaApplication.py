# Pizza Project
print("Welcome to the Pizza Ordering System!")

pizza_size = ""
base_price = 0
pep_price = 0
cheese_price = 0
total_price = 0

# Size Selection
while True:
    size = input("Choose your pizza size: Small (S), Medium (M), or Large (L)? ")
    size1 = size.upper()
    if size1 == "S":
        pizza_size = "small"
        base_price = 15
        break
    elif size1 == "M":
        pizza_size = "medium"
        base_price = 20
        break
    elif size1 == "L":
        pizza_size = "large"
        base_price = 25
        break
    else:
        print("Invalid response. Please choose a size between Small (S), Medium (M), or Large (L).")

# Add Pepperoni 
while True:
    add_pep = input("Would you like to add pepperoni? (Y/N) ")
    add_pep1 = add_pep.upper()
    if add_pep1 == "Y":
        if size1 == "S":
            pep_price += 2
            break
        elif size1 == "M" or size1 == "L": 
            pep_price += 3
            break
    elif add_pep1 == "N":
        pep_price += 0
        break
    else:
        print("Invalid input. Please enter Y or N.")

# Extra Cheese
while True:
    extra_cheese = input("Would you like to add extra cheese? (Y/N) ")
    extra_cheese1 = extra_cheese.upper()
    if extra_cheese1 == "Y":
        cheese_price += 1
        break
    elif extra_cheese1 == "N":
        cheese_price += 0
        break
    else:
        print("Invalid input. Please enter Y or N.")

total_price = base_price + pep_price + cheese_price
print("-----ORDER SUMMARY-----")
print("Pizza Size: " + str(size1))
print("Base Price: $" + str(base_price))
if add_pep1 == "Y":
    print("Pepperoni Added: $" + str(pep_price))
if extra_cheese1 == "Y":
    print("Extra Cheese Added: $" + str(cheese_price))
print("-----------------------")
print("Total Bill: $" + str(total_price))
print("Thank you for your order!")

