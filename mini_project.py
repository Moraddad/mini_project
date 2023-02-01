product_file = open("products.txt", "r+")
courier_file = open("couriers.txt", "r+")
product_list = []
courier_list = []
for line in product_file.readlines():
    product_list.append(line.rstrip())

for line in courier_file.readlines():
    courier_list.append(line.rstrip())


def product_menu(product_menu_choice):
    if product_menu_choice == "0":
        main_menu()
    elif product_menu_choice == "1":
        print(product_list)
    elif product_menu_choice == "2":
        new_prodcut = input("Enter new product's name:\n")
        product_list.append(new_prodcut)
        print(product_list)
        product_file.write(new_prodcut + "\n")
    elif product_menu_choice == "3":
        index = 1
        for product in product_list:
            print(f"[{index}] : {product} ")
            index += 1
        updated_index = int(input("Which product do you want to update? enter the code:\n" ))
        updated_name = input("Enter the new name: \n")
        product_list[updated_index - 1] = updated_name
        print(product_list)
    elif product_menu_choice == "4":
        index = 1
        for product in product_list:
            print(f"[{index}] : {product} ")
            index += 1
        updated_index = int(input("Which product do you want to delete? enter the code:\n" ))
        product_list.pop(updated_index - 1)
        print(product_list)


def courier_menu(courier_menu_choice):
    if courier_menu_choice == "0":
        main_menu()
    elif courier_menu_choice == "1":
        print(courier_list)
    elif courier_menu_choice == "2":
        new_courier = input("Enter new courier's name:\n")
        courier_list.append(new_courier)
        print(courier_list)
        courier_file.write(new_courier + "\n")
    elif courier_menu_choice == "3":
        index = 1
        for courier in courier_list:
            print(f"[{index}] : {courier} ")
            index += 1
        updated_index = int(input("Which courier do you want to update? enter the code:\n" ))
        updated_name = input("Enter the new name: \n")
        courier_list[updated_index - 1] = updated_name
        print(courier_list)
    elif courier_menu_choice == "4":
        index = 1
        for courier in courier_list:
            print(f"[{index}] : {courier} ")
            index += 1
        updated_index = int(input("Which courier do you want to delete? enter the code:\n" ))
        courier_list.pop(updated_index - 1)
        print(courier_list)
        

def main_menu():
    print("WELCOME to Main Menu!")
    first_choice = input("Press 1 to see the product menu/Press 2 to enter the couriers menu/ Press 0 to exit.\n")
    if first_choice == "0":
        exit()
    elif first_choice == "1":
        second_choice = input(
        """
        Press 0 to return to main menu,
        Press 1 to see product list,
        Press 2 to add a new product to the list,
        Press 3 to update an existing product,
        Press 4 to delete a product.\n
        """
        )
        product_menu(second_choice)
    elif first_choice == "2":
        second_choice = input(
        """
        Press 0 to return to main menu,
        Press 1 to see courier list,
        Press 2 to add a new courier to the list,
        Press 3 to update an existing courier,
        Press 4 to delete a courier.\n
        """
        )
        courier_menu(second_choice)


while True:
    main_menu()
    should_continue = input("do you want to continue? Y/N: ")
    if should_continue != "Y":
        product_file.close()
        break
