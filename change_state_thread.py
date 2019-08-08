import threading


class StateThread(threading.Thread):
    def __init__(self, greenState, yellowState, redState, trafficLight):
        threading.Thread.__init__(self)
        self.greenState = greenState
        self.yellowState = yellowState
        self.redState = redState
        self.trafficLight = trafficLight

    def run(self):
        while True:
            state = self.trafficLight.get_state()
            self.greenState.config(text=state[0])
            self.yellowState.config(text=state[1])
            self.redState.config(text=state[2])
