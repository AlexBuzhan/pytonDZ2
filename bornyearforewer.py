
year_of_birth = int(input('В каком году родился А. С. Пушкин? - '))
while year_of_birth != 1799:
    print('Не верно')
    year_of_birth = int(input('В каком году родился А. С. Пушкин? - '))
else: print('Верно')