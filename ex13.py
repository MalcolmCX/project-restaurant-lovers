n1 = int(input('Informe um número: '))

print(f"\nA tabuada do número {n1} é:")
for numero in range(1, 11):
    resultado = numero * n1
    print(f"{n1} x {numero} = {resultado}")
