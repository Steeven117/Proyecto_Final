##Programa Organizador de Horarios

print("--------------------------------------------")
print("--------------BIENVENIDO--------------------")
print("--------------------------------------------")

#INPUT


LUNES=1
MARTES=2
MIERCOLES=3
JUEVES=4
VIERNES=5
SABADO=6
lista_lunes=[]
lista_martes=[]
lista_miercoles=[]
lista_jueves=[]
lista_viernes=[]
lista_sabado=[]

def Menu():
    print("***********Programa para organizar Horarios***********")
    print("Menu:")
    print("1. Ingresar Actividad")
    print("2. Borrar Actividad")
    print("3. Ver Horario")
    print("4. Generar Excel")
    print("5. Salir")
    pass

def Menu_a():
    print("1. Lunes")
    print("2. Martes")
    print("3. Miercoles")
    print("4. Jueves")
    print("5. Viernes")
    print("6. Sabado")
    print("7. Volver Menu anterior")
    pass

def Menu_m():
    print("1. Ingrese una materia")
    print("2. Volver al menu anterior")
    pass

opcion=0

#PROCESSIBG

while(opcion!=5):
    Menu()
    opcion=int(input("Escoja una opcion:"))

    if(opcion==1):
        opcion_a=0
        while(opcion_a!=7):
            Menu_a()
            opcion_a=int(input("Escoja una opcion:"))
            if(opcion_a==LUNES):
                opcion_m=0
                while(opcion_m!=2):
                    Menu_m()
                    opcion_m=int(input("Escoja una opcion:"))

                    if(opcion_m==1):
                        materia=input("Ingrese el nombre de la materia:").lower()
                        lista_lunes.append(materia)
                        pass
                    elif(opcion_m==2):
                        pass
                    else:
                       print("Opcion no Existe")
                    pass
                pass

            elif(opcion_a==MARTES):
                opcion_m=0
                while(opcion_m!=2):
                    Menu_m()
                    opcion_m=int(input("Escoja una opcion:"))

                    if(opcion_m==1):
                        materia=input("Ingrese el nombre de la materia:").lower()
                        lista_martes.append(materia)
                        pass
                    elif(opcion_m==2):
                        pass
                    else:
                       print("Opcion no Existe")
                    pass
                pass
            elif(opcion_a==MIERCOLES):
                opcion_m=0
                while(opcion_m!=2):
                    Menu_m()
                    opcion_m=int(input("Escoja una opcion:"))

                    if(opcion_m==1):
                        materia=input("Ingrese el nombre de la materia:").lower()
                        lista_miercoles.append(materia)
                        pass
                    elif(opcion_m==2):
                        pass
                    else:
                       print("Opcion no Existe")
                    pass
                pass
                pass
            elif(opcion_a==JUEVES):
                opcion_m=0
                while(opcion_m!=2):
                    Menu_m()
                    opcion_m=int(input("Escoja una opcion:"))

                    if(opcion_m==1):
                        materia=input("Ingrese el nombre de la materia:").lower()
                        lista_jueves.append(materia)
                        pass
                    elif(opcion_m==2):
                        pass
                    else:
                       print("Opcion no Existe")
                    pass
                pass
                pass
            elif(opcion_a==VIERNES):
                opcion_m=0
                while(opcion_m!=2):
                    Menu_m()
                    opcion_m=int(input("Escoja una opcion:"))

                    if(opcion_m==1):
                        materia=input("Ingrese el nombre de la materia:").lower()
                        lista_viernes.append(materia)
                        pass
                    elif(opcion_m==2):
                        pass
                    else:
                       print("Opcion no Existe")
                    pass
                pass
                pass
            elif(opcion_a==SABADO):
                opcion_m=0
                while(opcion_m!=2):
                    Menu_m()
                    opcion_m=int(input("Escoja una opcion:"))

                    if(opcion_m==1):
                        materia=input("Ingrese el nombre de la materia:").lower()
                        lista_sabado.append(materia)
                        pass
                    elif(opcion_m==2):
                        pass
                    else:
                       print("Opcion no Existe")
                    pass
                pass
                pass
            elif(opcion_a==7):
                pass
            else:
                print('Opcion no Existe')
                pass
            pass

        pass
    elif(opcion==2):
        #borrar actividad
        opcion_borrar_actividad=0
        while(opcion_borrar_actividad!=7):
            Menu_a()
            opcion_borrar_actividad=int(input("Ingrese el dia donde desea borrar la materia:"))
            if(opcion_borrar_actividad==LUNES):
                materia_borrar=input("Escriba la materia a borrar:").lower()
                try:
                    lista_lunes.remove(materia_borrar) 
                    pass
                except:
                    print('Materia materia no existe en este dia')
                    pass

                pass

                pass

                
            

                pass
 
                pass
            elif(opcion_borrar_actividad==MARTES):
                pass
            elif(opcion_borrar_actividad==MIERCOLES):
                pass
            elif(opcion_borrar_actividad==JUEVES):
                pass    
            elif(opcion_borrar_actividad==VIERNES):
                pass
            elif(opcion_borrar_actividad==SABADO):
                pass
            elif(opcion_borrar_actividad==7):
                pass
            else:
                print("opcion no existe")
                pass

            pass

        pass
    elif(opcion==3):
        print("Lunes:")
        print(lista_lunes)
        print("Martes:")
        print(lista_martes)
        print("Miercoles:")
        print(lista_miercoles)
        print("Juves:")
        print(lista_jueves)
        print("Viernes:")
        print(lista_viernes)
        print("Sabado:")
        print(lista_sabado)


        pass
    elif(opcion==4):
        print("Generando Excel....")
        pass
    elif(opcion==5):
        print("Programa Finalizado")
        pass
    else:
        print("Opcion no exite")
    
    pass
