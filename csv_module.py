
import csv

def group_stock_by_category(file_path):
    category_stock_map = {}

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    category = row['category']
                    stock = int(row['stock'])

                    category_stock_map[category] = category_stock_map.get(category, 0) + stock

                except Exception:
                    print("Invalid row skipped:", row)

    except FileNotFoundError:
        print("File not found!")

    return category_stock_map
