destino = input("Digite o destino (Região Norte, Região Nordeste, Região Centro-Oeste, ou Região Sul): ")
ida_e_volta = input("A viagem inclui ida e volta? (S para Sim, N para Não): ")

preco_ida = 0
preco_ida_e_volta = 0 
if destino == "Região Norte":
    preco_ida = 500.00
    preco_ida_e_volta = 900.00

elif destino == "Região Nordeste":
    preco_ida = 350.00
    preco_ida_e_volta = 650.00

elif destino == "Região Centro-Oeste":
    preco_ida = 350.00
    preco_ida_e_volta = 600.00

elif destino == "Região Sul":
    preco_ida = 300.00
    preco_ida_e_volta = 550.00
else:
    print("Destino não reconhecido.")


if ida_e_volta == "S":
    preco_total = preco_ida_e_volta
    tipo_viagem = "ida e volta"
elif ida_e_volta == "N":
    preco_total = preco_ida
    tipo_viagem = "ida"
else:
    print("Opção de ida e volta inválida.")


if preco_total > 0:
    print(f"Destino: {destino}")
    print(f"Tipo de Viagem: {tipo_viagem}")
    print(f"Preço da Passagem: R${preco_total:.2f}")
