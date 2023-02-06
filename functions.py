def product_adder(input_list):
    new_item = input("Enter new item's name:\n")
    input_list.append(new_item)
    print(f"New Products List: {input_list}")
    with open("products.txt", "a") as file:
        file.write(new_item + "\n")


def courier_adder(input_list):
    new_item = input("Enter new item's name:\n")
    input_list.append(new_item)
    print(f"New Couriers List: {input_list}")
    with open("couriers.txt", "a") as file:
        file.write(new_item + "\n")


def product_updater(input_list):
    index = 1
    for item in input_list:
        print(f"[{index}] : {item} ")
        index += 1
    updated_index = int(input("Which item do you want to update? enter the code:\n" ))
    updated_name = input("Enter the new product's name: \n")
    old_name = input_list[updated_index - 1]
    input_list[updated_index - 1] = updated_name
    print(f"Updated Products List: {input_list}")
    with open("products.txt", "w") as file:
        file.seek(0)
        for i in input_list:
            if i != old_name:
                file.write(i + "\n")
            elif i == old_name:
                file.write(updated_name + "\n")


def courier_updater(input_list):
    index = 1
    for item in input_list:
        print(f"[{index}] : {item} ")
        index += 1
    updated_index = int(input("Which item do you want to update? enter the code:\n" ))
    updated_name = input("Enter the new courier's name: \n")
    old_name = input_list[updated_index - 1]
    input_list[updated_index - 1] = updated_name
    print(f"Updated Couriers List: {input_list}")
    with open("couriers.txt", "w") as file:
        file.seek(0)
        for i in input_list:
            if i != old_name:
                file.write(i + "\n")
            elif i == old_name:
                file.write(updated_name + "\n")
    
            
def product_remover(input_list):
    index = 1
    for item in input_list:
        print(f"[{index}] : {item} ")
        index += 1
    deleted_index = int(input("Which item do you want to delete? enter the code:\n" ))
    deleted_name = input_list[deleted_index - 1]
    input_list.pop(deleted_index - 1)
    print(f"New Products List: {input_list}")
    with open("products.txt", "w") as file:
        file.seek(0)
        for i in input_list:
            if i != deleted_name:
                file.write(i + "\n")


def courier_remover(input_list):
    index = 1
    for item in input_list:
        print(f"[{index}] : {item} ")
        index += 1
    deleted_index = int(input("Which item do you want to delete? enter the code:\n" ))
    deleted_name = input_list[deleted_index - 1]
    input_list.pop(deleted_index - 1)
    print(f"New Couriers List: {input_list}")
    with open("couriers.txt", "w") as file:
        file.seek(0)
        for i in input_list:
            if i != deleted_name:
                file.write(i + "\n")

# def product_menu(product_menu_choice):
#     if product_menu_choice == "1":
#         with open("products.txt") as product_file:
#             product_list = []
#             for line in product_file:
#                 product_list.append(line.rstrip())
#         print(f"Products List: {product_list}")
#     elif product_menu_choice == "2":
#         product_adder(product_list)
#     elif product_menu_choice == "3":
#         product_updater(product_list)
#     elif product_menu_choice == "4":
#         product_remover(product_list)


def courier_menu(courier_menu_choice, courier_list):
    if courier_menu_choice == "1":
        with open("couriers.txt") as courier_file:
            courier_list = []
            for line in courier_file:
                courier_list.append(line.rstrip())
        print(f"Couriers List: {courier_list}")
    elif courier_menu_choice == "2":
        courier_adder(courier_list)
    elif courier_menu_choice == "3":
        courier_updater(courier_list)
    elif courier_menu_choice == "4":
        courier_remover(courier_list)