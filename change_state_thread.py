import threading


class StateThread(threading.Thread):
    def __init__(self, green_state, yellow_state, red_state, traffic_light):
        threading.Thread.__init__(self)
        self.greenState = green_state
        self.yellowState = yellow_state
        self.redState = red_state
        self.trafficLight = traffic_light

    def run(self):
        state = self.trafficLight.get_current_state()
        self.change_state(state)

        while True:
            state = self.trafficLight.process_and_get_new_state()
            self.change_state(state)

    def change_state(self, state):
        self.greenState.config(fg='#00ff17' if state[0] else '#004f07')
        self.yellowState.config(fg='yellow' if state[1] else '#404500')
        self.redState.config(fg='red' if state[2] else '#5c0600')
