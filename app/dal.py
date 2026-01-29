from typing import List, Dict, Any

from db import get_db_connection
from db_init import init_database

init_database()
con = get_db_connection()

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    cursor = con.cursor()
    cursor.execute("SELECT SUM(amount) as total, AVG(amount) as average, MIN(amount) as minimum, MAX(amount) as maximum FROM payments")
    return cursor.fetchall()

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    cursor = con.cursor()
    cursor.execute("SELECT orderNumber, comments FROM orders WHERE comments is null ORDER BY orderDate")
    return cursor.fetchall()

def get_first_5_customers():
    """Return the first 5 customers."""
    cursor = con.cursor()
    cursor.execute("SELECT customerName, contactLastName, contactFirstName FROM customers ORDER BY contactLastName LIMIT 5")
    return cursor.fetchall()

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    cursor = con.cursor()
    cursor.execute("SELECT SUM(amount) as total, AVG(amount) as average, MIN(amount) as minimum, MAX(amount) as maximumFROM payments")
    return cursor.fetchall()
 
def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    cursor = con.cursor()
    cursor.execute("SELECT e.firstName, e.lastName, o.phone FROM employees e JOIN offices o ON e.officeCode = o.officeCode")
    return cursor.fetchall()

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    cursor = con.cursor()
    cursor.execute("SELECT c.customerName, o.shippedDate FROM customers c JOIN orders o ON c.customerNumber = o.customerNumber")
    return cursor.fetchall()

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    cursor = con.cursor()
    cursor.execute("SELECT c.customerName, SUM(od.quantityOrdered) as items FROM customers c JOIN orders oON o.customerNumber = c.customerNumber JOIN orderdetails od ON o.orderNumber = od.orderNumber GROUP BY od.orderNumber ORDER BY customerName")
    return cursor.fetchall()

def get_customers_payments_by_lastname_pattern():
    """Return customers and payments for last names matching pattern."""
    cursor = con.cursor()
    cursor.execute("SELECT c.customerName, concat(e.firstName, ' ', e.lastName) as salesman, SUM(p.amount) as total FROM customers c JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber JOIN payments p ON p.customerNumber = c.customerNumber WHERE c.contactFirstName LIKE '%ly%' OR c.contactFirstName LIKE '%Mu%' GROUP BY c.customerNumber ORDER BY total DESC")
    return cursor.fetchall()