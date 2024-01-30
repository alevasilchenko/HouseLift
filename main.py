# Данная программа имитирует движение кабины лифта по этажам многоэтажного дома.

# Импортируем функцию randint для случайного задания начального положения кабины лифта.
# Импортируем функцию sleep для имитации плавного перемещения кабины от этажа к этажу.

from random import randint
from time import sleep

# Вводим глобальную переменную game_over, служащую признаком окончания работы программы.
# Для завершения следует после вызова пустой кабины лифта указать тот же этаж назначения,
# на котором уже находится кабина.

game_over = False

# Объявляем класс House с тремя атрибутами и одним методом.
# Атрибуты класса:
#     количество этажей здания (передается из глобальной переменной num_floors);
#     текущее местоположение кабины лифта (при создании экземпляра класса генерируется случайным образом);
#     признак пустой кабины (т.е. лифт вызывается) или непустой кабины (т.е. лифт перевозит).
# Метод lift_go принимает в качестве параметра номер этажа, с которого либо вызвали лифт
# (если кабина пустая), либо на который требуется осуществить перевозку (если кабина непустая).
# В зависимости от этого признака в консоль выводятся либо приветственные сообщения,
# либо рекомендации по соблюдению техники безопасности )))


class House:

    def __init__(self):
        self.numberOfFloors = num_floors
        self.lift_position = randint(1, self.numberOfFloors)
        self.lift_empty = True

    def lift_go(self, to_floor):
        if (not self.lift_empty) and (self.lift_position == to_floor):
            global game_over
            game_over = True
            print('Спасибо, что покатались на нашем лифте!')
            return
        if self.lift_position < to_floor:
            step = 1
        elif self.lift_position > to_floor:
            step = -1
        else:
            step = 0
        if self.lift_empty:
            print('Ожидайте, пожалуйста!')
        else:
            print('Пристегните ремни!')
        print('Текущий этаж:', end=' ')
        while self.lift_position != to_floor:
            print(self.lift_position, end=' -> ')
            sleep(1)
            self.lift_position = self.lift_position + step
        else:
            print(self.lift_position, end='')
        sleep(2)
        print()
        if self.lift_empty:
            print('Входите, пожалуйста!')
        else:
            print('До свидания, приходите ещё!')


print()

# В начале работы пользователь задаёт количество этажей в доме.
# Если их будет задано меньше двух, бесконечный цикл не завершится.

while True:
    num_floors = int(input('Сколько в доме этажей? '))
    if num_floors < 2:
        print('Здесь лифт не нужен!')
        continue
    else:
        break

# Инициализируется объект класса House

any_house = House()

# До появления признака завершения работы (когда номера этажей вызова и назначения совпадут)
# будет выполняться цикл последовательных вызовов и перевозок с интерактивными запросами
# номеров этажей у пользователя.

# Предусмотрена проверка ввода некорректных номеров этажей (однако без проверки на "абракадабру").

# В теле метода lift_go в консоль выводится протокол движения кабины лифта.

# После завершения очередной перевозки стартовое местоположение кабины соответствует последнему прибытию.

# Тому, кто всё это прочитал, желаю благополучия во всех начинаниях!
# Впрочем, желаю того же и всем остальным!

while not game_over:
    print()
    print('Кабина лифта находится на этаже №', any_house.lift_position)
    while True:
        from_number = int(input('C какого этажа вызываем лифт? '))
        if not 1 <= from_number <= num_floors:
            print('Такого этажа в этом доме нет!')
            continue
        else:
            break
    print('Лифт вызван с этажа №', from_number)
    any_house.lift_go(to_floor=from_number)
    while True:
        to_number = int(input('На какой этаж поедем? '))
        if not 1 <= to_number <= num_floors:
            print('Такого этажа в этом доме нет!')
            continue
        else:
            break
    any_house.lift_empty = False
    any_house.lift_go(to_number)
    any_house.lift_empty = True
    sleep(3)
