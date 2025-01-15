
while True:
    first_stone = int(input('Введите число(3 до 20): '))
    if first_stone >= 3 and first_stone <= 20:
        second_stone = ''
        number_list = list(range(1, 20))
        for i in number_list:
            a = i
            for j in range(i+1,21):
                b = j
                if first_stone % (a + b) == 0:
                    second_stone += str(a)
                    second_stone += str(b)

        print(first_stone)
        print(int(second_stone))
    else:
        print('Неверное число!')
        break