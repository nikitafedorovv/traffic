import random


class TrafficLight:
    def __init__(self):
        pass

    def get_state(self):
        return [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]

