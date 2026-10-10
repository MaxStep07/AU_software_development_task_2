course = 2          # Текущий курс
year = 2026         # Текущий год
width = 70          # Ширина рамки >= 70

line1 = "Добро пожаловать!".center(width)
line2 = f"Студент {course}-го курса {year} года".center(width)
line3 = "Счастливых вам Голодных игр и пусть удача всегда будет с вами)".center(width)

print("=" * width,
    line1,
    line2,
    line3,
    "=" * width,
    sep="\n", end="\n")