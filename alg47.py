num = int(input("\nEntre com um numero de 3 digitos: "));
c = int(num/100);
d = int(num % 100 / 10);
u = int(num % 10);
num1 = u* 100 + d * 10 + c;
print("\nNumero: ", num)
print("\nNumero invertido: ", num1)
print("\n")