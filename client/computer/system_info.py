import psutil

def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        result = {}
        percent = battery.percent
        result["percent"] = percent
        secsleft = battery.secsleft
        plugged = battery.power_plugged
        result["plugged"] = plugged
        if secsleft == psutil.POWER_TIME_UNLIMITED:
            result["time"] = -2
        elif secsleft == psutil.POWER_TIME_UNKNOWN:
            result["time"] = -1
        else:
            result["time"] = secsleft
        return result
    else:
        return None

if __name__ == "__main__":
    print(get_battery_info())
