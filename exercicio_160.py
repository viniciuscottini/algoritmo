x = float(input("Digite o valor de x: "))


if x <= 1:
    y = 1
elif 1 < x <= 2.5:
    y = 2 * x
elif 2.5 < x <= 3:
    y = x
else:
    y = x ** 3

print(f"y = {y}")
