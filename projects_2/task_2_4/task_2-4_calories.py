mass_of_protein = float(input("Масса белков в продукте (г): "))
mass_of_fats = float(input("Масса жиров в продукте (г): "))
mass_of_carbohydrates = float(input("Масса углеводов в продукте (г): "))

total_caloric = mass_of_protein * 4 + mass_of_fats * 9 + mass_of_carbohydrates * 4

print(f"Общая калорийность в продукте: {total_caloric: .2f} ккал")