# Pizza Project
print("Welcome to the Pizza Ordering System!")

size = input("Choose your pizza size: Small (S), Medium (M), or Large (L)? ")
add_pep = input("Would you like to add pepperoni? (Y/N) ")
extra_cheese = input("Would you like to add extra cheese? (Y/N) ")

size1 = size.upper()
pizza_size = ""
base_price = 0
pep_price = 0
cheese_price = 0
total_price = 0
add_pep1 = add_pep.upper()
extra_cheese1 = extra_cheese.upper()

# Size Selection
if size1 == "S":
    pizza_size = "small"
    base_price = 15
elif size1 == "M":
    pizza_size = "medium"
    base_price = 20
elif size1 == "L":
    pizza_size = "large"
    base_price = 25
else:
    size = input("Invalid response. Please choose a size between Small (S), Medium (M), or Large (L)." )
# Add Pepperoni 
if add_pep1 == "Y":
    if size1 == "S":
        pep_price += 2
    elif size1 == "M" or size1 == "L": 
        pep_price += 3
else:
    add_pep = input("Invalid input. Please enter Y or N. ")
# Extra Cheese
if extra_cheese1 == "Y":
    cheese_price += 1
elif extra_cheese1 == "N":
    cheese_price += 0 
else:
    extra_cheese = input("Invalid input. Please enter Y or N. ")

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

