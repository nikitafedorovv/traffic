import time

from util import as_array


class TrafficLight:
    __state = '011'

    def __init__(self):
        pass

    def get_state(self):
        state_config = STATE_MACHINE[self.__state]
        time.sleep(state_config['sleep_time_seconds'])
        self.__state = state_config['next_state']
        return as_array(self.__state)


STATE_MACHINE = {'100': {'sleep_time_seconds': 4, 'next_state': '110'},
                 '110': {'sleep_time_seconds': 2, 'next_state': '001'},
                 '001': {'sleep_time_seconds': 4, 'next_state': '011'},
                 '011': {'sleep_time_seconds': 2, 'next_state': '100'}
                 }
