shopping_list = []

while True:
    print("Enter the name of the product" + str(len(shopping_list) + 1) + " (or press Enter to stop.):")
    product = input()
    if product == "":
        break
    shopping_list = shopping_list + [product]

print("The item names are: " + str(shopping_list))
