# Mini Display for Raspberry Pi

Show useful information on a 128x64 OLED display connected to a headless Raspberry Pi server.

## The solved problem

I'm running a headless Raspberry Pi 4 as development server, which I use at home, work or even while traveling. Different networks gives you different IPs and is not always posible to use a static IP, so how can I know what IP to connect? Attach a mini OLED display to your Pi so you can see its current IP.

Good! But I don't like to plug out the cable without properly shutdown my Pi. Solution: add a button to shut it down (or ssh to it and execute the command).

## Features

- Show your assigned IP
- Clean shutdown

## Extras

- Systems stats
- Time

## Instructions

```bash
#Clone the repo
git clone https://github.com/vjdv/rpiminidisplay.git
#go into project
cd rpiminidisplay
#install dependencies
./install.sh
#execute
python3 display.py
```
