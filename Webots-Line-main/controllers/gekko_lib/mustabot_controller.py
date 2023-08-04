"""mustabot_controller controller."""

from controller import Robot
from motor import MOTOR, ENCODER
from sensors import IR, LASER, COLOR
from functions import PID_LINE
from time import time, sleep

# create the Robot instance.
robot = Robot()
leftMotor = None
rightMotor = None
encoder_left = None
encoder_right = None

#initialize the sensor variables
ir_sensors = []
laser_frontal = None
laser_izquierdo = None
laser_derecho = None
color_derecho = None
color_izquierdo = None
potencia1 = None
potencia2 = None
error_line = 0
sum_error_line = 0

status_setup = False
timestep = 32
status_set_encoders = False
state_interseccion = False
start = 0
tiempo_ejecucion = 0
tiempo = 0
pow1 = 0
pow2 = 0

counter_interseccion = 0
counter_interseccion_derecha = 0
counter_interseccion_izquierda = 0
tiempo_mov = 0
tiempo_ejecucion_mov = 0
pow1_mov = 0
pow2_mov = 0
start_mov = 0
state_obstacle = False
tail_mov = []

def add_to_tail_mov(tiempo, pow1, pow2):
    tail_mov.append([tiempo, pow1, pow2])

def check_tail_mov():
    if len(tail_mov) != 0:
        set_Mov(tail_mov[0][0], tail_mov[0][1], tail_mov[0][2])
        tail_mov.pop(0)
        return True
    return False

def doblar_derecha(fraccion):
    tiempo_vuelta = 3.25
    #hacemos que el robot se de una fraccion de vuelta hacia la derecha, la fraccion depende del valor de input de la funcion
    fraccion_vuelta = 1/fraccion
    potencia1 = 4
    potencia2 = -4
    tiempo = tiempo_vuelta*fraccion_vuelta
    return tiempo, potencia1, potencia2

def doblar_izquierda(fraccion):
    tiempo_vuelta = 3.25
    #hacemos que el robot se de una fraccion de vuelta hacia la izquierda, la fraccion depende del valor de input de la funcion
    fraccion_vuelta = 1/fraccion
    potencia1 = -4
    potencia2 = 4
    tiempo = tiempo_vuelta*fraccion_vuelta
    return tiempo, potencia1, potencia2

def set_Mov(timepo, pow1, pow2):
    global tiempo_mov
    global tiempo_ejecucion_mov
    global pow1_mov
    global pow2_mov
    global start_mov
    global leftMotor
    global rightMotor
    pow1_mov = pow1
    pow2_mov = pow2
    tiempo_mov = timepo
    start_mov = time()
    return True

def state_mov():
    global tiempo_mov
    global tiempo_ejecucion_mov
    
    #print("state mov tiempo_mov: ", tiempo_mov, tiempo_ejecucion_mov)
    if tiempo_mov == 0:
        return False
    global pow1_mov
    global pow2_mov
    global start_mov
    global leftMotor
    global rightMotor

    if tiempo_ejecucion_mov < tiempo_mov:
        print("tiempo_mov: ", tiempo_mov, "tiempo_ejecucion_mov: ", tiempo_ejecucion_mov)
        leftMotor.setVelocity(pow1_mov)
        rightMotor.setVelocity(pow2_mov)
        tiempo_ejecucion_mov = time() - start_mov
        return True
    else:
        tiempo_ejecucion_mov = 0
        tiempo_mov = 0
        pow1_mov = 0
        pow2_mov = 0
        start_mov = 0
        return False