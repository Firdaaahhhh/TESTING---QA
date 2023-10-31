def calculate_total_sales(items):
    total_sales = 0
    for item in items:
        if "price" in item and "quantity" in item:
            total_sales += item["price"] * item["quantity"]
    return total_sales
