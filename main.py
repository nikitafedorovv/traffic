from change_state_thread import StateThread
from traffic_light import TrafficLight
from web_gui import MyGuy

if __name__ == '__main__':
    guy = MyGuy()
    thread1 = StateThread(guy.greenState, guy.yellowState, guy.redState, TrafficLight())
    thread1.start()
    guy.root.mainloop()
