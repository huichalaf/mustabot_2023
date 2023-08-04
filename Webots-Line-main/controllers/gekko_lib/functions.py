from time import sleep, time
from motor import MOTOR

interseccion_counter_big = 0

def normalize_values(values):
    #ahora creamos una lista con los valores ajustados para que el pid funcione de mejor forma cuando se enfrente a colores como el verde
    exponente = 3
    values_normalized = []
    for value in values:
        value /= 1000
        for i in range(1, exponente):
            value *= value
        values_normalized.append(value*1000)
    return values_normalized

def PID_LINE(kp, kd, ki, previous_error, sensor_values, PBASE, sum_error, motor1, motor2):
    #we calculate the error
    global interseccion_counter_big

    black_umbral = 900
    interseccion, semiinterseccion_derecha, semiinterseccion_izquierda = 0, 0, 0
    for i in range(0, len(sensor_values)):
        if sensor_values[i] > black_umbral:
            interseccion += 1
        if i < 4 and sensor_values[i] > black_umbral:
            semiinterseccion_derecha += 1
        if i > 3 and sensor_values[i] > black_umbral:
            semiinterseccion_izquierda += 1
    
    sensor_values = normalize_values(sensor_values)
    if interseccion == len(sensor_values):
        print("interseccion")
        interseccion_counter_big += 1
        return "interseccion"
    elif semiinterseccion_izquierda == 4:
        print("semiinterseccion izquierda")
        #semiinterseccion_counter_big += 1
        return "semiinterseccion izquierda"
    elif semiinterseccion_derecha == 4:
        print("semiinterseccion derecha")
        #semiinterseccion_counter_big2 += 1
        return "semiinterseccion derecha"
    
    if interseccion_counter_big > 2:
        interseccion_counter_big = 0
        return "interseccion"
    
    error = sensor_values[0]*-4 + sensor_values[1]*-3 + sensor_values[2]*-2 + sensor_values[3]*-1 + sensor_values[4]*1 + sensor_values[5]*2 + sensor_values[6]*3 + sensor_values[7]*4
    #we calculate the speed
    speed = error * kp + (error - previous_error) * kd + sum_error * ki
    #we limit the speed
    if speed > 10:
        speed = 10
    elif speed < -10:
        speed = -10
    #we update the previous error and sum error
    previous_error = error
    #we return the speed
    return PBASE+speed, PBASE-speed, previous_error, sum_error+error

def is_green(value):
    green_interval = [400, 600]
    if value > green_interval[0] and value < green_interval[1]:
        return True
    return False

