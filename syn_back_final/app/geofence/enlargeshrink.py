import json
import numpy as np
import paho.mqtt.client as mqtt
import time
from app.models import SpeedRange, SpeedRangeSchema, User, MqttTopics, MqttTopicsSchema
from app import db
from flask import jsonify, request, Flask, session, send_from_directory, url_for

newX = []  # new x coordinates for enlarge/shrink
newY = []
enlarge_shrink = []

"""
      This function takes the coordinates of the AGV, the coordinates of the
      geofence and the upper, lower limit of speed , offset value as input from the user and returns enlarged/shrunk coordinates around the AGV as per the speed of the AGV 
      
      :param rxl: list of x coordinates of the geofence in the local frame
      :param ryl: list of y coordinates of the robot in local frame
      :param Agv_name: The of the Robot 
      :param off_set: offset value for the geofence polygon
      :param q: Agv speed 
      :param client: mqtt client
      :param Geofence_ID: Name of the geofence assigned to the robot 
"""


def Enlargeshrink(upper,lower, off_set, client, Agv_name, Geofence_id, q, rxl, ryl):
    
    # Enlarge and shrink algorithm
    print("--------Enlarge---------")
    coordinates_ensh = {  # json data to be published to new data MapAreas/Geofence topic to enlarge or shrink coordinates
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Polygon", "coordinates": [enlarge_shrink]},
             "properties": {
                    "name": Geofence_id,
                    "isRelative": True,
                    "relativeItem": Agv_name,
                    "mqtt_settings_geofence": [],
                    "mqtt_settings_warningZone": [],
                    "zone_width": None,
                    "direction": 0,
                    "neighbours": [],
                    "isEnabled": True,
                    "disableIfFireAlarm": False,
                    "ignoredTags": [],
                    "waitingZoneNarrowArea": None,
                    "type": "geofence",
                    "event": None,
                },
            }
         ],
    }


    def normalizeVec(rxl, ryl):
        distance = np.sqrt(rxl * rxl + ryl * ryl)
        return rxl / distance, ryl / distance  # returning normalized vector

    def makeOffsetPoly(rxl, ryl, num, outer_ccw=1):
        num_points = len(rxl)

        for val in range(num_points):
            
            prev = (val + num_points - 1) % num_points
            
            next = (val + 1) % num_points
            

            vnX = rxl[next] - rxl[val]
            vnY = ryl[next] - ryl[val]
            vnnX, vnnY = normalizeVec(vnX, vnY)
            nnnX = vnnY
            nnnY = -vnnX

            vpX = rxl[val] - rxl[prev]
            vpY = ryl[val] - ryl[prev]
            vpnX, vpnY = normalizeVec(vpX, vpY)
            npnX = vpnY * outer_ccw
            npnY = -vpnX * outer_ccw

            bisX = (nnnX + npnX) * outer_ccw
            bisY = (nnnY + npnY) * outer_ccw

            bisnX, bisnY = normalizeVec(bisX, bisY)
            bislen = -(num) / np.sqrt(1 + nnnX * npnX + nnnY * npnY)

            newX.append(rxl[val] + bislen * bisnX)
            newY.append(ryl[val] + bislen * bisnY)

    def float_range(start, stop, step):
        assert step > 0.0
        total = start
        compo = 0.0
        while total <= stop:
            yield total
            y = step - compo
            temp = total + y
            tempr = round(temp, 4)
            compo = (tempr - total) - y
            total = tempr
    i=0
    while True:
        agv_speed = q.get()
        print("agv_speed",agv_speed)
        count = len(upper)
        while i < count:
            con = list(float_range(lower[i], upper[i], 0.001))
            if agv_speed in con:
              val = i
              num = off_set[val]
              print("offset", num)
              i = 0
              break

            else:
              i += 1

        enlarge_shrink.clear()
        makeOffsetPoly(rxl, ryl, num)
        

        for ex, ey in zip(newX, newY):
            enlarge_shrink.append([ex, ey])
        
        client.publish("MapAreas/Geofence", payload=json.dumps(coordinates_ensh))
        print("published to MapAreas")
        newX.clear()
        newY.clear()
        time.sleep(1)

