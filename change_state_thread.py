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
        self.change_state(state)

        while True:
            state = self.trafficLight.process_and_get_new_state()
            self.change_state(state)

    def change_state(self, state):
        self.greenState.config(fg='green' if state[0] else '#B8F6BD')
        self.yellowState.config(fg='yellow' if state[1] else '#FCFFD0')
        self.redState.config(fg='red' if state[2] else '#E9AEAA')
