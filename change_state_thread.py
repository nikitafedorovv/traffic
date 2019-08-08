import threading

LIGHT_ON_STR = '⚫'
LIGHT_OFF_STR = '⚪'


class StateThread(threading.Thread):
    def __init__(self, greenState, yellowState, redState, trafficLight):
        threading.Thread.__init__(self)
        self.greenState = greenState
        self.yellowState = yellowState
        self.redState = redState
        self.trafficLight = trafficLight

    def run(self):
        state = self.trafficLight.get_current_state()
        self.changeState(state)

        while True:
            state = self.trafficLight.process_and_get_new_state()
            self.changeState(state)

    def changeState(self, state):
        self.greenState.config(text=LIGHT_ON_STR if state[0] else LIGHT_OFF_STR)
        self.yellowState.config(text=LIGHT_ON_STR if state[1] else LIGHT_OFF_STR)
        self.redState.config(text=LIGHT_ON_STR if state[2] else LIGHT_OFF_STR)
