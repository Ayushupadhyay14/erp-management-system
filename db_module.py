import psycopg2


def connect():
    return psycopg2.connect(
        dbname="erp", user="postgres", password="password", host="localhost"
    )


# create all the tables if not already present in the database
def create_tables():
    conn = connect()
    cur = conn.cursor()

    # products table
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY,
        name TEXT,
        category TEXT,
        price FLOAT,
        stock INT
    );
    """
    )

    # customers table
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS customers(
        id SERIAL PRIMARY KEY,
        name TEXT
    );
    """
    )

    # orders table
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS orders(
        id SERIAL PRIMARY KEY,
        customer_id INT,
        product_id INT,
        quantity INT
    );
    """
    )

    conn.commit()
    conn.close()


def insert_product(name, category, price, stock):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO products(name, category, price, stock) VALUES (%s,%s,%s,%s)",
        (name, category, price, stock),
    )

    conn.commit()
    conn.close()


def fetch_orders_by_customer(customer_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM orders WHERE customer_id=%s", (customer_id,))

    orders = cur.fetchall()
    conn.close()
    return orders


# reduce stock when order is placed
def update_stock_after_order(product_id, quantity):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE products SET stock = stock - %s WHERE id=%s", (quantity, product_id)
    )

    conn.commit()
    conn.close()
