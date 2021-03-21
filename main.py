N = input('Пожалуйста, введите номер карты: ')
while len(N) > 16 or len(N) < 13:
    N = input('Номер должен иметь от 13 до 16 цифр, введите номер еще раз: ')


def kind_of_card(N):
    if N[0] == '4':
        return 'Visa card'
    elif N[0] == '5':
        return 'Mastercard card'
    elif N[0:2] == '37':
        return 'American Express card'
    elif N[0] == '6':
        return 'Discover card'
    elif N[0] == '2':
        return 'Карта Мир'
    else:
        return 'Карты такого вида нет в базе данных'


print('Номер карты: {}-{}-{}-{}'.format(N[:4], N[4:8], N[8:12], N[12:]))


def luhn(ccn):
    c = [int(x) for x in ccn[::-2]]  # находим все числа стоящие на НЕчетных позициях в обратном порядке и создаем
    # из них список
    u2 = [((2 * int(y)) // 10) + ((2 * int(y)) % 10) for y in ccn[-2::-2]]  # находим все числа стоящие на четных
    # позициях в обратном порядке и проводим алгоритм, записывая результат в список (3,4 пункты)

    return sum(c + u2) % 10 == 0


if luhn(N):
    print('Является действительным номером карты')
    print(kind_of_card(N))
else:
    print('Не является действительным номерм карты')
