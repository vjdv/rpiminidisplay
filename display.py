#!/user/bin/env python

import threading
from datetime import datetime
import psutil

def setInterval(func, time):
  def runner():
    e = threading.Event()
    while not e.wait(time):
      func()
  t = threading.Thread(target=runner)
  t.start()
  return t

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
  print "CPU: " + used_cpu
  print "RAM: " + used_memory
  print "Hora: " + current_time

#Intervals
setInterval(updateSystemStats, 5)
setInterval(showSystemStats, 1)
