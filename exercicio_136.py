nome = input("Digite seu nome:")

idade = int(input("Digite sua idade:"))

if idade <= 10:       
  valor = 30.00
elif idade <= 29:
  valor = 60.00
elif idade <= 45:
  valor = 120.00
elif idade <= 59:
  valor = 150.00
elif idade <= 65:
  valor = 250.00
else:
  valor = 400.00

print(f"{nome} deverá pagar R${valor:.2f}")
