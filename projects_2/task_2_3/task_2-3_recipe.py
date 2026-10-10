medium = input("Введите название питательной среды: ")
agar = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации (°C): ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{medium}\n\n")
    file.write(f"- Концентрация агара (%): {agar}\n")
    file.write(f"- Температура стерилизации (°C): {temperature}\n")

print("\nФайл 'recipe.txt' успешно сформирован!")