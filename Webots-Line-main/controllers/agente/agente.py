"""agente controller."""
import tensorflow as tf
from controller import Robot

# Crear robot y sensores/actuadores
robot = Robot()
motor = robot.getDevice('right_motor')
motor2 = robot.getDevice('left_motor')

# Definir modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')
])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# Definir funciones de recompensa y acciones
def reward_function(distance_sensor_values, action):
    def reward_function(distance_sensor_values):
    # Obtener la distancia promedio de los valores de los sensores
    distance = sum(distance_sensor_values) / len(distance_sensor_values)

    # Definir la recompensa como la inversa de la distancia promedio
    # Esto significa que cuanto menor sea la distancia, mayor será la recompensa
    reward = 1 / distance

    # Si la distancia es menor que un valor umbral, terminar la simulación y asignar una recompensa negativa
    if distance < 0.1:
        reward = -10
        done = True
    else:
        done = False

    return reward, done

    return reward

def get_action(state):
    # Obtener acción del modelo basada en el estado actual
    return action

# Loop principal
while robot.step(64) != -1:
    # Obtener estado actual
    state = [motor.getPosition()]

    # Obtener acción del modelo
    action = get_action(state)

    # Ejecutar acción en el robot
    motor.setPosition(action)

    # Obtener recompensa y estado siguiente
    reward = reward_function(state, action)
    next_state = [motor.getPosition()]

    # Actualizar modelo
    target = reward + 0.99 * model.predict(next_state[np.newaxis])[0]
    model.fit(state, [target], verbose=0)

# Cerrar el robot
robot.cleanup()

