import json
from messages import *
from functions import *

def main_menu():
    print("WELCOME to Main Menu!")
    first_choice = input(main_menu_message)
    if first_choice == "0":
        exit()
    elif first_choice == "1":
        print("*** Product Menu ***")
        second_choice = input(product_menu_message)
        while second_choice != "0":
            with open("product.json", "r") as product_file:
                product_list = json.load(product_file)
            products_menu(second_choice, product_list)
            print("\n*** Product Menu ***")
            second_choice = input(product_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "2":
        print("*** Courier Menu ***")
        second_choice = input(courier_menu_message)
        while second_choice != "0":
            with open("courier.json", "r") as courier_file:
                courier_list = json.load(courier_file)
            couriers_menu(second_choice, courier_list)
            print("*** Courier Menu ***")
            second_choice = input(courier_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "3":
        print("*** Orders Menu ***")
        second_choice = input(order_menu_message)
        while second_choice != "0":
            with open("courier.json", "r") as courier_file:
                courier_list = json.load(courier_file)
            with open("orders.json", "r") as order_file:
                order_list = json.load(order_file)
            orders_menu(second_choice, order_list, courier_list)
            second_choice = input(order_menu_message)
        if second_choice == "0":
            main_menu()
    else:
        print(wrong_input)
        main_menu()


while True:
    main_menu()