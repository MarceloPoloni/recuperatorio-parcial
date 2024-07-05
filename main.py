from funciones import *
import json


posts= []
bandera_primer_ingreso =True
bandera_segundo_ingreso = False
seguir = "si"

while seguir == "si":
    match menu():
        case "1":
            limpiar_pantalla()
            nombre_archivo = input("ingrese el nombre del archivo a cargar : ")
            lista = cargar_archivo_csv(nombre_archivo)
            if isinstance(lista, list):
                posts.append(lista)
                print ("El archivo fue cargado con exito.")
                bandera_primer_ingreso = False
            else:
                print ("no se cargo el archivo")          
                
        case "2":
            limpiar_pantalla()
            if bandera_primer_ingreso == False:
                if len(posts) > 0:
                    imprimir_lista(posts)
            else:
                print ("La lista indicada se encuentra vacia")
        
        case "3":
            if bandera_primer_ingreso == False:
                asignar_numeros(posts)
                bandera_segundo_ingreso = False
                print("se cargaron los tiempos")
            else :
                print("primero debe cargar el archivo")
        
        case "4":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                mejores_posts(posts)
            else:
                print("Primero debe cargar el archivo y asignarle los datos")
        
        case "5":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                filtro_haters(posts)
                print("Archivo creado correctamente")
            else:
                print("Primero debe cargar el archivo y asignarle los datos")
                
            
        
        case "6":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                promedio_followers(posts)
                
            else:
                print("Primero debe cargar el archivo y asignarle los datos")
                
            
        case "7":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                nombre_archivo = input ("ingrese nombre del archivo json")
                ordenar_y_guardar_json(posts, nombre_archivo)
            else:
                print("Primero debe cargar el archivo y asignarle los datos")
                
        case "8":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                mostrar_mas_popular(posts)
                
            else:
                print("Primero debe cargar el archivo y asignarle los datos")
                
        case "9":
            limpiar_pantalla()
            print("Se cierra el programa, muchas gracias!")
            bandera_primer_ingreso = True
            bandera_segundo_ingreso= True
            break
        case _:
            print("Opción no válida. Intenta de nuevo.")
    pausar()
    seguir = input("¿Deseas continuar? (si/no): ").lower()
    if seguir == "no":
        print("muchas gracias , que tenga buen dia!") 
    else :
        print("ingrese opcion valida")