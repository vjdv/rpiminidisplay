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
    title_text(draw, margin, width, text=interface + " " + data[0])
    print(data)
    draw.text((margin, 25), text="Rx: " + data[1], font=tiny_font, fill="white")
    draw.text((margin, 40), text="Tx: " + data[2], font=tiny_font, fill="white")

def showWlan(draw, width, height):
    showStats("wlan0", draw, width, height)

def showEth(draw, width, height):
    showStats("eth0", draw, width, height)
