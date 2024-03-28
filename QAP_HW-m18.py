# Объявление переменных, в которых хранится стоимость билетов и значение количества билетов.
ticket_cost_18_24, ticket_cost_25, ticket_count = 990, 1390, 0

# Количество билетов не должно быть меньше или равно нулю (изначально равно 0 - условие для цикла While).
while ticket_count <= 0:

# Приветствие, запрос количества билетов и определение размера скидки, в зависимости от количества билетов.
    ticket_count = int(input('Здравствуйте! Сколько билетов на конференцию Вы хотите приобрести:\t'))
    if ticket_count <= 0:
        print('Количество билетов не должно быть равно 0, и, тем более принимать отрицательные значения!')
discount = 10 if ticket_count >= 3 else 0

# Сумма к оплате изначально равна нулю (условие для цикла While).
total_cost = 0
while total_cost == 0:

# Запрос возраста поситителя.
    age = int(input('Пожалуйства, укажите Ваш возраст:\t'))

# Выполнение логики условий для расчета итоговой стоимости билетов.
    if 18 <= age < 25 and ticket_count >= 3:
        total_cost = ticket_count * (ticket_cost_18_24 - (ticket_cost_18_24 / discount))
        print('Всего к оплате:', round(total_cost), 'рублей')
    elif 18 <= age < 25 and ticket_count < 3:
        total_cost = ticket_count * ticket_cost_18_24
        print('Всего к оплате:', round(total_cost), 'рублей')
    elif 25 <= age < 99 and ticket_count >= 3:
        total_cost = ticket_count * (ticket_cost_25 - (ticket_cost_25 / discount))
        print('Всего к оплате:', round(total_cost), 'рублей')
    elif 25 <= age < 99 and ticket_count < 3:
        total_cost = ticket_count * ticket_cost_25
        print('Всего к оплате:', round(total_cost), 'рублей')
    elif 14 <= age < 18:
        print('Поздравляем! Вам разрешено посетить конференцию БЕСПЛАТНО!')
        break
    else:
        print('Вам не может быть столько лет (это слишком мало или слишком много)! Повторите ввод:\t')




