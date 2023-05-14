import time
import math
import shapely.geometry
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely import geometry
import queue
from app.geofence.coordinateconversion import localtoglobal_x
from app.geofence.coordinateconversion import localtoglobal_y

gbl_geofence_coords= []
agv_pos = []
rxl = []
ryl = []
x = 0
y = 0
w = queue.LifoQueue()
"""
      This function takes the coordinates of the tag, the coordinates of the AGV, the coordinates of the
      geofence and the offset value as input and returns the zone in which the tag is present
      
      :param rxl: list of x coordinates of the geofence in the local frame
      :param ryl: list of y coordinates of the robot in local frame
      :param agv_pos: This is the position of the AGV in the global frame
      :param x: x coordinate of the tag
      :param y: y coordinate of the tag
      :param zone_offset_value: This is the value that determines the size of the red zone. The default
      value is 0.2
"""


def Tag_detection(rxl, ryl, zone_offset_value, c, a, b, w,):
      print("--------Tag---------")
      print("zoneoffset", zone_offset_value)
      while True:
            
            agv_pos= c.get()
            x= a.get()
            y= b.get()
      
            inside_purple = False
            inside_red = False

            gbx= localtoglobal_x(rxl, agv_pos, ryl)
            #print("gbx=", gbx)
            gby= localtoglobal_y(rxl, agv_pos, ryl)
            #print("gby=", gby)

            tag_point = Point(x, y)
            gbl_geofence_coords.clear()
            for gx, gy in zip(gbx, gby):
                  gbl_geofence_coords.append([gx, gy])
            #print( "gbl_geofence_coords",gbl_geofence_coords )

            lines = [
                  [gbl_geofence_coords[i - 1], gbl_geofence_coords[i]]
                  for i in range(len(gbl_geofence_coords))]

            factor = zone_offset_value

            xs = [i[0] for i in gbl_geofence_coords]
            ys = [i[1] for i in gbl_geofence_coords]
            x_center = 0.5 * min(xs) + 0.5 * max(xs)
            y_center = 0.5 * min(ys) + 0.5 * max(ys)

            min_corner = geometry.Point(min(xs), min(ys))
            max_corner = geometry.Point(max(xs), max(ys))
            center = geometry.Point(x_center, y_center)
            shrink_distance = center.distance(min_corner) * factor

            my_polygon = geometry.Polygon(gbl_geofence_coords)
            my_polygon_shrunken = my_polygon.buffer(-shrink_distance)

            inside_purple = my_polygon.contains(tag_point)
            inside_red = my_polygon_shrunken.contains(tag_point)
            if inside_purple == True:
                  if inside_red == True:
                        action = {"warning":"Tag is inside the geofence-red zone"}
                        print("warning:Tag is inside the geofence-red zone")

                  else:
                        action = {"warning":"Tag is inside the geofence-blue zone"}
                        print("warning:Tag is inside the geofence-blue zone")
            else:
                  action = {"warning":"Tag is outside the geofence"}
                  print("warning:Tag is outside the geofence")
            
            w.put(action)
            gbx.clear()
            gby.clear()  
            time.sleep(1)

