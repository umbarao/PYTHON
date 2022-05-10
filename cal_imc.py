## CALCULADORA DE IMC ###
altura = 0
peso = 0
IMC = 0

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

IMC = peso/(altura*altura)

print("Seu IMC é: %.2f"% IMC)

if (IMC < 18.5):
    print("MAGREZA")
elif (IMC > 18.5 and IMC < 24.9 ):
    print("NORMAL")
elif (IMC > 25.0 and IMC < 29.9):
    print("SOBREPRESO")
elif (IMC > 30.0 and IMC < 39.9):
    print("OBESIDADE")
else:
    print("OBESIDADE GRAVE")



