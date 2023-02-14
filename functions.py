import json
from messages import *
from tabulate import tabulate

def products_menu(product_menu_choice, p_list):
    if product_menu_choice == "1":
        print_items(p_list, "Products")
    elif product_menu_choice == "2":
        add_product(p_list)
    elif product_menu_choice == "3":
        update_product(p_list)
    elif product_menu_choice == "4":
        remove_item(p_list, "product")
    else:
        print(wrong_input)


def couriers_menu(courier_menu_choice, c_list):
    if courier_menu_choice == "1":
        print_items(c_list, "Couriers")
    elif courier_menu_choice == "2":
        add_courier(c_list)
    elif courier_menu_choice == "3":
        update_courier(c_list)
    elif courier_menu_choice == "4":
        remove_item(c_list, "courier")
    else:
        print(wrong_input)


def orders_menu(order_menu_choice, order_list, c_list, p_list):
    if order_menu_choice == "1":
        print_orders(order_list)
    elif order_menu_choice == "2":
        add_order(order_list, c_list, p_list)
    elif order_menu_choice == "3":
        change_order_status(order_list)
    elif order_menu_choice == "4":
        update_order(order_list, c_list, p_list)
    elif order_menu_choice == "5":
        remove_item(order_list, "order")
    else:
        print(wrong_input)

          
def add_product(input_list : dict):
    product_name = input("Enter new product's name: ")
    product_price = input("Enter the price: ")
    new_number = str(len(input_list) + 1)
    input_list[new_number] = {"Name" : product_name, "Price" : product_price}
    print_items(input_list, "Products")
    write_file("product.json", input_list)


def add_courier(input_list : dict):
    courier_name =  input("Enter new courier's name: ")
    courier_phone = input("Enter the phone number: ")
    new_number = str(len(input_list) + 1)
    input_list[new_number] = {"Name" : courier_name, "Phone" : courier_phone}
    print_items(input_list, "Couriers")
    write_file("courier.json", input_list)


def update_product(input_list : dict):
    print_items(input_list, "Products")
    chosen_number = get_correct_input(input_list, "update")
    updated_name = input(f"Enter the new product's name. (If you don't want to change, just press ENTER): ")
    if updated_name != "" :
        input_list[chosen_number]["Name"] = updated_name
    updated_price = input(f"Enter the new price. (If you don't want to change, just press ENTER): ")
    if updated_price != "" :
        input_list[chosen_number]["Price"] = updated_price
    print_items(input_list, "Products")
    write_file("product.json", input_list)


def update_courier(input_list : dict):
    print_items(input_list, "Couriers")
    chosen_number = get_correct_input(input_list, "update")
    updated_name = input(f"Enter the new courier's name. (If you don't want to change, just press ENTER): ")
    if updated_name != "" :
        input_list[chosen_number]["Name"] = updated_name
    updated_phone = input(f"Enter the new phone number. (If you don't want to change, just press ENTER): ")
    if updated_phone != "" :
        input_list[chosen_number]["Phone"] = updated_phone
    print_items(input_list, "Couriers")
    write_file("courier.json", input_list)
   
       
def remove_item(input_list : dict, input_name : str):
    print_items(input_list, f"{input_name}s" )
    chosen_number = get_correct_input(input_list, "remove")
    input_list.pop(chosen_number)
    temp_values = input_list.values()
    input_list = {}
    i = 1
    for name in temp_values:
        input_list[i] = name
        i += 1
    print_items(input_list, f"{input_name}s" )
    write_file(f"{input_name}.json", input_list)


def add_order(input_list, c_list, p_list):
    new_order = {}
    new_order["customer_name"] = input("Please enter customer's name: \n")
    new_order["customer_address"] = input("Please enter the address: \n")
    new_order["customer_phone"] = input("Please enter the phone number: \n")
    print_items(p_list, "Products")
    product_numbers = input("Which products do you want to add to order? enter the code(s) with a comma: ")
    index_of_products = product_numbers.split(",")
    name_of_products = []
    for i in index_of_products:
        chosen_product = p_list[i]["Name"]
        name_of_products.append(chosen_product)
    print_items(c_list, "Couriers")
    courier_number = input("Which courier do you want to assign? enter the code:\n")
    new_order["courier"] = c_list[courier_number]["Name"]
    new_order["status"] = "preparing"
    new_order["items"] = name_of_products
    print(f"New order: {new_order}")
    new_number = str(len(input_list) + 1)
    input_list[new_number] = new_order
    with open("order.json", "w") as file:
        json.dump(input_list, file, indent=4)


def change_order_status(input_list):
    statuses = ["Preparing", "Sent", "Delivered"]
    print_orders(input_list)
    order_number = get_correct_input(input_list, "update status")
    status_index = 1
    for status in statuses:
        print(f"[{status_index}] : {status}")
        status_index += 1
    input_list[order_number]["status"] = statuses[int(input("Which status is the order in? Enter the code: ")) - 1]
    print(f"New status: {input_list[order_number]}")
    with open("order.json", "w") as file:
        json.dump(input_list, file, indent=4)


def update_order(input_list, c_list, p_list):
    elements = ["customer_name", "customer_address", "customer_phone", "items", "courier", "status"]
    key_index = 1
    print_orders(input_list)
    order_number = get_correct_input(input_list, "update")
    for element in elements:
        if element == "status":
            continue
        print(f"[{key_index}] : {element}")
        key_index += 1
    which_element_to_update = elements[int(input("Which part do you want to update? Enter the code: ")) - 1]
    if which_element_to_update == "courier":
        print_items(c_list, "Couriers")
        chosen_courier_index = str(input("Which courier do you want to choose? Enter the code: "))
        new_value = c_list[chosen_courier_index]["Name"]
        input_list[order_number][which_element_to_update] = new_value
    elif which_element_to_update == "items":
        print_items(p_list, "Products")
        product_numbers = input("Which products do you want to add to order? enter the code(s) with a comma: ")
        index_of_products = product_numbers.split(",")
        name_of_products = []
        for i in index_of_products:
            chosen_product = p_list[i]["Name"]
            name_of_products.append(chosen_product)
        input_list[order_number][which_element_to_update] = name_of_products
    else:
        new_value = input("Enter the new value: ")
        if new_value != "":
            input_list[order_number][which_element_to_update] = new_value
    print(f"Updated order: {input_list[order_number]}")
    with open("order.json", "w") as file:
        json.dump(input_list, file, indent=4)
    

def print_items(input_dict : dict, input_name : str):
    print(f"\n## {input_name} ##")
    for key in input_dict:
        print(f"[{key}] : {input_dict[key]}")


def print_orders(order_list):
    headers = ["Order No.", "Customer Name", "Customer Address", "Customer Phone", "Items", "Courier", "Status" ]
    rows = []
    for key, values in order_list.items():
        row = [key, values["customer_name"], values["customer_address"], values["customer_phone"], values["items"], values["courier"], values["status"]]
        rows.append(row)
    print(tabulate(rows, headers=headers, numalign = "center" ))


def get_correct_input(input_list, command):
    false_input = True
    while false_input:
        chosen_number = input(f"Which item do you want to {command}? enter the code: " )
        acceptable_input = input_list.keys()
        if chosen_number not in acceptable_input:
            print("*** Enter the correct input please! ***")
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