from threading import Thread
from datetime import datetime
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        vrag = 100
        day = 0
        while vrag > 0:
            sleep(1)
            vrag = vrag - self.power
            day += 1
            print(f'{self.name} сражается {day}день(дня), осталось {vrag} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')