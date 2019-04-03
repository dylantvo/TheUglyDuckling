from nav.gridMovement import GridMovement
from nav.grid import Grid
import queue, serial, time, math
import json
from constants import strr,strl, fwd
from misc import get_sensor_data

def corrected_angle(angle, dist):
    angle = 180 - angle
    a = math.sqrt(math.pow(dist,2) + math.pow(3.5, 2) - 2*dist*3.5*math.cos(math.radians(angle)))
    angle_c = math.asin(math.sin(math.radians(angle))*dist/a)
    return math.ceil(180-angle-math.degrees(angle_c))
    
def map_JSON(filename, movement):
    with open(filename, encoding='utf-8') as data_file:
      data = json.loads(data_file.read())
    size = data['size']
    x_arr = data['x coords']
    y_arr = data['y coords']
    for i in range(size):
      movement.map_target((x_arr[i], y_arr[i]))
angle = 0
dist = 0

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
time.sleep(1)
q = queue.Queue()
grid = Grid(8,8)
movement = GridMovement(grid, ser)
#map_JSON('mar1.json', movement)



movement.drop()
print(get_sensor_data(ser))
movement.reset_servo()
