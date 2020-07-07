#!/user/bin/env python3

import threading
from datetime import datetime
import psutil
import netifaces as ni
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

#Interval helper
def setInterval(func, time):
  def runner():
    e = threading.Event()
    while not e.wait(time):
      func()
  t = threading.Thread(target=runner)
  t.start()
  return t

#serial
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

#System network
eth0_ip = "9.9.9.9"
wlan0_ip = "9.9.9.9"
def updateIps():
  global eth0_ip
  global wlan0_ip
  #eth0_ip = ni.ifaddresses("eth0")[ni.AF_INET][0]["addr"]
  eth0 = ni.ifaddresses("eth0")
  if ni.AF_INET in eth0:
    eth0_ip = eth0_ip[ni.AF_INET][0]["addr"]
  else:
    eth0_ip = "--"
  wlan0 = ni.ifaddresses("wlan0")
  if ni.AF_INET in wlan0:
    wlan0_ip = ni.ifaddresses("wlan0")[ni.AF_INET][0]["addr"]
  else:
    wlan0_ip = "--"

#System stats
used_cpu = "0.0%"
used_memory = "0.0%"
current_time = "00:00"
def updateSystemStats():
  global used_cpu
  global used_memory
  global current_time
  used_cpu = str(psutil.cpu_percent()) + "%"
  used_memory = str(psutil.virtual_memory().percent) + "%"
  current_time = datetime.now().strftime("%H:%S")
  showSystemStats()

def showSystemStats():
  print("CPU: " + used_cpu)
  print("RAM: " + used_memory)
  print("Hora: " + current_time)
  print("eth0: " + eth0_ip)
  print("wlan0: " + wlan0_ip)
  with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((3, 5), "Hora: " + current_time, fill="white")
    draw.text((3, 15), "CPU: " + used_cpu, fill="white")
    draw.text((3, 25), "RAM: " + used_memory, fill="white")
    draw.text((3, 35), "eth0: " + eth0_ip, fill="white")
    draw.text((3, 45), "wlan0: " + wlan0_ip, fill="white")

#exec
updateIps()

#Intervals
setInterval(updateSystemStats, 5)
setInterval(showSystemStats, 1)
