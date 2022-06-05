#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Maxence
#
# Created:     05/06/2022
# Copyright:   (c) Maxence 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests
from datetime import datetime

from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    departures = []
    r = requests.get("https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:SNCF:87286005/departures?datetime=20220605T173520", headers={'Authorization': '<my token>'})
    data = r.json()
    for departure in data["departures"]:
        date = datetime.strptime(departure['stop_date_time']['arrival_date_time'], '%Y%m%dT%H%M%S')
        departures.append(f"{departure['display_informations']['direction']} : {date.strftime('%H:%M:%S')}")
        print(f"depart {departure['display_informations']['direction']}")
    return "\r\n".join(departures)

run(app, host='localhost', port=8080)