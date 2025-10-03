import random
import datetime

stores = ["7-Eleven", "Family Mart", "Indomaret", "Alfamart", "Circle K", "Lawson"]


items = [

    ("Air Mineral", 3000, 0, 1),  
    ("Roti Tawar", 12000, 1, 0),
    ("Mie Instan", 3500, 1, 0),
    ("Kopi Instan", 5000, 1, 0),
    ("Minuman Soda", 8000, 0, 1),
    ("Susu UHT", 15000, 0, 1),
    ("Cokelat Batangan", 12000, 1, 0),
    ("Snack Kentang", 10000, 1, 0),
    ("Teh Botol", 6000, 0, 1),
    ("Rokok", 25000, 1, 0),
    ("Baterai", 10000, 1, 0),
    ("Air Mineral 2", 3200, 0, 1),  
    ("Roti Gandum", 12500, 1, 0),
    ("Mie Goreng", 3600, 1, 0),
    ("Kopi Hitam", 5200, 1, 0),
    ("Minuman Berkarbonasi", 8200, 0, 1),
    ("Susu Cokelat", 15500, 0, 1),
    ("Cokelat Putih", 12500, 1, 0),
    ("Keripik Kentang", 10500, 1, 0),
    ("Teh Hijau", 6500, 0, 1),
    ("Rokok Filter", 26000, 1, 0),
    ("Baterai AAA", 10200, 1, 0),
    ("Air Mineral 3", 3100, 0, 1),  
    ("Roti Manis", 13000, 1, 0),
    ("Mie Kuah", 3700, 1, 0),
    ("Kopi Susu", 5300, 1, 0),
    ("Soda Lemon", 8500, 0, 1),
    ("Susu Stroberi", 15800, 0, 1),
    ("Cokelat Almond", 13000, 1, 0),
    ("Snack Jagung", 10800, 1, 0),
    ("Teh Melati", 6800, 0, 1),
    ("Rokok Kretek", 27000, 1, 0),
    ("Baterai AA", 10500, 1, 0),
    ("Air Mineral 4", 3050, 0, 1),  
    ("Roti Coklat", 13500, 1, 0),
    ("Mie Pedas", 3900, 1, 0),
    ("Kopi Mocha", 5400, 1, 0),
    ("Soda Anggur", 8800, 0, 1),
    ("Susu Vanila", 16000, 0, 1),
    ("Cokelat Kacang", 13500, 1, 0),
    ("Snack Keju", 11200, 1, 0),
    ("Teh Lemon", 7000, 0, 1),
    ("Rokok Menthol", 28000, 1, 0),
    ("Baterai 9V", 11000, 1, 0),
    ("Air Mineral 5", 2900, 0, 1),  
    ("Roti Isi", 14000, 1, 0),
    ("Mie Ayam", 4000, 1, 0),
    ("Kopi Gula Aren", 5500, 1, 0),
    ("Soda Jeruk", 9000, 0, 1),
    ("Susu Kedelai", 16500, 0, 1),
    ("Cokelat Matcha", 14000, 1, 0),
    ("Snack Rumput Laut", 11500, 1, 0),
    ("Teh Susu", 7200, 0, 1),
    ("Rokok Mild", 29000, 1, 0),
    ("Baterai C", 11500, 1, 0),
    ("Air Mineral 6", 2800, 0, 1),  
    ("Roti Keju", 14500, 1, 0),
    ("Mie Kari", 4100, 1, 0),
    ("Kopi Latte", 5700, 1, 0),
    ("Soda Mangga", 9200, 0, 1),
    ("Susu Full Cream", 17000, 0, 1),
    ("Cokelat Susu", 14500, 1, 0),
    ("Snack Pedas", 11800, 1, 0),
    ("Teh Tarik", 7500, 0, 1),
    ("Rokok Premium", 30000, 1, 0),
    ("Baterai D", 12000, 1, 0),
]


def random_date():
    today = datetime.date.today()
    random_days = random.randint(1, 365)
    date = today - datetime.timedelta(days=random_days)
    return date.year, date.month, date.day


file_path = "invoice.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write("InvoiceLineID,CustomerCode,TransactionID,Description,Year,Month,Day,PackageTypeID,Quantity,Sales,TotalDryItems,TotalChillerItems\n")
    
    for i in range(8000000):  
        store = random.choice(stores)
        item, price, dry_items, chiller_items = random.choice(items)
        quantity = random.randint(1, 5)
        total_price = price * quantity
        year, month, day = random_date()
        package_type_id = random.randint(1, 3)  
        customer_code = f"{random.randint(1, 5000)}"
        transaction_id = f"{random.randint(1, 5000000)}"
        
        file.write(f"{i+1},{customer_code},{transaction_id},{item} - {store},{year},{month},{day},{package_type_id},{quantity},{total_price},{dry_items * quantity},{chiller_items * quantity}\n")

print(f"File '{file_path}' has been made")
