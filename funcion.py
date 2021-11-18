# Crear una funcion que permita ingresar al usuario
# Numeros enteros... y strings...
# 1- print -> imprima la lista que se fue cargando hasta el momento...
# 2- append a-> siendo a numero entero
# 3- renove b-> siendo b nuemro entero
# 4- sart
# 5- reverse
# 6- inser c d -> siendo ambos numeros enteros c lo indico y d el valor
# 7- exit -> termina el programa

isRunning = true
myList = []

while isRunning:
    userInput = input("ingrese Comando: ")
    command = userimput.split()

    if command[0]== "exit":
        isRunning = False
    elif command[0] == "append":
        # Quizas debamos hacer un chequeo del input 
        argumentos = command [1]
        if argumentos.isdigit():
            myList.append(int(argumentos))
    elif command[0] == "print":
        print(myList) 
    elif command[0] == "sort":
        myList.sort()
    elif command[0] == "insert":
        myList.insert(int(command[1]), int(command[2]))
        #print("Se agrego",command[2],"en el indica",command[1])       
