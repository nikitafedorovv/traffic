import time
from util import *
from config import STATES_CONFIG


class TrafficLight:
    __state = [1, 0, 0]

    def __init__(self):
        pass

    def get_state(self):
        state_config = STATES_CONFIG[as_str(self.__state)]
        time.sleep(state_config['delay'])
        self.__state = as_array(state_config['next_state'])
        return self.__state
