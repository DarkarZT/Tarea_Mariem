import random
from random import randint, uniform


def imprimirmatriz():
    i= 0
    m= int(input("Digite una dimension Filas"))
    n= int(input("Digite una dimension Columnas"))
    while m < 0 : 
        m= int(input("Digite una dimension Filas"))    
    while n < 0 :
        n= int(input("Digite una dimension Columnas"))
    for i in range(0,m):
        for j in range(0,n):
            numerosA= random.randint(100,300)
            print(numerosA," ", end='')
        print(" ")


def imprimirbordes():   
    m= int(input("Digite una dimension Filas"))
    n= int(input("Digite una dimension Columnas"))
    while m < 0 : 
        m= int(input("Digite una dimension Filas"))    
    while n < 0 :
        n= int(input("Digite una dimension Columnas"))
    for i in range(0,n):
        numerosA= random.randint(100,300)
        print (numerosA," ", end='')
    print()
    for i in range(0,m-2):
        numerosA= random.randint(100,300)
        print(numerosA," ", end='')
        for j in range(0,n-2):
            print("     ", end='')
        print(numerosA," ")
    for i in range(0,n):
        numerosA= random.randint(100,300)
        print(numerosA," ", end='')
    
def imprimirdiagonal():
    
    i=0
    j=0

    m=int(input("ingrese un lado"))
    n=int(input("ingrese un lado"))
    while m % 2 == 0 :
        m=int(input("ingrese un lado"))
    while n % 2 == 0 :
        n=int(input("ingrese un lado"))
    for i in range(0,m):
        for j in range(0,n):
            if i==j or i+j==n-1:
                numerosA= random.randint(100,300)
                print(numerosA," ", end="")
            else:
                print("     ", end="")
        
        print(" ")

def cifradobasico():
    table = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X'],
        ['Y', 'Z', 'A', 'B'],
        ['B', 'C', 'D', 'E']
    ]


    key = 3
    word = 'HOLA'

    result = ''
    for char in word:
        print(char)
        for i in range(len(table)):
            found = False
            for j in range(len(table[i])):
                if char == table[i][j]:
                    found = True
                    result += str(((i*4) + j) + key) # AQUI, CIEGO
                    break
            
            if found: break
            
    print(result)


def imprimircruz():   
    filas=int(input("ingrese un lado"))
    columnas=int(input("ingrese un lado"))

    while filas % 2 == 0:
        filas=int(input("ingrese un lado"))
        
    while columnas < 0:
        columnas=int(input("ingrese columnas"))

    for i in range(filas):
        for j in range(columnas):
            if i == 2 :
                numerosA= str(random.randint(100,300))
                
                print(f"{numerosA} ", end='')
            elif j == columnas-1:
                numerosA= str(random.randint(100,300))
                print(" "*columnas," "*(columnas-4),numerosA, end='')

        print("", end='')
            

        print(" ")


    print()




def precipitacion():
    mayor = 0
    k= 0 
    ciudades = int(input("Cuantas Ciudades? "))
    matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]

    for f in matriz:
        print(f)

    for i in range(len(matriz[0])):
        mayor=0
        
        for j in range(len(matriz)):
            
            if matriz[j][i] >= mayor:
                mayor = matriz[j][i]
                k= j+1
         
    
        print("En la ciudad",i+1 ,  "con una precipitacion de:",mayor, " y el dia es",k )


def promedio_ciudades():
    ciudades = int(input("Cuantas Ciudades? "))
    matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]
    
    for f in matriz:
        print(f)

    for i in range(len(matriz[0])):
        
        suma = 0
        for j in range(len(matriz)):
            suma = suma + matriz[j][i]
            
        promedio = suma/(j+1)
        
        print("El promedio de la ciudad:",i+1, "es igual a:", promedio)    

def promediogeneral():
    ciudades = int(input("Cuantas Ciudades? "))
    matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]
    for f in matriz:
        print(f)
    k =ciudades*30
    suma = 0
    for i in range(len(matriz[0])):
        
        for j in range(len(matriz)):
            suma = suma + matriz[j][i]

    print(suma)  
    promedio = suma/(k)
    print(promedio)
    p = 0
    for i in range(len(matriz[0])):
        mayor = 0
        for j in range(len(matriz)):
            suma = suma + matriz[j][i]
            if matriz[j][i] >= promedio:
                mayor = matriz[j][i]
                p = j+1     
                print("En la ciudad",i+1 ,  "con una precipitacion de:",mayor, " y el dia es",p )

def menor():
    ciudades = int(input("Cuantas Ciudades? "))
    matriz = [[uniform(1,6).__round__(1)  for j in range(ciudades)]  for i in range(30)]
    for f in matriz:
        print(f)

    k= 0
    for i in range(len(matriz[0]))  :
        menor=6
        for j in range(len(matriz[i])) :

            if matriz[i][j] <= menor:
                menor = matriz[i][j]
                k = j+1
        print("la ciudad", k , "en el dia", i+1, "con menor precipitacion fue:", menor )


def letra_V():
    
    letra = input("Digite una letra con la que llene la letra a dibujar ")
    for i in range(17):
        
        for j in range(14):
            
            if i == j-(14//2) :
                print(letra, end='')
        
            print("  ", end='')
        for j in range(14):
            
        
            if 1-i == j-(14//2)+2:
                print(letra, end='')
            else:
                print(" ", end='')
            print(" ", end='')
        print(" ")

def letra_M():
    letra = input("Digite una letra con la que llene la letra a dibujar ")
    for i in range(7):
        for j in range(12):
            if (i == 0 or i == 1 or 4 <= i <= 6) and (j == 1 or j == 11):
                print(letra, end='')
            elif i == 2 and (j == 1 or j == 3 or j == 9 or j == 11):
                print(letra, end='')
            elif i == 3 and (j == 1 or j == 6 or j == 11):
                print(letra, end='')
            else:
                print(' ', end='')
        print()
#