# Buggy Script 1: Inefficient loop


def get_even_numbers_buggy(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result


def get_even_numbers(nums):
    return [n for n in nums if n % 2 == 0]


# Buggy Script 2: SQL injection risk + no error handling


def fetch_product_buggy(product_id):
    import psycopg2

    conn = psycopg2.connect(
        dbname="erp", user="user", password="password", host="localhost"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE id = " + str(product_id))
    return cur.fetchone()


def fetch_product(product_id):
    import psycopg2

    conn = None
    try:
        conn = psycopg2.connect(
            dbname="erp", user="user", password="password", host="localhost"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        return cur.fetchone()
    except psycopg2.Error as e:
        print("Database error:", e)
        return None
    finally:
        if conn:
            conn.close()


# Buggy Script 3: Incorrect stock update


def update_stock_buggy(products, name, qty):
    for p in products:
        if p["name"] == name:
            p["stock"] = qty


def update_stock(products, name, qty):
    for p in products:
        if p["name"] == name:
            if p["stock"] >= qty:
                p["stock"] -= qty
                return True
            print("Not enough stock")
            return False
    print("Product not found")
    return False
