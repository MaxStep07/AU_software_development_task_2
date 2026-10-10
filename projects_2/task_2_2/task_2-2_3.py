device_name = "Микроскоп"
inventory_number = "INV-00123"
is_working = True
quantity = 5

print(f"{'Device':9}\t{'Inventory_number':16}\t{'Status':10}\tQuantity")
print(f"{device_name:9}\t{inventory_number:16}\t{'Исправен' if is_working else 'Неисправен':10}\t{quantity}")