#!/user/bin/env python

import threading
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
global used_cpu
global used_memory
used_cpu = "0.0%"
used_memory = "0.0%"
def updateSystemStats():
  global used_cpu
  global used_memory
  used_cpu = str(psutil.cpu_percent()) + "%"
  used_memory = str(psutil.virtual_memory().percent) + "%"
  showSystemStats()

def showSystemStats():
  print "CPU: " + used_cpu
  print "RAM: " + used_memory

#Intervals
setInterval(updateSystemStats, 5)
setInterval(showSystemStats, 1)
