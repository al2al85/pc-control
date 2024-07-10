class BatteryInfo:
    def __init__(self, percent, plugged, time):
        self.percent = percent
        self.plugged = plugged
        self.time = time
    def get_percent(self):
        return self.percent
    def get_plugged(self):
        return self.plugged
    def get_time(self):
        return self.time
        