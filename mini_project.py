
from functions import *
list_of_orders = [
{
"customer_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 2,
"status": "preparing"
},

{
"customer_name": "Ghasem",
"customer_address": "Unit 25, LONDON",
"customer_phone": "02345666",
"courier": 3,
"status": "preparing"
}
]
product_menu_message = """
        Press [0] to RETURN to main menu,
        Press [1] to PRINT products list,
        Press [2] to ADD a new product to the list,
        Press [3] to UPDATE an existing product,
        Press [4] to DELETE a product.
        """
courier_menu_message = """
        Press [0] to RETURN to main menu,
        Press [1] to PRINT couriers list,
        Press [2] to ADD a new courier to the list,
        Press [3] to UPDATE an existing courier,
        Press [4] to DELETE a courier.
        """
main_menu_message = """
        Press [1] to enter the PRODUCTS MENU,
        Press [2] to enter the COURIERS MENU,
        Press [3] to enter the ORDERS MENU,
        Press [0] to EXIT

        """
order_menu_message = """
        Press [0] to RETURN to main menu,
        Press [1] to PRINT orders list,
        Press [2] to ADD a new order,
        Press [3] to UPDATE an existing order status
       
"""


def main_menu():
    print("WELCOME to Main Menu!")
    first_choice = input(main_menu_message)
    if first_choice == "0":
        exit()
    elif first_choice == "1":
        with open("products.txt") as product_file:
            product_list = []
            for line in product_file:
                product_list.append(line.rstrip())
        second_choice = input(product_menu_message)
        while second_choice != "0":
            products_menu(second_choice, product_list)
            second_choice = input(product_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "2":
        with open("couriers.txt") as courier_file:
            courier_list = []
            for line in courier_file:
                courier_list.append(line.rstrip())
        second_choice = input(courier_menu_message)
        while second_choice != "0":
            couriers_menu(second_choice, courier_list)
            second_choice = input(courier_menu_message)
        if second_choice == "0":
            main_menu()
    elif first_choice == "3":
        with open("couriers.txt") as courier_file:
            courier_list = []
            for line in courier_file:
                courier_list.append(line.rstrip())
        second_choice = input(order_menu_message)
        while second_choice != "0":
            orders_menu(second_choice, list_of_orders, courier_list)
            second_choice = input(order_menu_message)
        if second_choice == "0":
            main_menu()




    else:
        print("Please enter the correct input!")
        main_menu()


while True:
    main_menu()