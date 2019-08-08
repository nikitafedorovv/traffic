import threading


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
        self.greenState.config(text="◯" if state[0] == 0 else "⬤")
        self.yellowState.config(text="◯" if state[1] == 0 else "⬤")
        self.redState.config(text="◯" if state[2] == 0 else "⬤")
