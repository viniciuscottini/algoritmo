import math

x = float(input("Digite um número para ser o x (X > 4): "))
numerador = 5 * x + 3 
denominador = math.sqrt(x ** 2 - 16)

if x <=4:
    print("Esse número não trará um resultado")

else:
    funcao = numerador / denominador

print ("Dado o x dessa função, o resultado será", funcao)

