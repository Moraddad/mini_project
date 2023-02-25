import json
from messages import *
from functions import *
import pymysql.cursors
import os
from dotenv import load_dotenv


load_dotenv(".env")


HOST = os.environ.get("HOST")
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")


def connet_to_db():
    connection = pymysql.connect(host=HOST,
                                user=USER_NAME,
                                password=PASSWORD,
                                database=DATABASE,
                                cursorclass=pymysql.cursors.DictCursor)

    return connection



def main_menu():
    print("WELCOME to Main Menu!")
   
    first_choice = input(main_menu_message)
    if first_choice == "0":
        exit()
    elif first_choice == "1":
        print("*** Product Menu ***")
        second_choice = input(product_menu_message)
        while second_choice != "0":
            connet_to_db()
            cursor = connection.cursor()
            sql = "SELECT `product_id`, `product_name`, `product_price` FROM `products`"
            cursor.execute(sql)
            product_list = cursor.fetchall()
            # product_list = read_file("product.json")
            products_menu(second_choice, product_list)
            print("\n*** Product Menu ***")
            second_choice = input(product_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "2":
        print("*** Courier Menu ***")
        second_choice = input(courier_menu_message)
        while second_choice != "0":
            connet_to_db()
            cursor = connection.cursor()
            sql = "SELECT `courier_id`, `courier_name`, `courier_phone` FROM `couriers`"
            cursor.execute(sql)
            courier_list = cursor.fetchall()
            couriers_menu(second_choice, courier_list)
            print("\n*** Courier Menu ***")
            second_choice = input(courier_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "3":
        print("*** Orders Menu ***")
        second_choice = input(order_menu_message)
        while second_choice != "0":
            courier_list = read_file("courier.json")
            order_list = read_file("order.json")
            product_list = read_file("product.json")

            orders_menu(second_choice, order_list, courier_list, product_list)
            print("\n*** Orders Menu ***")
            second_choice = input(order_menu_message)
        if second_choice == "0":
            main_menu()
    else:
        print(wrong_input)
        main_menu()


while True:
    main_menu()