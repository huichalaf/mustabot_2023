import random
import numpy as np
def create_q_table(num_states, num_actions):
    """
    Crea una tabla Q de num_states x num_actions y la inicializa con valores aleatorios.
    """
    q_table = np.zeros((num_states, num_actions))
    return q_table

def choose_action(state, q_table, eps):
    """
    Elige una acción en el estado actual, ya sea explotando los valores Q conocidos o explorando una acción aleatoria.
    """
    if random.uniform(0, 1) < eps:
        action = random.randint(0, 9)  # elegir una acción aleatoria
    else:
        action = np.argmax(q_table[state, :])  # elegir la acción con el valor Q máximo para este estado
    return action

def update_q_table(state, action, reward, next_state, q_table, lr, discount_factor):
    """
    Actualiza la tabla Q con el valor de aprendizaje lr y el factor de descuento discount_factor.
    """
    q_predict = q_table[state, action]
    q_target = reward + discount_factor * np.max(q_table[next_state, :])
    q_table[state, action] += lr * (q_target - q_predict)
    return q_table
def sum_game():
    # generar dos números aleatorios
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    # mostrar los números y pedir una respuesta al usuario
    print("¿Cuál es la suma de", a, "y", b, "?")
    answer = int(input())
    # calcular la respuesta correcta y recompensar o penalizar al modelo
    if answer == a + b:
        print("¡Respuesta correcta!")
        reward = 1
    else:
        print("Respuesta incorrecta.")
        reward = -1
    return reward

q_table = create_q_table(110, 10)  # 110 estados posibles (0-10 para a, 0-10 para b)
lr = 0.1
eps = 0.1
discount_factor = 0.9

for i in range(10000):
    state = random.randint(0, 109)  # elegir un estado aleatorio
    action = choose_action(state, q_table, eps)
    reward = sum_game()
    next_state = state + 11  # siguiente estado es simplemente agregar 1 al valor del estado actual
    q_table = update_q_table(state, action, reward, next_state, q_table, lr, discount_factor)

