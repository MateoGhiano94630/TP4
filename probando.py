import simpy
import random

# Función para simular la llegada de grupos de deportistas
def llegada_grupos(env, num_grupos, tiempo_llegada, disciplina, tiempo_ocupacion):
    for i in range(num_grupos):
        yield env.timeout(random.uniform(*tiempo_llegada))
        print(f"Grupo de {disciplina} llega al polideportivo en el tiempo {env.now}")
        env.process(ocupar_cancha(env, f"Grupo {i+1} de {disciplina}", tiempo_ocupacion))

# Función para simular la ocupación de la cancha por un grupo
def ocupar_cancha(env, nombre_grupo, tiempo_ocupacion):
    with cancha.request() as req:
        print(f"{nombre_grupo} solicita ocupar la cancha en el tiempo {env.now}")
        yield req  # Esperar a que la cancha esté disponible
        print(f"{nombre_grupo} comienza a ocupar la cancha en el tiempo {env.now}")
        yield env.timeout(random.uniform(*tiempo_ocupacion))
        print(f"{nombre_grupo} termina de ocupar la cancha en el tiempo {env.now}")

        # Simular limpieza de la cancha después del partido
        print(f"Cancha siendo limpiada en el tiempo {env.now}")
        yield env.timeout(10)
        print(f"Cancha limpia en el tiempo {env.now}")

# Configuración de la simulación
tiempo_simulacion = 24 * 60  # Tiempo total de simulación (24 horas en minutos)
tiempo_llegada_futbol = (10 * 60, 10 * 60 + 60)      # Tiempo promedio entre llegadas de grupos de fútbol (en minutos)
tiempo_llegada_handball = (10 * 60, 14 * 60)    # Tiempo promedio entre llegadas de grupos de handball (en minutos)
tiempo_llegada_basketball = (6 * 60, 10 * 60)   # Tiempo promedio entre llegadas de grupos de basketball (en minutos)

# Inicialización del entorno de simulación
env = simpy.Environment()
cancha = simpy.Resource(env, capacity=1)  # Recurso que representa la cancha

# Iniciar procesos de llegada de grupos de deportistas
env.process(llegada_grupos(env, num_grupos=10, tiempo_llegada=tiempo_llegada_futbol, disciplina="Fútbol", tiempo_ocupacion=(80, 100)))
env.process(llegada_grupos(env, num_grupos=10, tiempo_llegada=tiempo_llegada_handball, disciplina="Handball", tiempo_ocupacion=(60, 100)))
env.process(llegada_grupos(env, num_grupos=10, tiempo_llegada=tiempo_llegada_basketball, disciplina="Basketball", tiempo_ocupacion=(70, 130)))

# Ejecutar la simulación
env.run(until=tiempo_simulacion)