import time
import os

def load_file():
    with open("./Session_8_Game_life/genesis.txt", 'r', encoding='utf-8') as file:
        return file.readlines()

def set_environment(raw_file):
    env = []
    for line in raw_file:
        line = line.strip()
        if not line:
            continue
        env.append([int(c) for c in line])
    return env

def print_environment(env):
  for row in env:
    for cell in row:
      if cell == 1:
        print('■', end="")
      else:
        print(' ', end="")
    print()
  None

def count_neighbors(env, x, y):
    count = 0
    rows = len(env)
    cols = len(env[0])
    for i in [x - 1, x, x + 1]:
        for j in [y - 1, y, y + 1]:
            if i == x and j == y:
                continue
            if env[i][j] == 1:
                count += 1
    return count

# Inicialización
genesis = load_file()
env = set_environment(genesis)

# Simulación
for generation in range(50):
    os.system("cls")
    print(f"Generación {generation + 1}:")
    print_environment(env)
    time.sleep(0.5)

    new_env = [row[:] for row in env]  # Copia profunda

    for i in range(1,len(env)-1):
        for j in range(1,len(env[0])-1):
            neighbors = count_neighbors(env, i, j)
            if env[i][j] == 1:
                new_env[i][j] = 0 if neighbors < 2 or neighbors > 3 else 1
            else:
                new_env[i][j] = 1 if neighbors == 3 else 0

    env = new_env