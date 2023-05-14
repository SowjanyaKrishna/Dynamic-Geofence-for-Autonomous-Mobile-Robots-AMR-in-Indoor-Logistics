import numpy as np
import geopandas as gpd
from shapely.geometry import mapping
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon

def Geo2Array(geo, skip=0):
    result = []
    all_coords = mapping(geo)["coordinates"]
    array = np.array(all_coords)
    result=list(array[0])
    if skip != 0:
        result = result[0::skip]
    return result

def MultiPolygon2Polygon(data):
    outdf = gpd.GeoDataFrame(columns=data.columns)
    for idx, row in data.iterrows():
        if type(row.geometry) == Polygon:
            outdf = outdf.append(row,ignore_index=True)
        if type(row.geometry) == MultiPolygon:
            multdf = gpd.GeoDataFrame(columns=data.columns)
            recs = len(row.geometry)
            multdf = multdf.append([row]*recs,ignore_index=True)
            for geom in range(recs):
                multdf.loc[geom,'geometry'] = row.geometry[geom]
            outdf = outdf.append(multdf,ignore_index=True)
    return outdf
            
def minValue(data, index):
    return min(data, key = lambda t: t[index])

def maxValue(data, index):
    return max(data, key = lambda t: t[index])

def PointInPolygon(point, polygon):
    minX = minValue(polygon, 0)[0]
    minY = minValue(polygon, 1)[1]
    maxX = maxValue(polygon, 0)[0]
    maxY = maxValue(polygon, 1)[1]
    x = point[0]
    y = point[1]
    if x > maxX or x < minX or y > maxY or x < minY:
        return False
    sumAngle = 0
    i = 0
    j = len(polygon)-1
    inside = False
    while i < len(polygon):
        if x==polygon[i][0] and y==polygon[i][1]:
                return True
        if(((polygon[i][1] > y) != (polygon[j][1] > y)) and ( x <= (polygon[j][0]-polygon[i][0])*(y-polygon[i][1])/(polygon[j][1]-polygon[i][1])+polygon[i][0])):
            if inside:
                inside = False
            else:
                inside = True
        j = i
        i += 1
    return inside
