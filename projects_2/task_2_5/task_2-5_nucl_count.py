print("=== Анализ последовательности ДНК ===\n")

seq = input("Введите последовательность ДНК: ")
seq = seq.upper()

print(f"\nПоследовательность в верхнем регистре: {seq}\n")


counts = {
    'A': seq.count('A'),
    'T': seq.count('T'),
    'G': seq.count('G'),
    'C': seq.count('C')
}

total = len(seq)

print("Подсчёт нуклеотидов:")
for nuc in ['A', 'T', 'G', 'C']:
    count = counts[nuc]
    percent = (count / total * 100) if total > 0 else 0.0
    print(f"{nuc}: {count} ({percent:.2f}%)")

print()
print(f"Общая длина: {total} нуклеотидов")