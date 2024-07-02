number = int(input("Введите число(3 до 20): "))

list_ = []
pairs = set()
for i in range(1, 21):
    for j in range(1, 21):
        if i == j:
            continue
        if number % (i+j) == 0 and (i, j) not in pairs:
            list_.append((i, j))
            pairs.add((i, j))
            pairs.add((j, i))
print(f"Пары для {number} --> {list_}")


