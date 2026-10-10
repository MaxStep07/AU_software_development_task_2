total = int(input("Введите общее количество произведенных капсул: "))
per_pack = int(input("Введите количество капсул в одной упаковке: "))

full_packs = total // per_pack
remainder = total % per_pack

print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{remainder}")