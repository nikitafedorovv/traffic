import time

from util import as_array

STATE_MACHINE = {'100': {'sleep_time_seconds': 4, 'next_state': '010'},
                 '010': {'sleep_time_seconds': 2, 'next_state': '001'},
                 '001': {'sleep_time_seconds': 4, 'next_state': '011'},
                 '011': {'sleep_time_seconds': 2, 'next_state': '100'}
                 }


class TrafficLight:
    __state = '011'

    def __init__(self):
        pass

    def process_and_get_new_state(self):
        state_config = STATE_MACHINE[self.__state]
        time.sleep(state_config['sleep_time_seconds'])
        self.__state = state_config['next_state']
        return as_array(self.__state)

    def get_current_state(self):
        return self.__state
