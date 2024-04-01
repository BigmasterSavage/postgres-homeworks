import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="Touch12345"
)

cur = conn.cursor()

with open('north_data/customers_data.csv', 'r', encoding="utf-8") as f:
    next(f)
    cur.copy_from(f, 'customers_data', sep=',')
    conn.commit()

with open('north_data/employees_data.csv', 'r', newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)", row)
    conn.commit()

with open('north_data/orders_data.csv', 'r', newline="", encoding="utf-8") as f:
    next(f)
    cur.copy_from(f, 'orders_data', sep=',')
    conn.commit()