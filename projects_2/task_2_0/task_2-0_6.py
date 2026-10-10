f = open("output.txt", "w", encoding="utf-8")
print("Фамилия: Степанов",
       "Имя: Максим",
       "Группа: 202.1",
       "Год поступления: 2025",
       sep='\n', end='', file=f)
f.close()