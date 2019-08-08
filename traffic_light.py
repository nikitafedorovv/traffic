import time
from config import STATES_CONFIG
from util import as_array


class TrafficLight:
    __state = '011'

    def __init__(self):
        pass

    def get_state(self):
        state_config = STATES_CONFIG[self.__state]
        time.sleep(state_config['sleep_time_seconds'])
        self.__state = state_config['next_state']
        return as_array(self.__state)
