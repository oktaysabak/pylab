import csv
from math import sqrt, pi, sin, cos, atan2
RADIUS = 6371
RED_MIN = 20
RED_MAX = 30
GREEN_MIN = 35
GREEN_MAX = 50
BLUE_MIN = 20
BLUE_MAX = 80
branchs = [[41.049792,29.003031],[41.069940,29.019250],[41.049997,29.026108]]
orders = []
with open('orders.csv') as order_file:
    csv_reader = csv.reader(order_file, delimiter=',')

    for row in csv_reader:
        
        orders.append([float(x) for x in row])

def degree2Radian(degree):
    return degree*(pi/180)


def getDistance(branch, order):
    lat = degree2Radian(order[0]-branch[0])
    lng = degree2Radian(order[1]-branch[0])

    haversine_a = sin(lat/2)*sin(lat/2) + cos(degree2Radian(branch[0]))*cos(degree2Radian(order[0]))* sin(lng/2)* sin(lng/2)
    haversine_c = 2* atan2(sqrt(haversine_a),sqrt(1-haversine_a))

    return RADIUS*haversine_c
red = []
green = []
blue = []
for o in orders:
    red.append(getDistance(branchs[0],o))
    green.append(getDistance(branchs[1],o))
    blue.append(getDistance(branchs[2],o))

red_orders = []
green_orders = []
blue_orders = []
for i,v in enumerate(red):
    print(str(i)+". red {} green {} blue {} ".format(*[v,green[i], blue[i]]))

# print("redMax::",str(max(red)), "redMin::",str(min(red)))
# print("greenMax::",str(max(green)), "greenMin::",str(min(green)) )
# print("blueMax::",str(max(blue)), "blueMin::",str(min(blue)) )