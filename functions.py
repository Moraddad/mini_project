import json
from messages import *
from tabulate import tabulate
import pymysql.cursors
import os
from dotenv import load_dotenv
load_dotenv(".env")
HOST = os.environ.get("HOST")
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")

connection = pymysql.connect(host=HOST,
                             user=USER_NAME,
                             password=PASSWORD,
                             database=DATABASE,
                             cursorclass=pymysql.cursors.DictCursor)


def connet_to_db():
    connection = pymysql.connect(host=HOST,
                                user=USER_NAME,
                                password=PASSWORD,
                                database=DATABASE,
                                cursorclass=pymysql.cursors.DictCursor)
    return connection


def products_menu(product_menu_choice, p_list):
    if product_menu_choice == "1":
        print_items(p_list, "Products")
    elif product_menu_choice == "2":
        add_product()
    elif product_menu_choice == "3":
        update_product(p_list)
    elif product_menu_choice == "4":
        remove_product(p_list, "Products")
    else:
        print(wrong_input)


def couriers_menu(courier_menu_choice, c_list):
    if courier_menu_choice == "1":
        print_items(c_list, "Couriers")
    elif courier_menu_choice == "2":
        add_courier()
    elif courier_menu_choice == "3":
        update_courier(c_list)
    elif courier_menu_choice == "4":
        remove_courier(c_list, "Couriers")
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
        remove_order(order_list, "order")
    else:
        print(wrong_input)

          
def add_product():
    product_name = input("Enter new product's name: ")
    product_price = input("Enter the price: ")
    cursor = connection.cursor()
    sql = "INSERT INTO `products` (`product_name`, `product_price`) VALUES (%s, %s)"
    cursor.execute(sql, (product_name, product_price))
    connection.commit()


def add_courier():
    c_name = input("Enter new courier's name: ")
    c_phone = input("Enter the phone number: ")
    cursor = connection.cursor()
    sql = "INSERT INTO `couriers` (`courier_name`, `courier_phone`) VALUES (%s, %s)"
    cursor.execute(sql, (c_name, c_phone))
    connection.commit()


def update_product(input_list):
    print_items(input_list, "Products")
    chosen_id = input("Which product do you want to update? enter the ID: ")
    updated_name = input("Enter the new product's name: ")
    updated_price = input("Enter the new price: ")
    cursor = connection.cursor()
    sql = "UPDATE `products` SET `product_name` = %s, `product_price` = %s  WHERE `product_id` = %s"
    cursor.execute(sql, (updated_name, updated_price, chosen_id))
    connection.commit()
    connet_to_db()



def update_courier(input_list):
    print_items(input_list, "Couriers")
    chosen_id = input("Which courier do you want to update? enter the ID: ")
    updated_name = (input(f"Enter the courier's name: "))
    updated_phone = input(f"Enter the new phone number: ")
    cursor = connection.cursor()
    sql = "UPDATE `couriers` SET `courier_name` = %s, `courier_phone` = %s  WHERE `courier_id` = %s"
    cursor.execute(sql, (updated_name, updated_phone, chosen_id))
    connection.commit()
   
       
def remove_product(input_list : dict, input_name : str):
    print_items(input_list, input_name)
    chosen_id = int(input("Which product do you want to delete? enter the ID: "))
    cursor = connection.cursor()
    sql = "DELETE FROM `products` WHERE `product_id` = %s"
    cursor.execute(sql, chosen_id)
    connection.commit()


def remove_courier(input_list, input_name : str):
    print_items(input_list, input_name)
    chosen_id = int(input("Which courier do you want to delete? enter the ID: "))
    # connet_to_db()
    cursor = connection.cursor()
    sql = "DELETE FROM `couriers` WHERE `courier_id` = %s"
    cursor.execute(sql, chosen_id)
    connection.commit()


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
    

def remove_order(input_list : dict, input_name : str):
    print_items(input_list, input_name)
    chosen_id = input("Which order do you want to delete? enter the ID: ")
    input_list.pop(chosen_id)
    temp_values = input_list.values()
    input_list = {}
    i = 1
    for content in temp_values:
        input_list[i] = content
        i += 1
    print_items(input_list, f"{input_name}s" )
    write_file(f"{input_name}.json", input_list)


def print_items(input_dict, input_name : str):
    print(f"\n## {input_name} ##")
    for i in input_dict:
        print(i)
        

def print_orders(order_list):
    headers = ["Order No.", "Customer Name", "Customer Address", "Customer Phone", "Items", "Courier", "Status" ]
    rows = []
    for key, values in order_list.items():
        row = [key, values["customer_name"], values["customer_address"], values["customer_phone"], values["items"], values["courier"], values["status"]]
        rows.append(row)
    print(tabulate(rows, headers=headers, numalign = "center" ))


# def get_correct_input(input_list, command):
#     false_input = True
#     while false_input:
#         user_input = input(f"Which item do you want to {command}? enter the code: " )
#         acceptable_input = input_list.keys()
#         if user_input not in acceptable_input:
#             print("*** Enter the correct input please! ***")
#         else:
#             false_input = False
#     return user_input

def get_correct_input(input_list : dict, command):
    valid_inputs = []
    i = 1
    for key in input_list.keys():
        valid_inputs.append(key)
    while True: 
        try:
            user_input = input(f"Which item do you want to {command}? Enter the code: ")
            if user_input not in valid_inputs:
                raise ValueError
            break
        except ValueError:
            print(" *** Invalid input. Please enter one of the above codes. *** ")
    return user_input

def read_file(dict_name : str):
    with open(dict_name) as file:
        content = json.load(file)
    return content


def write_file(dict_name : str, contetnt):
    with open(dict_name, "w") as file:
        json.dump(contetnt, file, indent=4)