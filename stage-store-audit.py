raw_orders = [
    {"order_id": 101, "customer_id": 1, "customer": "  ahmed ali ", "city": "cairo", "item": "laptop_stand", "price": "250.50", "qty": 3},
    {"order_id": 102, "customer_id": 2, "customer": "SARA", "city": "Alex", "item": "mouse_pad", "price": "400.00", "qty": 2},
    {"order_id": 103, "customer_id": 1, "customer": "ahmed ali", "city": "CAIRO", "item": "usb_cable", "price": "-50.00", "qty": 5},
    {"order_id": 104, "customer_id": 3, "customer": "Mona", "city": "Giza", "item": "keyboard", "price": None, "qty": 1},
    {"order_id": 105, "customer_id": 2, "customer": "sara", "city": "alex", "item": "monitor_arm", "price": "0", "qty": 2},
    {"order_id": 106, "customer_id": 3, "customer": "Mona", "city": "Giza", "item": "webcam_hd", "price": "150.75", "qty": 4}
]

#1. clean_orders(rows, min_price=0):
#2. Loops through rows and skips any row where price is None or float(price) <= min_price.
#3. Cleans strings: .strip().title() on customer and city, and replaces "_" with " " in item.
#4. Converts price to a float and calculates total_cost = round(price * qty, 2).
#5. Returns *two values*: (clean_list, rejected_count).


def clean_orders(rows, min_price=0):
    clean_list =[]
    rejected_count = 0


    for row in rows:
        if row["price"] is None or float(row["price"]) <= min_price:
            rejected_count = rejected_count + 1
            continue
        price = float(row["price"])
        clean_list.append({
            "order_id": row["order_id"],
            "customer_id": row["customer_id"],
            "customer": row["customer"].strip().title(),
            "city": row["city"].strip().title(),
            "item": row["item"].strip().lower(),
            "price": price,
            "qty": row["qty"],
            "total_cost": round(price * row["qty"], 2)
        })
    return clean_list, rejected_count

#1. summarize_orders(clean_list):
#2. Uses a *list comprehension* to extract all total_cost values.
#3. Uses a *set* to get all unique cleaned cities.
#4. Prints a summary using *f-strings* showing: valid order count, sum(), min(), max(), average order cost, and the set of unique cities.

def summarize_orders(clean_list):
    totals = [order["total_cost"] for order in clean_list]
    cities = [order["city"] for order in clean_list]
    print(f"valid orders: {len(clean_list)}")
    print(f"Total revenue: {sum(totals)}")
    print(f"Min order: {min(totals)}")
    print(f"Max order: {max(totals)}")
    print(f"Average order: {sum(totals) / len(totals):.2f}") 
    print(f"Unique cities: {set(cities)}")


if __name__ == "__main__":
    clean, rejected = clean_orders(raw_orders)
    print(f"Rejected orders: {rejected}")
    summarize_orders(clean)