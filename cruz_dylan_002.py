equipos=[]
import csv
def menu():
    while True:
        print("")
        print(".-.-.- menu -.-.-.")
        print("")
        print("1.- Agregar equipo")
        print("2.- Listar Equipo")
        print("3.- Actualizar nombre de equipo pór id")
        print("4.- Generar BBDD")
        print("5.- Cargar BBDD")
        print("6.- Estadisticas")
        print("0.- Salir")
        print("\n"*3)
        op=int(input("Ingrese una opcion : "))

        if op==1:
            agregar_equipo(equipos)
        elif op==2:
            print(".-.-.- LISTA DE EQUIPOS -.-.-.")
            print("")
            for equipo in equipos:
                print(f"ID :{equipo[0]} , Nombre : {equipo[1]} , Puntos : {equipo[2]} , Categoria : {equipo[3]}")
        elif op==3:
            print("")
            print(".-.-.- ACTUALIZACION DE NOMBRE -.-.-.")
            re=int(input("Ingrese id de equipo a actualizar : "))
            for lis in equipos:
                if lis[0]==re:
                    nuevo=input("Ingrese nuevo nombre : ")
                    lis[1]=nuevo
                    print("creado correctamente")
                
        elif op==4:
            print("")
            print(".-.-.- Generando base de datos -.-.-.")
            
            with open ('bbdd_equipos.csv','w',newline='') as bbdd_equipos:
                escritor_csv=csv.writer(bbdd_equipos)
                escritor_csv.writerow(['equipo','nombre','puntos','categoria'])
                escritor_csv.writerows(equipos)
                print("")
                print("Archivo creado correctamente")

        elif op==5:
            print("")
            print(".-.-.- Cargando base de datos -.-.-.")
            equipos.clear()
            cont=1
            with open ('bbdd_equipos.csv','r',newline='') as bbdd_equipos:
                lector_csv=csv.reader(bbdd_equipos)
                for fila in lector_csv:
                    if cont==0:
                        cont+=1
                        continue
                I=int(fila[0])
                N=fila[1]
                P=int(fila[2])
                C=fila[3]
                equipito=[I,N,P,C]
                equipos.append(equipito)
        elif op==6:
            total=0
            the_strongest=0
            for equip in equipos:
                total=total+equip[2]
            promedio=total/len(equipos)
            print(f"Puntaje promedio por equipo : {promedio}")
            for equip in equipos:
                if the_strongest<equip[2]:
                    the_strongest=equip[2]
            print(f"Puntaje mas alto : {the_strongest}")
            print(f"equipo mas alto : {equip[1]}")

        elif op==0:
            print("saliendo ....")
            break
        
        else:
            print("ingrese una opcion valida....")
            
def agregar_equipo(equipos):
    ID=int(input("Ingrese ID del equipo : "))
    nombre=input("Ingrese nombre del equipo : ")
    puntos=int(input("Ingrese cantidad de puntos del equipo : "))
    if puntos>=0 or puntos<=150:
        categ=categoria(puntos)
    else:
        print("ingrese una cantidad valida...")
    equipo=[ID,nombre,puntos,categ]
    equipos.append(equipo)
    print("equipo agregado correctamente")
        
def categoria(puntos):
    if puntos>120:
        return("IDOLOS")
    if puntos>=81 or 120<= puntos:
        return("Avanzado")
    if puntos>=41 or 80<=puntos:
        return("Principiante")
    if puntos>=0 or 40>=puntos:
        return("Amateur")

menu()
