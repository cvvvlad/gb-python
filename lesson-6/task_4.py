class Car:
    _car_type = 'Автомобиль'
    speed = 0
    color = 'красный'
    name = 'BMW'
    is_police = False
    directions = {
        'r': 'направо',
        'l': 'налево'
    }

    def __init__(self, name, color='красный'):
        self.name = name
        self.color = color

    def _car_info_string(self):
        return f"{self.color} {self._car_type} {self.name}"

    def go(self):
        print(f"{self._car_info_string()} начинает движение")

    def stop(self):
        print(f"{self._car_info_string()} останавливается")

    def turn(self, direction):
        print(f"{self._car_info_string()} поворачивает {self.directions[direction]}")

    def show_speed(self):
        print(f"{self._car_info_string()} едет со скоростью: {self.speed} км/ч")


class TownCar(Car):

    def __init__(self, name, color):
        super(TownCar, self).__init__(name, color)
        self._car_type = 'Городской автомобиль'

    def show_speed(self):
        speed_warn = ''
        if self.speed > 60:
            speed_warn = f'ВНИМАНИЕ! Скорость превышена на {self.speed - 60} км/ч'
        print(f"{self._car_info_string()} едет со скоростью {self.speed} км/ч. {speed_warn}")


class SportCar(Car):

    def __init__(self, name, color):
        super(SportCar, self).__init__(name, color)
        self._car_type = 'Спорткар'


class WorkCar(Car):

    def __init__(self, name, color):
        super(WorkCar, self).__init__(name, color)
        self._car_type = 'Рабочий автомобиль'

    def show_speed(self):
        speed_warn = ''
        if self.speed > 40:
            speed_warn = f'ВНИМАНИЕ! Скорость превышена на {self.speed - 40} км/ч'
        print(f"Рабочий автомобиль марки {self.name} едет на разгрузку со скоростью {self.speed} км/ч. {speed_warn}")


class PoliceCar(Car):

    def __init__(self, name, color):
        super(PoliceCar, self).__init__(name, color)
        self._car_type = 'Полицейский автомобиль'
        self.is_police = True


police_car = PoliceCar("Ford Explorer", 'чёрный')
police_car.speed = 20
police_car.show_speed()
police_car.turn('l')

criminal_town_car = TownCar('BMW X8', 'синий')
criminal_town_car.speed = 90
criminal_town_car.show_speed()

police_car.speed = 70
police_car.show_speed()
police_car.speed = 90
police_car.show_speed()

criminal_town_car.turn('r')
police_car.turn('r')
criminal_town_car.turn('l')
police_car.turn('l')
criminal_town_car.stop()
police_car.stop()

police_car.speed = 20
police_car.show_speed()
police_car.turn('r')
sport_car = SportCar('Bugatti Chiron', 'желтый')
sport_car.speed = 50
sport_car.show_speed()
police_car.turn('r')
police_car.turn('l')

criminal_work_car = WorkCar('Газель NEXT', 'белый')
criminal_work_car.speed = 55
criminal_work_car.show_speed()
police_car.speed = 55
police_car.show_speed()
criminal_work_car.stop()
police_car.stop()
