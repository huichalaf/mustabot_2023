import tensorflow as tf
import gym
import numpy as np

# Crear entorno
env = gym.make('CartPole-v0')

# Definir modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=env.observation_space.shape),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(env.action_space.n, activation='linear')
])

# Compilar modelo
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# Entrenar modelo
for episode in range(100):
    state = env.reset()
    done = False
    while not done:
        # Obtener acción del modelo
        action = np.argmax(model.predict(state[np.newaxis]), axis=1)[0]
        # Ejecutar acción en entorno
        next_state, reward, done, info = env.step(action)
        # Calcular objetivo de aprendizaje
        target = reward + 0.99 * np.max(model.predict(next_state[np.newaxis]), axis=1)[0]
        # Actualizar modelo
        model.fit(state[np.newaxis], [target], verbose=0)
        # Actualizar estado actual
        state = next_state

# Probar modelo entrenado
state = env.reset()
done = False
while not done:
    action = np.argmax(model.predict(state[np.newaxis]), axis=1)[0]
    next_state, reward, done, info = env.step(action)
    state = next_state
    env.render()

env.close()

