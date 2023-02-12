import json
from messages import *


def products_menu(product_menu_choice, p_list):
    if product_menu_choice == "1":
        print_items(p_list)
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
        print_items(c_list)
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
        print_items(order_list)
    elif order_menu_choice == "2":
        add_order(order_list, c_list)
    elif order_menu_choice == "3":
        change_order_status(order_list)
    elif order_menu_choice == "4":
        update_order(order_list, c_list)
    elif order_menu_choice == "5":
        remove_order(order_list)
    else:
        print(wrong_input)
          
def add_item(input_list : dict, input_name : str):
    new_item = input(f"Enter new {input_name}'s name:\n")
    new_number = str(len(input_list) + 1)
    input_list[new_number] = new_item
    print(f"New {input_name}s list: ")
    print_items(input_list)
    write_file(f"{input_name}.json", input_list)

def update_item(input_list : dict, input_name: str):
    print_items(input_list)
    chosen_number = get_correct_input(input_list, "update")
    updated_name = input(f"Enter the new {input_name}'s name: \n")
    input_list[chosen_number] = updated_name
    print(f"Updated {input_name}s list: ")
    print_items(input_list)
    write_file(f"{input_name}.json", input_list)
   
       
def remove_item(input_list : dict, input_name : str):
    print_items(input_list)
    chosen_number = get_correct_input(input_list, "remove")
    input_list.pop(chosen_number)
    temp_values = input_list.values()
    input_list = {}
    i = 1
    for name in temp_values:
        input_list[i] = name
        i += 1
    print(f"New {input_name}s list: ")
    print_items(input_list)
    write_file(f"{input_name}.json", input_list)


def add_order(input_list, c_list):
    new_order = {}
    new_order["customer_name"] = input("Please enter customer's name: \n")
    new_order["customer_address"] = input("Please enter the address: \n")
    new_order["customer_phone"] = input("Please enter the phone number: \n")
    print("List of couriers: ")
    print_items(c_list)
    courier_number = input("Which courier do you want to assign? enter the code:\n")
    new_order["courier"] = c_list[courier_number]
    new_order["status"] = "preparing"
    print(f"New order: {new_order}")
    new_number = str(len(input_list) + 1)
    input_list[new_number] = new_order
    with open("orders.json", "w") as file:
        json.dump(input_list, file, indent=4)


def change_order_status(input_list):
    statuses = ["Preparing", "Sent", "Delivered"]
    print_items(input_list)
    order_number = get_correct_input(input_list, "update status")
    status_index = 1
    for status in statuses:
        print(f"[{status_index}] : {status}")
        status_index += 1
    input_list[order_number]["status"] = statuses[int(input("Which status is the order in? Enter the code: ")) - 1]
    print(f"New status: {input_list[order_number]}")
    with open("orders.json", "w") as file:
        json.dump(input_list, file, indent=4)


def update_order(input_list, c_list):
    elements = ["customer_name", "customer_address", "customer_phone", "courier", "status"]
    key_index = 1
    print_items(input_list)
    order_number = get_correct_input(input_list, "update")
    for element in elements:
        if element == "status":
            continue
        print(f"[{key_index}] : {element}")
        key_index += 1
    which_element_to_update = elements[int(input("Which part do you want to update? Enter the code: ")) - 1]
    if which_element_to_update == "courier":
        print_items(c_list)
        chosen_courier_index = str(input("Which courier do you want to chose? Enter the code: "))
        new_value = c_list[chosen_courier_index]
    else:
        new_value = input("Enter the new value: ")
    if new_value != "":
        input_list[order_number][which_element_to_update] = new_value
    print(f"Updated order: {input_list[order_number]}")
    with open("orders.json", "w") as file:
        json.dump(input_list, file, indent=4)
    
            
def remove_order(input_list):
    order_index = 1
    print_items(input_list)
    deleted_index = (input("Which order do you want to delete? Enter the code: "))
    input_list.pop(deleted_index)
    temp_values = input_list.values()
    input_list = {}
    i = 1
    for customer in temp_values:
        input_list[i] = customer
        i += 1
    with open("orders.json", "w") as file:
        json.dump(input_list, file, indent=4)


def print_items(input_dict):
    for key in input_dict:
        print(f"[{key}] : {input_dict[key]}")


def get_correct_input(input_list, command):
    false_input = True
    while false_input:
        chosen_number = input(f"Which item do you want to {command}? enter the code: " )
        acceptable_input = input_list.keys()
        if chosen_number not in acceptable_input:
            print("Enter the correct input please!")
        else:
            false_input = False
    return chosen_number


def read_file(dict_name : str):
    with open(dict_name) as file:
        content = json.load(file)
    return content


def write_file(dict_name : str, contetnt):
    with open(dict_name, "w") as file:
        json.dump(contetnt, file, indent=4)