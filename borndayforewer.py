
year_of_birth = int(input('В каком году родился А. С. Пушкин? - '))
while year_of_birth != 1799:
    print('Не верно')
    year_of_birth = int(input('В каком году родился А. С. Пушкин? - '))
else:
    birthday = float(input('Укажите день рождения А. С. Пушкина? (дд.мм) - '))
    while birthday != 26.05:
        print('Не верный день рождения')
        birthday = float(input('Укажите день рождения А. С. Пушкина? (дд.мм) - '))
    else: print('Верно')
