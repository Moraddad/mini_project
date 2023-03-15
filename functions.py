from messages import wrong_input
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
cursor=connection.cursor()


def close_db():
    cursor.close()
    connection.close()


def read_from_db(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def edit_db(query):
    cursor.execute(query)
    connection.commit()
    
def products_menu(product_menu_choice):
    if product_menu_choice == "1":
        print_products()
    elif product_menu_choice == "2":
        add_product()
    elif product_menu_choice == "3":
        update_products()
    elif product_menu_choice == "4":
        remove_product()
    else:
        print(wrong_input)


def couriers_menu(courier_menu_choice):
    if courier_menu_choice == "1":
        print_couriers()
    elif courier_menu_choice == "2":
        add_courier()
    elif courier_menu_choice == "3":
        update_courier()
    elif courier_menu_choice == "4":
        remove_courier()
    else:
        print(wrong_input)


def customers_menu(customer_menu_choice):
    if customer_menu_choice == "1":
        print_customers()
    elif customer_menu_choice == "2":
        add_customer()
    elif customer_menu_choice == "3":
        update_customers()
    elif customer_menu_choice == "4":
        remove_customer()
    else:
        print(wrong_input)


def orders_menu(order_menu_choice):
    if order_menu_choice == "1":
        print_orders()
    elif order_menu_choice == "2":
        add_order()
    elif order_menu_choice == "3":
        change_order_status()
    elif order_menu_choice == "4":
        update_order()
    elif order_menu_choice == "5":
        remove_order()
    else:
        print(wrong_input)


#Products
def print_products():
    query = "SELECT `product_id` as ID, `product_name` as Name, `product_price` as Price FROM `products`"
    result = read_from_db(query)
    for product in result:
        print(f"\n{product}")
    
          
def add_product():
    product_name = input("Enter the name of the new product: ")
    product_price = input("Enter the price: ")
    query = f"INSERT INTO `products` (`product_name`, `product_price`) VALUES ('{product_name}', {product_price})"
    edit_db(query)
    print_products()


def update_products():
    print_products()
    selected_id = input("Which product do you want to update? enter the ID: ")
    updated_name = input("Enter the new product's name: ")
    updated_price = input("Enter the new price: ")
    query = f"UPDATE `products` SET `product_name` = '{updated_name}', `product_price` = {updated_price}  WHERE `product_id` = {selected_id}"
    edit_db(query)
    print_products()


def remove_product():
    print_products()
    selected_id = int(input("Which product do you want to delete? enter the ID: "))
    query1 = f"DELETE FROM `order_to_product` WHERE `product_id` = {selected_id}"
    edit_db(query1)
    query2 = f"DELETE FROM `products` WHERE `product_id` = {selected_id}"
    edit_db(query2)
    print_products()


#Couriers
def print_couriers():
    query = "SELECT `courier_id` as ID, `courier_name` as Name, `courier_phone` as Phone FROM `couriers`"
    result = read_from_db(query)
    for courier in result:
        print(f"\n{courier}")


def add_courier():
    print_couriers()
    courier_name = input("Enter the name of the new courier: ")
    courier_phone = input("Enter the phone number: ")
    query = f"INSERT INTO `couriers` (`courier_name`, `courier_phone`) VALUES ('{courier_name}', '{courier_phone}')"
    edit_db(query)
    print_couriers()


def update_courier():
    print_couriers()
    selected_id = input("Which courier do you want to update? enter the ID: ")
    updated_name = input("Enter the courier's name: ")
    updated_phone = input("Enter the new phone number: ")
    query = f"UPDATE `couriers` SET `courier_name` = '{updated_name}', `courier_phone` = '{updated_phone}'  WHERE `courier_id` = {selected_id}"
    edit_db(query)
    print_couriers()
   

def remove_courier():
    print_couriers()
    selected_id = int(input("Which courier do you want to delete? enter the ID: "))
    query = f"DELETE FROM `couriers` WHERE `courier_id` = {selected_id}"
    edit_db(query)
    print_couriers()

#Orders
def print_orders():
    query = """
    SELECT 
    orders.order_id, 
    customers.customer_name, 
    customers.customer_address, 
    customers.customer_phone, 
    couriers.courier_name, 
    couriers.courier_phone, 
    products.product_name, 
    order_status.status 
    FROM 
    orders 
    JOIN customers ON orders.customer_id = customers.customer_id 
    JOIN couriers ON orders.courier_id = couriers.courier_id 
    JOIN order_to_product ON orders.order_id = order_to_product.order_id 
    JOIN products ON order_to_product.product_id = products.product_id 
    JOIN order_status ON orders.status_id = order_status.status_id;
        """
    result = read_from_db(query)
    for order in result:
        print(order)

def add_order():
    print_customers()
    customer_id = input("Please enter the customer's ID: ")
    print_couriers()
    courier_id = input("Please enter the courier's ID: ")
    print_products()
    product_IDs = input("Which product(s) do you want to add to order? enter the ID(s) with a comma: ").split(",")
    selected_products = []
    for i in product_IDs:
        selected_products.append(int(i))
    query1 = f"INSERT INTO `orders` (`customer_id`, `courier_id`, `status_id`) VALUES ({customer_id}, {courier_id}, 1)"
    edit_db(query1)
    cursor.execute("SELECT LAST_INSERT_ID()")
    result = cursor.fetchone()
    order_id = result["LAST_INSERT_ID()"]
    for product in selected_products:
        query2 = f"INSERT INTO `order_to_product` (`order_id`, `product_id`) VALUES ({order_id}, {product})"
        edit_db(query2)
    

def change_order_status():
    statuses = ["Preparing", "Sent", "Delivered"]
    print_orders()
    chosen_id = int(input("Which order do you want to update? enter the ID: "))
    status_index = 1
    for status in statuses:
        print(f"[{status_index}] : {status}")
        status_index += 1
    status_id = int(input("Which status is the order in? Enter the code: "))
    query = f"UPDATE `orders` SET `status_id` = {status_id}, WHERE `order_id` = {chosen_id}"
    edit_db(query)


def update_order():
    print_orders()
    selected_id = input("Enter the order ID that you want to change: ")
    print_customers()
    customer_id = input("Please enter the customer's ID: ")
    print_couriers()
    courier_id = input("Please enter the courier's ID: ")
    print_products()
    product_IDs = input("Which product(s) do you want to add to order? enter the ID(s) with a comma: ").split(",")
    selected_products = []
    for i in product_IDs:
        selected_products.append(int(i))
    query = f"UPDATE `orders` SET `customer_id` = {customer_id}, `courier_id` = {courier_id}  WHERE `order_id` = {selected_id}"
    edit_db(query)
    for product in selected_products:
        query2 = f"UPDATE `order_to_product` SET  `product_id` = {product} WHERE `order_id` = {selected_id}"
        edit_db(query2)


def remove_order():
    print_orders()
    selected_id = int(input("Which order do you want to delete? enter the ID: "))
    query1 = f"DELETE FROM `order_to_product` WHERE `order_id` = {selected_id}"
    edit_db(query1)
    query2 = f"DELETE FROM `orders` WHERE `order_id` = {selected_id}"
    edit_db(query2)
    print_products()


#Customers
def print_customers():
    query = "Select `customer_id` as ID, `customer_name` as Name, `customer_address` as Adress, `customer_phone` as Phone FROM customers"   
    result = read_from_db(query)
    for customer in result:
        print(customer)


def add_customer():
    customer_name = input("Enter the name of the new customer: ")
    customer_address = input("Enter the address: ")
    customer_phone = input("Enter the phone number: ")
    query = f"INSERT INTO `customers` (`customer_name`, `customer_Address`, `customer_phone`) VALUES ('{customer_name}', '{customer_address}', '{customer_phone}' )"
    edit_db(query)
    print_customers()
    

def update_customers():
    print_customers()
    selected_id = input("Which customer do you want to update? enter the ID: ")
    updated_name = input("Enter the new customer's name: ")
    updated_address = input("Enter the new address: ")
    updated_phone = input("Enter the new phone number: ")
    query = f"UPDATE `customers` SET `customer_name` = '{updated_name}', `customer_Address` = '{updated_address}', `customer_phone` = '{updated_phone}'  WHERE `product_id` = {selected_id}"
    edit_db(query)
    print_customers()


def remove_customer():
    print_customers()
    selected_id = int(input("Which customer do you want to delete? enter the ID: "))
    query = f"DELETE FROM `customers` WHERE `customer_id` = {selected_id}"
    edit_db(query)
    print_customers()
