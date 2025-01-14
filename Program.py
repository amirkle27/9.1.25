from Customer import Customer
import sqlite3

connection = sqlite3.connect("customer.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

def print_all_customers():
    customers = cursor.execute("""SELECT * FROM Customer""")
    customers_list = [Customer(row['id'], row['fname'], row['lname'], row['address'], row['mobile'])
    for row in customers]
    return customers_list

def insert_customer(fname, lname, address, mobile):
    cursor.execute("""
    INSERT INTO Customer (fname, lname, address, mobile) VALUES
            (?, ?, ?, ?)            
        """, (fname, lname, address, mobile))
    connection.commit()
insert_customer('Amir', 'Klein', 'Balfour 119 Bat Yam', '058-5567711')
insert_customer( 'Rachel', 'Mizrachi', '39 Hatmarim st. Eilat', '052-5312276')


all_customers = print_all_customers()
for customer in all_customers:
    print(customer)

print(all_customers[0])
print(repr(all_customers[1]))
print(all_customers[0]==all_customers[4])


print(f'hash of customer 1: {hash(all_customers[0])}, hash of customer 5: {hash(all_customers[4])})')


