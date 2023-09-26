saldo_medio = float(input("Digite o saldo médio do cliente:"))
if saldo_medio <= 500:
  valor_credito = o 
elif saldo_medio <= 1000:
  valor_credito = saldo_medio * 0.30
elif saldo_medio <= 3000:
  valor_credito = saldo_medio * 0.40
else: 
  valor_credito = saldo_medio *0.50

print(f"Saldo Médio: R${saldo_medio:.2f}")
print(f"Valor do Crédito: R${valor_credito:.2f}")
