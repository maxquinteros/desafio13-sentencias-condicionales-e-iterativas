peso = float(input("Ingrese el peso en Kg: "))
altura = float(input("Ingrese el peso en centímetros: "))

imc = peso/((altura/100)**2)
print(f"Su IMC es {round(imc,2)}")

if imc < 18.5:
    print("La clasificación OMS es Bajo Peso")
elif 18.5 < imc and imc < 25:
    print("La clasificación es adecuado")
elif 25 < imc and imc < 30:
    print("La clasificación es Sobrepeso")
elif 30 < imc and imc < 35:
    print("La clasificación es Obesidad Grado I")
elif 35 < imc and imc < 40:
    print("La clasificación es Obesidad Grado II")
else:
    print("La clasificación es Obesidad Grado III")