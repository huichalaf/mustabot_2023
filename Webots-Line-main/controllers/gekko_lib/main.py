from mustabot_controller import *

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
    global counter_interseccion
    global counter_interseccion_derecha
    global counter_interseccion_izquierda
    global state_obstacle
    #leemos el sensor laser frontal
    laser_frontal_value = laser_frontal.getValue()
    #print("laser frontal: ", laser_frontal_value)
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
    #print(ir_sensors_values)
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
            #print("semiinterseccion izquierda fuera funcion")
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
            #print("semiinterseccion  fuera funcion")
            if interseccion_tipo == "semiinterseccion izquierda" or counter_interseccion_izquierda != 0:
                interseccion_tipo = "interseccion"
                counter_interseccion = 3
                counter_interseccion_izquierda = 0
                counter_interseccion_derecha = 0
            tiempo, pow1, pow2 = doblar_derecha(4)
            state_interseccion = True
            add_to_tail_mov(tiempo, pow1, pow2)
            counter_interseccion_derecha = 0

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
                print("error: ",e)