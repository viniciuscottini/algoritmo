nome = input("Digite o nome do paciente: ")
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)

faixa_de_risco = ""
if imc < 20:
    faixa_de_risco = "abaixo do peso"
elif 20 <= imc < 25:
    faixa_de_risco = "normal"
elif 25 <= imc < 30:
    faixa_de_risco = "excesso de peso"
elif 30 <= imc < 35:
    faixa_de_risco = "obesidade"
else:
    faixa_de_risco = "obesidade mórbida"


print(f"Nome do paciente: {nome}")
print(f"IMC: {imc:.2f}")
print(f"Faixa de Risco: {faixa_de_risco}")
