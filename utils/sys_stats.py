import threading
import time
import psutil
from utils.common import bytes2human, tiny_font

class Updater(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.cpu_data = []
        self.current_cpu = "0"
        self.used_ram = "0MB"
        self.cpu_temperature = "0"
    def run(self):
        global flag
        global val     #made global here
        while True:
            #cpu
            cpu = psutil.cpu_percent()
            self.current_cpu = str(cpu) + "%"
            #cpu history
            if len(self.cpu_data) == 200:
                self.cpu_data.pop(0)
            self.cpu_data.append(cpu)
            #ram
            ramStat = psutil.virtual_memory()
            self.used_ram = bytes2human(ramStat.used)
            #temperature
            try:
                with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp:
                    self.cpu_temperature = str(int(temp.read()[:2])) + "°C"
            except:
                self.cpu_temperature = "0°C"
            #wait
            time.sleep(1)

data = Updater("updater_thread")
data.start()

#show stats
def showCpuStats(draw, width, height):
    maxHeight = height - 15
    size = len(data.cpu_data)
    draw.rectangle((0, 12, width-1, height-1), fill="black", outline="white")
    #draw history
    for i in range(size):
        cpu = data.cpu_data[size - 1 - i]
        cpu = round(maxHeight * cpu / 100)
        draw.point((width - 2 - i, height - 1 - cpu), fill="white")
    #draw current cpu usage
    cpuwidth = draw.textsize(data.current_cpu)[0]
    draw.rectangle((0, 12, cpuwidth + 1, 22), fill="white", outline="white")
    draw.text((1,12), data.current_cpu, fill="black")
    #draw ram
    draw.text((0,0), "RAM " + data.used_ram, fill="white", font=tiny_font)
    #draw temp
    tempwidth = draw.textsize(data.cpu_temperature)[0]
    draw.text((width - tempwidth - 1, 0), data.cpu_temperature, fill="white")
