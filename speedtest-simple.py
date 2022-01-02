#!/usr/bin/python3

import subprocess
import json
import time
from pprint import pprint

speedtest_p = subprocess.run(
    ["/pack/SpeedTest/SpeedTest", "--output=json"], 
    capture_output=True, text=True
) 
speedtest_d = json.loads(speedtest_p.stdout)

# speedtest_d = {'_': 'all ok',
#  'client': {'ip': '80.166.182.3',
#             'isp': 'TDC Danmark',
#             'lat': '55.6514',
#             'lon': '12.2926'},
#  'download': '1044262177.735848',
#  'jitter': '4',
#  'ping': '11',
#  'server': {'distance': '228.662',
#             'host': 'bck-speedtest-1.tele2.net:8080',
#             'latency': '11',
#             'name': 'Gothenburg',
#             'sponsor': 'Tele2'},
#  'servers_online': '10',
#  'upload': '117524793.230421'}
#pprint(speedtest_d)

print("{DT} | {HOST} | Downlink={DL:.1f}Mb/s | UPLINK={UL:.1f}Mb/s".format(
    DT=time.strftime('%d.%m.%Y %X'),
    HOST=speedtest_d["server"]["host"],
    DL=float(speedtest_d["download"])/1000000,
    UL=float(speedtest_d["upload"])/1000000,
))
