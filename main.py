
from messages import *
from functions import *
import os
from dotenv import load_dotenv

# load_dotenv(".env")

# HOST = os.environ.get("HOST")
# USER_NAME = os.environ.get("USER_NAME")
# PASSWORD = os.environ.get("PASSWORD")
# DATABASE = os.environ.get("DATABASE")
# print()

def main_menu():
    print("WELCOME to Main Menu!")
    first_choice = input(main_menu_message)
    if first_choice == "0":
        exit()
    elif first_choice == "1":
        print("*** Product Menu ***")
        second_choice = input(product_menu_message)
        while second_choice != "0":
            p_sql = "SELECT `product_id`, `product_name`, `product_price` FROM `products`"
            product_list = read_from_db(p_sql)
            # print(type(product_list))
            # print(product_list)
            products_menu(second_choice, product_list)
            print("\n*** Product Menu ***")
            second_choice = input(product_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "2":
        print("*** Courier Menu ***")
        second_choice = input(courier_menu_message)
        while second_choice != "0":
            c_sql = "SELECT `courier_id`, `courier_name`, `courier_phone` FROM `couriers`"
            courier_list = read_from_db(c_sql)
            couriers_menu(second_choice, courier_list)
            print("\n*** Courier Menu ***")
            second_choice = input(courier_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "3":
        print("*** Orders Menu ***")
        second_choice = input(order_menu_message)
        while second_choice != "0":
            p_sql = "SELECT * FROM `products`"
            product_list = read_from_db(p_sql)
            c_sql = "SELECT * FROM `couriers`"
            courier_list = read_from_db(c_sql)
            o_sql =  """
                SELECT 
                o.order_id
                , cu.customer_name
                , cu.customer_address
                , c.courier_name
                , p.product_name
                FROM orders o
                INNER JOIN couriers c ON o.courier_id = c.courier_id
                INNER JOIN customers cu ON o.customer_id = cu.customer_id
                INNER JOIN order_to_product otp ON o.order_id = otp.order_id
                INNER JOIN products p ON p.product_id = otp.product_id
                ORDER BY o.order_id
                """
            order_list = read_from_db(o_sql)

            # courier_list = read_file("courier.json")
            # order_list = read_file("order.json")
            # product_list = read_file("product.json")

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