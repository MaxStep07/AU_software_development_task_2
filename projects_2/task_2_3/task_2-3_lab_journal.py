def wrap(text, width):
    '''
    Разбивает длинный текст на строки заданной ширины по словам.
    '''
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) < width:
            current = (current + " " + word).strip()
        else:
            if len(current) != 0:
                lines.append(current)
            current = word
    if len(current) != 0:
        lines.append(current)
    return lines


def row(text):
    '''
    Формирует строку для вывода в таблицу.
    '''
    return f"| {text:<{width}} |"


fio = input("Введите ФИО исследователя: ")
date = input("Введите дату: ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

width = 48  # Ширина внутренней части рамки (без "| " и " |")

border = "+" + "-" * (width + 2) + "+"

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(border + "\n")
    file.write(row("Электронный лабораторный журнал") + "\n")
    file.write(border + "\n")
    file.write(row(f"ФИО исследователя : {fio}") + "\n")
    file.write(row(f"Дата              : {date}") + "\n")
    file.write(row(f"Эксперимент       : {experiment}") + "\n")
    file.write(border + "\n")
    file.write(row("Вывод:") + "\n")
    for line in wrap(conclusion, width):
        file.write(row(line) + "\n")
    file.write(border + "\n")