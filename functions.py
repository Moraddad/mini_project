import json
from messages import *

def products_menu(product_menu_choice, p_list):
    if product_menu_choice == "1":
        print(f"Products List: {p_list}")
    elif product_menu_choice == "2":
        add_item(p_list, "product")
    elif product_menu_choice == "3":
        update_item(p_list, "product")
    elif product_menu_choice == "4":
        remove_item(p_list, "product")
    else:
        print(wrong_input)


def couriers_menu(courier_menu_choice, c_list):
    if courier_menu_choice == "1":
        print(f"Couriers List: {c_list}")
    elif courier_menu_choice == "2":
        add_item(c_list, "courier")
    elif courier_menu_choice == "3":
        update_item(c_list, "courier")
    elif courier_menu_choice == "4":
        remove_item(c_list, "courier")
    else:
        print(wrong_input)


def orders_menu(order_menu_choice, order_list, c_list):
    if order_menu_choice == "1":
        print("Orders List: ")
        for order in order_list:
            print(order)
    elif order_menu_choice == "2":
        add_order(order_list, c_list)
    elif order_menu_choice == "3":
        change_order_status(order_list)
    elif order_menu_choice == "4":
        update_order(order_list)
    elif order_menu_choice == "5":
        remove_order(order_list)
    else:
        print(wrong_input)
          
def add_item(input_list, item_type):
    new_item = input(f"Enter new {item_type}'s name:\n")
    input_list.append(new_item)
    print(f"New {item_type}s list: {input_list}")
    with open(f"{item_type}.json", "w") as file:
        json.dump(input_list, file)


def update_item(input_list,item_type):
    index = 1
    for item in input_list:
        print(f"[{index}] : {item} ")
        index += 1
    updated_index = int(input(f"Which {item_type} do you want to update? enter the code:\n" ))
    updated_name = input(f"Enter the new {item_type}'s name: \n")
    input_list[updated_index - 1] = updated_name
    print(f"Updated {item_type}s list: {input_list}")
    with open(f"{item_type}.json", "w") as file:
        json.dump(input_list, file)
       

def remove_item(input_list, item_type):
    index = 1
    for item in input_list:
        print(f"[{index}] : {item} ")
        index += 1
    deleted_index = int(input(f"Which {item_type} do you want to delete? enter the code:\n" ))
    input_list.pop(deleted_index - 1)
    print(f"New {item_type}s list: {input_list}")
    with open(f"{item_type}.json", "w") as file:
        json.dump(input_list, file)


def add_order(input_list, c_list):
    new_order = {}
    new_order["customer_name"] = input("Please enter customer's name: \n")
    new_order["customer_address"] = input("Please enter the address: \n")
    new_order["customer_phone"] = input("Please enter the phone number: \n")
    print("List of couriers: ")
    index = 1
    for item in c_list:
        print(f"[{index}] : {item} ")
        index += 1
    new_order["courier"] = int(input("Which courier do you want to assign? enter the code:\n"))
    new_order["status"] = "preparing"
    print(f"New order: {new_order}")
    input_list.append(new_order)
    with open("orders.json", "w") as file:
        json.dump(input_list, file, indent=4)


def update_order(input_list):
    keys = ["customer_name", "customer_address", "customer_phone", "courier", "status"]
    key_index = 1
    order_index = 1
    for order in input_list:
        print(f"[{order_index}] : {order['customer_name']}'s order")
        order_index += 1
    updated_index = int(input("Which order do you want to update? Enter the code: "))
    for key in input_list[updated_index - 1]:
        if key == "status" or key == "courier":
            continue
        print(f"[{key_index}] : {key}")
        key_index += 1
    which_key_to_update = keys[int(input("Which key do you want to update? Enter the code: ")) - 1]
    new_value = input("Enter the new value: ")
    if new_value != "":
        input_list[updated_index -1][which_key_to_update] = new_value
    with open("orders.json", "w") as file:
        json.dump(input_list, file, indent=4)
    
            
def change_order_status(input_list):
    statuses = ["Preparing", "Sent", "Delivered"]
    order_index = 1
    status_index = 1
    for order in input_list:
        print(f"[{order_index}] : {order['customer_name']}'s order")
        order_index += 1
    changed_status_index = int(input("Which order do you want to update the status? Enter the code: "))
    for status in statuses:
        print(f"[{status_index}] : {status}")
        status_index += 1
    input_list[changed_status_index - 1]["status"] = statuses[int(input("Which status is the order in? Enter the code: ")) - 1]
    with open("orders.json", "w") as file:
        json.dump(input_list, file, indent=4)


def remove_order(input_list):
    order_index = 1
    for order in input_list:
        print(f"[{order_index}] : {order['customer_name']}'s order")
        order_index += 1
    deleted_index = int(input("Which order do you want to delete? Enter the code: "))
    input_list.pop(deleted_index - 1)
    with open("orders.json", "w") as file:
        json.dump(input_list, file, indent=4)





