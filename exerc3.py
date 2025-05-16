# Calculo do seno cosseno e tangente

import math

angulo = float(input("Digite o ângulo em graus: "))

# Converter o ângulo para radianos
angulo_radianos = math.radians(angulo)

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

# Exibir os resultados
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
