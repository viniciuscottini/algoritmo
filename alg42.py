import math
angulo = float(input("\nDigite um angulo em graus: "));
rang = angulo * math.pi / 180;
print("\nSeno: ", math.sin(rang));
print("\nCo-Seno: ", math.cos(rang));
print("\nTangente: ", math.tan(rang));
print("\nCo-Secante: ", 1/ math.sin(rang));
print("\nSecante: ", 1/ math.cos(rang));
print("\nCo-Tangente: ", 1/ math.tan(rang));
print("\n")