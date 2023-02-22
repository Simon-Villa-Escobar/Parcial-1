import random

nombre = ['Edison', 'Ana', 'Pedro', 'Carlos']
apellido = ['Valencia', 'Cano', 'Restrepo', 'Rendon']
letra_silla = ['A', 'B', 'C', 'H', 'J', 'K']


#Generador de nombres aleatorios
def generarNombre():
  pasajero = f'{random.choice(nombre)} {random.choice(apellido)} {random.choice(apellido)}'
  return pasajero


#Generador de nombres
def generarNombre1():
    Nom = (input("Ingrese su nombre: \n"))
    Ap1 = (input("Ingrese su primer apellido: \n"))
    Ap2 = (input("Ingrese su segundo apellido: \n"))
    Ed = (input("Ingrese su edad: "))
    pasajero = f'{Nom} {Ap1} {Ap2} ,  {Ed}  años'
    return pasajero


#Generador de sillas aleatorias
def generarSilla():
  fila = random.randint(5, 27)
  silla = random.choice(letra_silla)
  return (fila, silla)

#Generador de sillas
def generarSilla1():
    sil = (input("Ingrese el asiento que deseas: \n"))
    fi = int(input("Ingrese la fila que deseas:  \n"))
    fila = fi
    silla = sil
    return (fila, silla)




#Silla en el avion
def ubicarSilla(fila, silla):
  dicSilla = {"A":0, "B":1, "C":2, "H":3, "J":4, "K":5}
  y = dicSilla[silla]
  x = fila - 5
  return (x,y)




#Estados de las sillas en el avion
avion = []
def disponerAvion(filas, sillas):
  # 0=libre, 1=reservado, 2=comprada
  for fila in range(filas):
    listaSilla = []
    for silla in range(sillas):
      listaSilla.append(0)
    avion.append(listaSilla)

    
nombres = []
  
if __name__ == "__main__":
    disponerAvion(23,6)
    puestos = 0
while True:
    print("1 para reservar el asiento, 2 para comprarlo, 3 para cancelar una reserva, 4 para verla información de los pasajeros, 5 para ver los nombres en orden alfabetico, 6 para ver los pasajeros según el estado de los asientos, 7 para ver los pasajeros de adelante hacia atras del avion, 8 para ver la cantidad de pasajeros en el avion, 9 para ver el precio del asiento, 10 para salir")
    d = int(input())
    
    
                
    if d == 1:      #Reservar un asiento
        Nbr = generarNombre1()
        print(Nbr)
        (fila, silla) = generarSilla1()
        (x,y)=ubicarSilla(fila,silla)
        print(f"{(fila,silla)} : {(x,y)}")
        filan = 5
        if avion[x][y] != 0:
            for fila in avion:
                print(f'{filan} [ A:{fila[0]} B:{fila[1]} C:{fila[2]}  | ... | H:{fila[3]} J:{fila[4]} K:{fila[5]} ]')
                filan = filan + 1
            print("La silla no esta disponible")
            continue
        estado = "Reservado"
        puestos+=1
        if puestos > 110:
            precio = 200000
        elif puestos > 69:
            precio = 150000
        elif puestos >= 0:
            precio = 100000
            
        nombres.append([Nbr, silla, fila, estado, precio])
        avion[x][y]=1
        for fila in avion:
            print(f'{filan} [ A:{fila[0]} B:{fila[1]} C:{fila[2]}  | ... | H:{fila[3]} J:{fila[4]} K:{fila[5]} ]')
            filan = filan + 1
        
    
    elif d == 2:        #Comprar un asiento
        Nbr = generarNombre1()
        print(Nbr)
        (fila, silla) = generarSilla1()
        (x,y)=ubicarSilla(fila,silla)
        print(f"{(fila,silla)} : {(x,y)}")
        filan = 5
        if avion[x][y] != 0:
            for fila in avion:
                print(f'{filan} [ A:{fila[0]} B:{fila[1]} C:{fila[2]}  | ... | H:{fila[3]} J:{fila[4]} K:{fila[5]} ]')
                filan = filan + 1
            print("La silla no esta disponible")
            continue
        estado = "Comprado"
        puestos +=1
        if puestos > 110:
            precio = 200000
        elif puestos > 69:
            precio = 150000
        elif puestos >= 0:
            precio = 100000
        nombres.append([Nbr, silla, fila, estado])
        avion[x][y]=2
        for fila in avion:
            print(f'{filan} [ A:{fila[0]} B:{fila[1]} C:{fila[2]}  | ... | H:{fila[3]} J:{fila[4]} K:{fila[5]} ]')
            filan = filan + 1  
                
    elif d == 3:        #Cancelar un asiento
        Nbr = generarNombre1()
        print(Nbr)
        s = (input("Ingrese el asiento: "))
        f = int(input("Ingrese la fila de su asiento: "))
        (x,y)=ubicarSilla(f,s)        
        filan = 5
        if avion[x][y] == 2:
            for fila in avion:
                print(f'{filan} [ A:{fila[0]} B:{fila[1]} C:{fila[2]}  | ... | H:{fila[3]} J:{fila[4]} K:{fila[5]} ]')
                filan = filan + 1
            print("No se pueden cancelar los asientos comprados")
            continue
        estado = "Reservado"
        puestos -=1
        
        
        for persona in nombres:
            if persona[0] == Nbr:
                cancelado = nombres.pop(nombres.index(persona))

        avion[x][y]=0
        for fila in avion:
            print(f'{filan} [ A:{fila[0]} B:{fila[1]} C:{fila[2]}  | ... | H:{fila[3]} J:{fila[4]} K:{fila[5]} ]')
            filan = filan + 1
            
    elif d == 4:        #Ver la informacion de los pasajeros
        for nombre in nombres:
            print(nombre)
            
    elif d == 5:        #Ver la infromacion de los pasajeros en orden alfabetico
        nombres_alf = sorted(nombres)
        print(nombres_alf)
    
    elif d == 6:        #Pasajeros según el estado de la silla
        estadoSillas = sorted(nombres, key=lambda persona: 1 if persona[3] == 'Comprado' else 0)
        print(estadoSillas)
        
    elif d == 7:        #Pasajeros de adelante hacia atras
        ordenSillas = sorted(nombres, key=lambda persona: persona[2])
        print(ordenSillas)
        
    elif d==8: #Cantidad de pasajeros
        print(f"Cantidad de pasajeros en el avion:  {puestos}")
         
         
        
    elif d==9:  #Ver el precio del asiento segun los asientos disponibles
        if puestos > 110:    #110 es el 80% de los asientos disponibles
            precio = 200000
        elif puestos > 69:  #69 es el 50% de los asientos disponibles
            precio = 150000
        elif puestos >= 0:
            precio = 100000
        print(f"El precio del asiento es de: {precio}")
    
    elif d == 10:        #Cerrar el programa
        print("Hasta luego")
        break  
    
    