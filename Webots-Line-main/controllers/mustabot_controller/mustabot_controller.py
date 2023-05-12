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

tiempo_mov = 0
tiempo_ejecucion_mov = 0
pow1_mov = 0
pow2_mov = 0
start_mov = 0

tail_mov = []

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
    
    print("state mov tiempo_mov: ", tiempo_mov, tiempo_ejecucion_mov)
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

def doblar_derecha(fraccion):
    tiempo_vuelta = 3
    #hacemos que el robot se de una fraccion de vuelta hacia la derecha, la fraccion depende del valor de input de la funcion
    fraccion_vuelta = 1/fraccion
    potencia1 = 4
    potencia2 = -4
    tiempo = tiempo_vuelta*fraccion_vuelta
    return tiempo, potencia1, potencia2

def doblar_izquierda(fraccion):
    tiempo_vuelta = 3
    #hacemos que el robot se de una fraccion de vuelta hacia la izquierda, la fraccion depende del valor de input de la funcion
    fraccion_vuelta = 1/fraccion
    potencia1 = -4
    potencia2 = 4
    tiempo = tiempo_vuelta*fraccion_vuelta
    return tiempo, potencia1, potencia2


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

def loop():
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
    print(ir_sensors_values)
    try:
        potencia1, potencia2, error_line, sum_error_line = PID_LINE(0.001, 0, 0, error_line, ir_sensors_values, 2.14, sum_error_line, leftMotor, rightMotor)
    except:

        interseccion_tipo = PID_LINE(0.001, 0, 0, error_line, ir_sensors_values, 2.14, sum_error_line, leftMotor, rightMotor)

        if interseccion_tipo == "interseccion":
            print("interseccion fuera funcion")
            set_Mov(0.5, 0, 0)
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

        if interseccion_tipo == "semiinterseccion izquierda" and state_interseccion == False:
            set_Mov(0.1, 3.14, 3.14)
            print("semiinterseccion izquierda fuera funcion")
            tiempo, pow1, pow2 = doblar_izquierda(4)
            state_interseccion = True
            add_to_tail_mov(tiempo, pow1, pow2)
        
        if interseccion_tipo == "semiinterseccion derecha" and state_interseccion == False:
            set_Mov(0.1, 3.14, 3.14)
            print("semiinterseccion  fuera funcion")
            tiempo, pow1, pow2 = doblar_derecha(4)
            state_interseccion = True
            add_to_tail_mov(tiempo, pow1, pow2)

    leftMotor.setVelocity(potencia2)
    rightMotor.setVelocity(potencia1)

if __name__ == "__main__":
    while robot.step(timestep) != -1:
        try:
            loop()
        except Exception as e:
            if not status_setup:
                setup()
                status_setup = True
            else:
                print(e)