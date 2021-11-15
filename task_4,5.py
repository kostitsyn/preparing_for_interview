"""Скрипт 'Банковский депозит'."""
MONTS_YEAR = 12


def calculate_deposit(summ: float, term: int, fix_pay: float) -> float:
    first_product = {
        'begin_sum': 1000,
        'end_sum': 10000,
        6: 5,
        12: 6,
        24: 5
    }

    second_product = {
        'begin_sum': 10000,
        'end_sum': 100000,
        6: 6,
        12: 7,
        24: 6.5
    }

    third_product = {
        'begin_sum': 100000,
        'end_sum': 1000000,
        6: 7,
        12: 8,
        24: 7.5
    }

    if summ == 1000:
        correct_product = first_product
    else:
        correct_product = [i for i in [first_product, second_product, third_product]
                           if i['begin_sum'] < summ <= i['end_sum']][0]
    deposit_percent = 1 + correct_product[term]/100*term/MONTS_YEAR

    def count_percent():
        total_add_sum = fix_pay * (correct_product[term] - 2) * deposit_percent
        return total_add_sum

    final_sum = summ * deposit_percent
    count_percent()
    return round(final_sum + count_percent(), 2)


print('Расчет депозита')
while True:
    try:
        start_sum, term, fix_pay = tuple(
            input('Введите через пробел начальную сумму, '
                  'срок вклада в месяцах (6, 12, 24)'
                  '\nи ежемесячную сумму пополнения: ').split())
        start_sum, term, fix_pay = float(start_sum), int(term), float(fix_pay)

    except ValueError:
        print('Вы ввели не корректные данные.\n')
    else:
        if term not in (6, 12, 24):
            print('Указан неверный срок вклада.\n')
            continue
        if start_sum < 1000 or start_sum > 1000000:
            print('Указана неверная сумма вклада.\n')
            continue
        result = calculate_deposit(start_sum, term, fix_pay)
        print(f'Сумма вклада на конец срока равна {result}')
        break
