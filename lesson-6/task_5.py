class Stationary:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print(f"{self.title}: Запуск отрисовки")


class Pen(Stationary):

    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        print(f"{self.title} пишет")


class Pencil(Stationary):

    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        print(f"{self.title} рисует")


class Handle(Stationary):

    def __init__(self):
        self.title = "Маркер"

    def draw(self):
        print(f"{self.title} помечает")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

marker = Handle()
marker.draw()
