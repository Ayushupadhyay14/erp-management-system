
class Product:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock


class ERPSystem:
    def __init__(self):
        self.inventory = {}
        self.total_sales = 0
        self.sales_log = []

    def add_product(self, product):
        self.inventory[product.name] = product
        print(f"Added: {product.name} ({product.category}) - Stock: {product.stock}")

    def make_sale(self, product_name, quantity):
        # check if product exists in inventory
        if product_name not in self.inventory:
            print("Product not found")
            return

        product = self.inventory[product_name]

        if product.stock < quantity:
            print("Insufficient stock")
            return

        # update stock and add to sales log
        product.stock -= quantity
        sale_amount = product.price * quantity
        self.total_sales += sale_amount
        self.sales_log.append({
            'product': product_name,
            'quantity': quantity,
            'amount': sale_amount
        })
        print(f"Sold {quantity} x {product_name} = Rs.{sale_amount}")

    def generate_report(self):
        print("\n===== ERP Summary Report =====")
        print(f"\nTotal Sales Revenue: Rs.{self.total_sales}")

        print("\n--- Sales Log ---")
        for sale in self.sales_log:
            print(f"  {sale['product']} | Qty: {sale['quantity']} | Amount: Rs.{sale['amount']}")

        print("\n--- Remaining Inventory ---")
        print(f"  {'Product':<15} {'Category':<15} {'Price':<10} {'Stock':<10}")
        print("  " + "-" * 50)
        for p in self.inventory.values():
            print(f"  {p.name:<15} {p.category:<15} Rs.{p.price:<8} {p.stock}")
        print("=" * 32)
