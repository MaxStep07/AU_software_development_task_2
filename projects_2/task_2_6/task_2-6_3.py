donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()

if donor == "I" or donor == recipient:
    print(f"Переливание возможно: кровь группы {donor} подходит пациенту с группой {recipient}.")
elif donor not in ("I", "II", "III", "IV") or recipient not in ("I", "II", "III", "IV"):
    print("Ошибка: введена некорректная группа крови.")
else:
    print(f"Переливание невозможно: кровь группы {donor} не подходит пациенту с группой {recipient}.")