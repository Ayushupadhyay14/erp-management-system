
from erp_system import Product, ERPSystem
from csv_module import group_stock_by_category

def main():
    # Section 1: CSV Module Demo
    print("===== CSV Module Demo =====")
    result = group_stock_by_category("products.csv")
    print("Stock grouped by category:", result)

    # Section 2: ERP System Demo
    print("\n===== ERP System Demo =====")
    system = ERPSystem()

    p1 = Product("Laptop", "Electronics", 50000, 10)
    p2 = Product("Shoes", "Fashion", 2000, 30)
    p3 = Product("Rice", "Grocery", 60, 100)

    system.add_product(p1)
    system.add_product(p2)
    system.add_product(p3)

    system.make_sale("Laptop", 2)
    system.make_sale("Shoes", 5)
    system.make_sale("Rice", 10)

    print("\nGenerating final report...")
    system.generate_report()

if __name__ == "__main__":
    main()
