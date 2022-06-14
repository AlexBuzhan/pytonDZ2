

year_of_birth = int(input('В каком году родился А. С. Пушкин? - '))
if year_of_birth == 1799:
    birthday = float(input('Укажите день рождения А. С. Пушкина? (дд.мм) - '))
    if birthday == 26.05:
        print('Верно')
    else: print('Не верный день рождения')
else: print('Не верный год')