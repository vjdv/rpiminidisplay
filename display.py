#!/user/bin/env python3
# -*- coding: utf-8 -*-

import time
from luma.core.render import canvas
from utils.clock import showClock
from utils.network import showWlan, showEth
from utils.sys_stats import showCpuStats
from utils.opts import get_device

# main
def main():
  width = device.width
  height = device.height
  counter = 1
  duration = 5
  size = 3
  while True:
    step = counter / duration
    with canvas(device) as draw:
      if step <= 1:
        showClock(draw, width, height)
      elif step <= 2:
        showEth(draw, width, height)
      elif step <= 3:
        showWlan(draw, width, height)
    counter = counter + 1
    if counter > (duration * size):
      counter = 1
    time.sleep(1)

try:
  device = get_device()
  main()
except KeyboardInterrupt:
  pass

