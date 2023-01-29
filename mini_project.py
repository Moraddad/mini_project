
product_list = ["Pizza", "Pasta", "Cheese Burger", "Coke", "Fanta", "Salad"]

def product_menu(user_choice):
    if user_choice == "0":
        main_menu()
    elif user_choice == "1":
        print(product_list)
    elif user_choice == "2":
        new_prodcut = input("Enter new product's name:\n")
        product_list.append(new_prodcut)
        print(product_list)
    elif user_choice == "3":
        index = 1
        for product in product_list:
            print(f"[{index}] : {product} ")
            index += 1
        updated_index = int(input("Which product do you want to update? enter the code:\n" ))
        updated_name = input("Enter the new name: \n")
        product_list[updated_index - 1] = updated_name
        print(product_list)
    elif user_choice == "4":
        index = 1
        for product in product_list:
            print(f"[{index}] : {product} ")
            index += 1
        updated_index = int(input("Which product do you want to delete? enter the code:\n" ))
        product_list.pop(updated_index - 1)
        print(product_list)



def main_menu():
    print("WELCOME to Main Menu!")
    first_choice = input("Press 1 to see the product menu/ Press 0 to exit.\n")
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
        return second_choice

while True:
    second_choice = main_menu()
    product_menu(second_choice)
    if_continue = input("do you want to continue? Y/N: ")
    if if_continue == "N"  :
        break
    




