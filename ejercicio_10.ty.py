i=1

n = int(input("Digite el valor para num"))
suma_notas=0
while i<=n:
    nota = float(input("Digite su nota"))
    suma_notas += nota
    i+=1
print("El promedio es : ", suma_notas/n)
