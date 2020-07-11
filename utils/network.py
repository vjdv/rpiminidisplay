import psutil
from utils.common import bytes2human, right_text, title_text, tiny_font

# get interface stats
def interfaceStats(interface):
    address = psutil.net_if_addrs()[interface][0].address
    counters = psutil.net_io_counters(pernic=True)[interface]
    rx = bytes2human(counters.bytes_recv)
    tx = bytes2human(counters.bytes_sent)
    return (address, rx, tx)

# display wlan stats
def showStats(interface, draw, width, height):
    margin = 2
    data = interfaceStats(interface)
    title_text(draw, margin, width, text=data[0])
    print(data)
    draw.text((margin, 20), text=interface, fill="white")
    draw.text((margin, 35), text="Rx: " + data[1], font=tiny_font, fill="white")
    draw.text((margin, 47), text="Tx: " + data[2], font=tiny_font, fill="white")
    #dibuja icono wifi
    if interface.startswith("wlan"):
      draw.pieslice((80,25,125,70), 225, 315, outline="white", fill="white", width=3)
      draw.arc((95,40,110,55), 225, 315, fill="black", width=4)
      draw.arc((85,30,120,65), 225, 315, fill="black", width=5)

def showWlan(draw, width, height):
    showStats("wlan0", draw, width, height)

def showEth(draw, width, height):
    showStats("eth0", draw, width, height)
