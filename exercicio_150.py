import math
angulo = float(input("Digite o ângulo em graus: "))

angulo_radianos = math.radians(angulo)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)

quadrante = int(angulo // 90) + 1  

if quadrante % 2 == 0:
    print(f"Seno do ângulo {angulo} graus: {seno:.2f}")
else:
    print(f"Cosseno do ângulo {angulo} graus: {cosseno:.2f}")
