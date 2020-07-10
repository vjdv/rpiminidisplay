#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
import threading
import math
from datetime import datetime
import psutil
import netifaces as ni
from PIL import ImageFont
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

#Font helper
def make_font(name, size):
  font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "fonts", name))
  return ImageFont.truetype(font_path, size)

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
cpu_temp = "--"
used_memory = "0.0%"
current_time = "00:00"
def updateSystemStats():
  global used_cpu
  global cpu_temp
  global used_memory
  global current_time
  used_cpu = str(psutil.cpu_percent()) + "%"
  temps = psutil.sensors_temperatures()
  if not temps:
    cpu_temp = "0 °C"
  else:
    for name, entries in temps.items():
        print(name)
        for entry in entries:
          cpu_temp = str(math.trunc(entry.current)) + " °C"
          break
        break
  used_memory = str(psutil.virtual_memory().percent) + "%"
  current_time = datetime.now().strftime("%I:%M%p")
  #showSystemStats()

clockFont = make_font("FreePixel.ttf", 30)
def showClock():
  with canvas(device) as draw:
    draw.text((10,20), current_time, fill="white", font=clockFont)

def showCpuStats():
  with canvas(device) as draw:
    draw.text((0,0), "CPU:", fill="white")
    draw.text((5,10), used_cpu, fill="white")
    draw.text((0,22), "RAM:", fill="white")
    draw.text((5,32), used_memory, fill="white")
    draw.text((0,44), "Temp:", fill="white")
    draw.text((5,54), cpu_temp, fill="white")

def showNetStats():
  with canvas(device) as draw:
    draw.text((0,10), "eth0:", fill="white")
    draw.text((0,20), eth0_ip, fill="white")
    draw.text((0,40), "wlan0:", fill="white")
    draw.text((0,50), wlan0_ip, fill="white")

def showSystemStats():
  print("CPU: " + used_cpu)
  print("CPU Temp: " + cpu_temp)
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
setInterval(updateIps, 30)
setInterval(updateSystemStats, 5)
setInterval(showClock, 1)
