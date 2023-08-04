"""mustabot_controller controller."""

from controller import Robot
from motor import MOTOR, ENCODER, doblar_derecha, doblar_izquierda
from sensors import IR, LASER, COLOR
from functions import PID_LINE
from time import time, sleep

robot = Robot()
leftMotor = None
rightMotor = None
encoder_left = None
encoder_right = None
status_setup = False

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

#----------------------------funciones necesarias para el funcionamiento del robot-----------------------------#
def add_to_tail_mov(tiempo, pow1, pow2):
    tail_mov.append([tiempo, pow1, pow2])

def check_tail_mov():
    if len(tail_mov) != 0:
        set_Mov(tail_mov[0][0], tail_mov[0][1], tail_mov[0][2])
        tail_mov.pop(0)
        return True
    return False

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

#----------------------------------------definimos el void setup-------------------------------------------#
def setup():
    global robot
    global leftMotor
    global rightMotor
    global encoder_left
    global encoder_right
    global ir_sensors
    global laser_frontal
    global laser_izquierdo
    global laser_derecho
    global color_derecho
    global color_izquierdo

    leftMotor = MOTOR(robot, "left_motor")
    rightMotor = MOTOR(robot, "right_motor")
    encoder_left = ENCODER(robot, "left_encoder")
    encoder_right = ENCODER(robot, "right_encoder")

    for i in range(1,9):
        ir_sensors.append(IR(robot, f"ir_{i}"))

    laser_frontal = LASER(robot, "laser_frontal")
    laser_izquierdo = LASER(robot, "laser_izquierdo")
    laser_derecho = LASER(robot, "laser_derecho")
    color_derecho = COLOR(robot, "color1")
    color_izquierdo = COLOR(robot, "color2")
#----------------------------------------definimos el void loop-------------------------------------------#
def loop():
    #variables globales
    global robot
    global leftMotor
    global rightMotor
    global encoder_left
    global encoder_right
    global ir_sensors
    global status_set_encoders
    global potencia1
    global potencia2
    global error_line
    global sum_error_line
    global laser_frontal
    global laser_izquierdo
    global laser_derecho
    global color_derecho
    global color_izquierdo
    global state_interseccion
    global start
    global tiempo_ejecucion
    global tiempo
    global pow1
    global pow2
    global counter_interseccion
    global counter_interseccion_derecha
    global counter_interseccion_izquierda
    global state_obstacle
    #leemos el sensor laser frontal
    laser_frontal_value = laser_frontal.getValue()
    #nos preguntamos si existe un obstaculo en frente
    if laser_frontal_value < 100:
        print("Obstaculo detectado")
        if state_obstacle == False:
            set_Mov(0.5, 0, 0)
            add_to_tail_mov(0.7, -2, -2)
            add_to_tail_mov(1.6, 2, -2)
            add_to_tail_mov(2.5, 2, 2)
            add_to_tail_mov(1.6, -2, 2)
            add_to_tail_mov(5, 2, 2)
            add_to_tail_mov(1.6, -2, 2)
            add_to_tail_mov(2.4, 2, 2)
            add_to_tail_mov(2.4, 2, -2)
            state_obstacle = True
            
    if not status_set_encoders:
        encoder_left.set_start_position()
        encoder_right.set_start_position()
        status_set_encoders = True

    if state_mov() == True:
        return False

    if check_tail_mov() == True:
        return False
    
    state_interseccion = False
    ir_sensors_values = [x.getValue() for x in ir_sensors]

    try:
        potencia1, potencia2, error_line, sum_error_line = PID_LINE(0.001, 0, 0, error_line, ir_sensors_values, 2.14, sum_error_line, leftMotor, rightMotor)
    except:
        interseccion_tipo = PID_LINE(0.001, 0, 0, error_line, ir_sensors_values, 2.14, sum_error_line, leftMotor, rightMotor)
        if interseccion_tipo == "interseccion" and counter_interseccion < 5:
            counter_interseccion += 1
            print("interseccion dentro funcion")
        if interseccion_tipo == "semiinterseccion izquierda" and counter_interseccion_izquierda < 5:
            counter_interseccion_izquierda += 1
            print("semiinterseccion izquierda dentro funcion")
        if interseccion_tipo == "semiinterseccion derecha" and counter_interseccion_derecha < 5:
            counter_interseccion_derecha += 1
            print("semiinterseccion derecha dentro funcion")

        if interseccion_tipo == "interseccion" and counter_interseccion >= 3:
            print("interseccion fuera funcion")
            set_Mov(0.5, 0, 0)
            set_Mov(0.1, 3.14, 3.14)
            #ahora revisamos los valores de los sensores de color
            color_derecho_value = color_derecho.get_color()
            color_izquierdo_value = color_izquierdo.get_color()
            #ahora revisamos si alguno de los sensores de color detecto verde
            if color_derecho_value == "green" and color_izquierdo_value != "green":
                tiempo, pow1, pow2 = doblar_derecha(4)
                add_to_tail_mov(tiempo, pow1, pow2)
            elif color_derecho_value != "green" and color_izquierdo_value == "green":
                tiempo, pow1, pow2 = doblar_izquierda(4)
                add_to_tail_mov(tiempo, pow1, pow2)
            elif color_derecho_value == "green" and color_izquierdo_value == "green":
                tiempo, pow1, pow2 = doblar_derecha(2)
                add_to_tail_mov(tiempo, pow1, pow2)
            else:
                add_to_tail_mov(0.5, 3.14, 3.14)
            counter_interseccion = 0

        if interseccion_tipo == "semiinterseccion izquierda" and state_interseccion == False and counter_interseccion_izquierda >= 3:
            set_Mov(0.1, 3.14, 3.14)
            if interseccion_tipo == "semiinterseccion derecha" or counter_interseccion_derecha != 0:
                interseccion_tipo = "interseccion"
                counter_interseccion = 3
                counter_interseccion_derecha = 0
                counter_interseccion_izquierda = 0
            tiempo, pow1, pow2 = doblar_izquierda(4)
            state_interseccion = True
            add_to_tail_mov(tiempo, pow1, pow2)
            counter_interseccion_izquierda = 0
        
        if interseccion_tipo == "semiinterseccion derecha" and state_interseccion == False and counter_interseccion_derecha >= 3:
            set_Mov(0.1, 3.14, 3.14)
            if interseccion_tipo == "semiinterseccion izquierda" or counter_interseccion_izquierda != 0:
                interseccion_tipo = "interseccion"
                counter_interseccion = 3
                counter_interseccion_izquierda = 0
                counter_interseccion_derecha = 0
            tiempo, pow1, pow2 = doblar_derecha(4)
            state_interseccion = True
            add_to_tail_mov(tiempo, pow1, pow2)
            counter_interseccion_derecha = 0

    #cambiamos la potencia de los motores del robot a la que teníamos anteriormente
    leftMotor.setVelocity(potencia2)
    rightMotor.setVelocity(potencia1)

#--------------inicializamos todo y entramos al loop principal-----------------#
if __name__ == "__main__":
    while robot.step(timestep) != -1:
        try:
            loop()
        except Exception as e:
            if not status_setup:
                setup()
                status_setup = True
            else:
                print("error: ",e)