from messages import *
from functions import *
import os
from dotenv import load_dotenv

def main_menu():
    print("WELCOME to Main Menu!")
    first_choice = input(main_menu_message)
    if first_choice == "0":
        close_db()
        exit()
    elif first_choice == "1":
        print("*** Products Menu ***")
        second_choice = input(product_menu_message)
        while second_choice != "0":
            products_menu(second_choice)
            print("\n*** Products Menu ***")
            second_choice = input(product_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "2":
        print("*** Couriers Menu ***")
        second_choice = input(courier_menu_message)
        while second_choice != "0":
            couriers_menu(second_choice)
            print("\n*** Couriers Menu ***")
            second_choice = input(courier_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "3":
        print("*** Orders Menu ***")
        second_choice = input(order_menu_message)
        while second_choice != "0":
            orders_menu(second_choice)
            print("\n*** Orders Menu ***")
            second_choice = input(order_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "4":
        print("*** Customers Menu ***")
        second_choice = input(customer_menu_message)
        while second_choice != "0":
            customers_menu(second_choice)
            print("\n*** Customers Menu ***")
            second_choice = input(customer_menu_message)
        if second_choice == "0":
            main_menu()
    else:
        print(wrong_input)
        main_menu()

        
while True:
    main_menu()