from functions import *
# product_file = open("products.txt", "r+")
# courier_file = open("couriers.txt", "r+")
with open("products.txt") as product_file:
    product_list = []
    for line in product_file:
        product_list.append(line.rstrip())
with open("couriers.txt") as courier_file:
    courier_list = []
    for line in courier_file:
        courier_list.append(line.rstrip())
# for line in product_file:
#     product_list.append(line.rstrip())
# for line in courier_file:
#     courier_list.append(line.rstrip())
product_menu_message = """
        Press [0] to RETURN to main menu,
        Press [1] to PRINT products list,
        Press [2] to ADD a new product to the list,
        Press [3] to UPDATE an existing product,
        Press [4] to DELETE a product.
        """
courier_menu_message = """
        Press [0] to RETURN to main menu,
        Press [1] to PRINT couriers list,
        Press [2] to ADD a new courier to the list,
        Press [3] to UPDATE an existing courier,
        Press [4] to DELETE a courier.
        """
main_menu_message = """
        Press [1] to enter the PRODUCTS MENU,
        Press [2] to enter the COURIERS MENU,
        Press [0] to EXIT
        """

def main_menu():
    print("WELCOME to Main Menu!")
    first_choice = input(main_menu_message)
    if first_choice == "0":
        # product_file.close()
        # courier_file.close()
        exit()
    elif first_choice == "1":
        second_choice = input(product_menu_message)
        while second_choice != "0":
            product_menu(second_choice)
            second_choice = input(product_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "2":
        second_choice = input(courier_menu_message)
        while second_choice != "0":
            courier_menu(second_choice)
            second_choice = input(courier_menu_message)
        if second_choice == "0":
            main_menu()
    else:
        print("Please enter the correct input!")
        main_menu()


def product_menu(product_menu_choice):
    if product_menu_choice == "1":
        print(f"Products List: {product_list}")
    elif product_menu_choice == "2":
        product_adder(product_list)
    elif product_menu_choice == "3":
        product_updater(product_list)
    elif product_menu_choice == "4":
        product_remover(product_list)
        

# def courier_menu(courier_menu_choice):
#     if courier_menu_choice == "1":
#         print(f"Couriers List: {courier_list}")
#     elif courier_menu_choice == "2":
#         courier_adder(courier_list)
#     elif courier_menu_choice == "3":
#         courier_updater(courier_list)
#     elif courier_menu_choice == "4":
#         courier_remover(courier_list)
    

# def product_adder(input_list):
#     new_item = input("Enter new item's name:\n")
#     input_list.append(new_item)
#     print(f"New Products List: {input_list}")
#     with open("products.txt", "a") as file:
#         file.write(new_item + "\n")


# def courier_adder(input_list):
#     new_item = input("Enter new item's name:\n")
#     input_list.append(new_item)
#     print(f"New Couriers List: {input_list}")
#     with open("couriers.txt", "a") as file:
#         file.write(new_item + "\n")


# def product_updater(input_list):
#     index = 1
#     for item in input_list:
#         print(f"[{index}] : {item} ")
#         index += 1
#     updated_index = int(input("Which item do you want to update? enter the code:\n" ))
#     updated_name = input("Enter the new product's name: \n")
#     old_name = input_list[updated_index - 1]
#     input_list[updated_index - 1] = updated_name
#     print(f"Updated Products List: {input_list}")
#     with open("products.txt", "w") as file:
#         file.seek(0)
#         for i in input_list:
#             if i != old_name:
#                 file.write(i + "\n")
#             elif i == old_name:
#                 file.write(updated_name + "\n")


# def courier_updater(input_list):
#     index = 1
#     for item in input_list:
#         print(f"[{index}] : {item} ")
#         index += 1
#     updated_index = int(input("Which item do you want to update? enter the code:\n" ))
#     updated_name = input("Enter the new courier's name: \n")
#     old_name = input_list[updated_index - 1]
#     input_list[updated_index - 1] = updated_name
#     print(f"Updated Couriers List: {input_list}")
#     with open("couriers.txt", "w") as file:
#         file.seek(0)
#         for i in input_list:
#             if i != old_name:
#                 file.write(i + "\n")
#             elif i == old_name:
#                 file.write(updated_name + "\n")
    
            


# def product_remover(input_list):
#     index = 1
#     for item in input_list:
#         print(f"[{index}] : {item} ")
#         index += 1
#     deleted_index = int(input("Which item do you want to delete? enter the code:\n" ))
#     deleted_name = input_list[deleted_index - 1]
#     input_list.pop(deleted_index - 1)
#     print(f"New Products List: {input_list}")
#     with open("products.txt", "w") as file:
#         file.seek(0)
#         for i in input_list:
#             if i != deleted_name:
#                 file.write(i + "\n")


# def courier_remover(input_list):
#     index = 1
#     for item in input_list:
#         print(f"[{index}] : {item} ")
#         index += 1
#     deleted_index = int(input("Which item do you want to delete? enter the code:\n" ))
#     deleted_name = input_list[deleted_index - 1]
#     input_list.pop(deleted_index - 1)
#     print(f"New Couriers List: {input_list}")
#     with open("couriers.txt", "w") as file:
#         file.seek(0)
#         for i in input_list:
#             if i != deleted_name:
#                 file.write(i + "\n")
      


while True:
    main_menu()