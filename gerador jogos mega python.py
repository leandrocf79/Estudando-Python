import random

# Gerador de números aleatórios para MEGA SENA
num = random.sample(range(1, 61), 6)

# Números em ordem crescente
num = sorted(num)

print(num)