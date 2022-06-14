#Год рождения Пушкина - 1799
#Год рождения Эйштейна - 1879
#Год Рождения Ньютона - 1643
#Год Рождения Дали - 1904
#Год Рождения Леонардо да Винчи - 1452

more = 'y'
yes = 'y'
no = 'n'
while more == yes:
    r_answer = 0
    n_answer = 0
    year_of_birth1 = int(input('В каком году родился А. С. Пушкин? - '))
    year_of_birth2 = int(input('В каком году родился Эйштейн? - '))
    year_of_birth3 = int(input('В каком году родился Ньютон? - '))
    year_of_birth4 = int(input('В каком году родился Дали? - '))
    year_of_birth5 = int(input('В каком году родился Леонардо да Винчи? - '))
    if year_of_birth1 == 1799:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    if year_of_birth2 == 1879:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    if year_of_birth3 == 1643:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    if year_of_birth4 == 1904:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    if year_of_birth5 == 1452:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    print('Правильных ответов', r_answer)
    print('Не правильных ответов', n_answer)
    r_answer100 = ((r_answer * 100) / 5)
    n_answer100 = ((n_answer * 100) / 5)
    print('Процент правильных ответов', r_answer100)
    print('Процент правильных ответов', n_answer100)
    more = input('Хотите сыграть сначала? ')
else: print('Конец игры')
