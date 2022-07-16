import sys
import pygame
from pygame.locals import *

colors = {
    "RED": (255, 0, 0),
    "WHITE": (255, 255, 255),
    "BLACK": (50, 50, 50),
    "YELLOW": (255, 200, 0),
    "GREEN": (0, 255, 0)
}


class TrafficLight:
    color = 'red'
    __color_changed_time = 0
    __color_times_ms = {
        'red': 7000,
        'yellow': 2000,
        'green': 3000
    }

    def running(self, current_time_ms):
        delta_time = current_time_ms - self.__color_changed_time
        if self.color == 'red' and delta_time >= self.__color_times_ms['red']:
            self.set_color('yellow')
        elif self.color == 'yellow' and delta_time >= self.__color_times_ms['yellow']:
            self.set_color('green')
        elif self.color == 'green' and delta_time >= self.__color_times_ms['green']:
            self.set_color('red')

    def set_color(self, new_color):
        self.color = new_color
        self.__color_changed_time = pygame.time.get_ticks()


class TrafficLightRenderer:

    def __init__(self, surface, traffic_light):
        self.__surface = surface
        self.__traffic_light = traffic_light

    def draw(self):
        red_color = colors["RED"] if self.__traffic_light.color == 'red' else colors["BLACK"]
        yellow_color = colors["YELLOW"] if self.__traffic_light.color == 'yellow' else colors["BLACK"]
        green_color = colors["GREEN"] if self.__traffic_light.color == 'green' else colors["BLACK"]

        pygame.draw.circle(self.__surface, red_color, (150, 88), 30)
        pygame.draw.circle(self.__surface, yellow_color, (150, 150), 30)
        pygame.draw.circle(self.__surface, green_color, (150, 212), 30)


class MainGame:

    def __init__(self):
        pygame.init()
        self.__surface = pygame.display.set_mode((300, 300))
        self.__surface.fill(colors["WHITE"])
        pygame.display.set_caption("TrafficLight")
        self.__fps = 30
        self.__fps_clock = pygame.time.Clock()
        self.__traffic_light = TrafficLight()
        self.__traffic_light_renderer = TrafficLightRenderer(self.__surface, self.__traffic_light)

    def run(self):
        while True:
            current_time_ms = pygame.time.get_ticks()
            self.__traffic_light.running(current_time_ms)
            self.__traffic_light_renderer.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.__fps_clock.tick()


MainGame().run()
