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
    YEAR_OF_BIRTH_PUSHKIN = int(input('В каком году родился А. С. Пушкин? - '))
    YEAR_OF_BIRTH_EISHTEIN = int(input('В каком году родился Эйштейн? - '))
    YEAR_OF_BIRTH_NUTON = int(input('В каком году родился Ньютон? - '))
    YEAR_OF_BIRTH_DALI = int(input('В каком году родился Дали? - '))
    YEAR_OF_BIRTH_LEO = int(input('В каком году родился Леонардо да Винчи? - '))
    if YEAR_OF_BIRTH_PUSHKIN == 1799:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    if YEAR_OF_BIRTH_EISHTEIN == 1879:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    if YEAR_OF_BIRTH_NUTON == 1643:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    if YEAR_OF_BIRTH_DALI == 1904:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    if YEAR_OF_BIRTH_LEO == 1452:
        r_answer = r_answer + 1
    else: n_answer = n_answer + 1
    print('Правильных ответов', r_answer)
    print('Не правильных ответов', n_answer)
    questions = 5
    r_answer_proc = ((r_answer * 100) / questions)
    n_answer_proc = ((n_answer * 100) / questions)
    print('Процент правильных ответов', r_answer_proc)
    print('Процент правильных ответов', n_answer_proc)
    more = input('Хотите сыграть сначала? (y/n) ')
else: print('Конец игры')
