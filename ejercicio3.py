frase = input("escriba una frase: ")
for i, c in enumerate(frase):
    print('caracter: %s - indice: %i' % (c, i))
   
indice= int(input("elija el indice de la letra a modificar"))
print(frase[indice])
letra = input("letra nueva")
print(letra)
print(frase.replace((frase[indice]), (letra)))