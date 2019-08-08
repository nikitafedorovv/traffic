class RoadTrafficState:
    def __init__(self, red, red_yellow, yellow, green):
        self.items = [("Red", red), ("Red Yellow", red_yellow), ("Yellow", yellow), ("Green", green)]
        pass

    def get_items(self):
        return self.items

    

