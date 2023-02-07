def products_menu(product_menu_choice, product_list):
    if product_menu_choice == "1":
        print(f"Products List: {product_list}")
    elif product_menu_choice == "2":
        product_adder(product_list)
    elif product_menu_choice == "3":
        product_updater(product_list)
    elif product_menu_choice == "4":
        product_remover(product_list)
    else:
        print("Please enter the correct input!")


def couriers_menu(courier_menu_choice, courier_list):
    if courier_menu_choice == "1":
        print(f"Couriers List: {courier_list}")
    elif courier_menu_choice == "2":
        courier_adder(courier_list)
    elif courier_menu_choice == "3":
        courier_updater(courier_list)
    elif courier_menu_choice == "4":
        courier_remover(courier_list)
    else:
        print("Please enter the correct input!")


def orders_menu(order_menu_choice, order_list, courier_list):
    if order_menu_choice == "1":
        print(order_list)
    elif order_menu_choice == "2":
        new_order = {}
        new_order["customer_name"] = input("Please enter customer's name: \n")
        new_order["customer_address"] = input("Please enter the address: \n")
        new_order["customer_phone"] = input("Please enter the phone number: \n")
        print("List of couriers: ")
        index = 1
        for item in courier_list:
            print(f"[{index}] : {item} ")
            index += 1
        new_order["courier"] = int(input("Which courier do you want to assign? enter the code:\n"))
        new_order["status"] = "preparing"
        print(f"New order: {new_order}")
        order_list.append(new_order)
    
    elif order_menu_choice == "3":
        index = 1
        for order in order_list:
            print(f"[{index}] : {order['customer_name']}'s order")
            index += 1
        changed_status_index = int(input("Which order do you want to update the status? Enter the code: "))
        order_list[changed_status_index - 1]["status"] = input("Enter the order's status: ")
        print(order_list)
        

        

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


