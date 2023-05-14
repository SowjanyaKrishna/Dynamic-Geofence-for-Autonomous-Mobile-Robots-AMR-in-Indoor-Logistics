import math

rxl=[]
ryl=[]
gbx=[]
gby=[]

def globaltolocal_x(gx, agv_pos, gy):
    for i in range(len(gx)):
        rxl.append((gx[i] - agv_pos[0]) * (math.cos(agv_pos[2])) + (gy[i] - agv_pos[1]) * (math.sin(agv_pos[2])))
    return rxl
    
def globaltolocal_y(gx, agv_pos, gy):
    for i in range(len(gx)):
        ryl.append(-(gx[i] - agv_pos[0]) * (math.sin(agv_pos[2])) + (gy[i] - agv_pos[1]) * (math.cos(agv_pos[2])))
    return ryl

def localtoglobal_x(rxl, agv_pos, ryl):
    for i in range(len(rxl)):
        gbx.append(rxl[i] * (math.cos(agv_pos[2])) - ryl[i] * (math.sin(agv_pos[2])) + agv_pos[0])
    return gbx

def localtoglobal_y(rxl, agv_pos, ryl):
    for i in range(len(rxl)):
        gby.append(rxl[i] * (math.sin(agv_pos[2])) + ryl[i] * (math.cos(agv_pos[2])) + agv_pos[1])
    return gby
