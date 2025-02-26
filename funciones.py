from os import system
import os
import json





def get_path_actual(nombre_archivo):
    """_summary_

    Args:
        nombre_archivo (_type_): Nombre del archivo actual

    Returns:
        _type_: la ubicacion del archivo en el que se trabaja
    """
    
    ubi = os.path.dirname(__file__)
    
    return os.path.join(ubi, nombre_archivo)

# ----------------------------------------------------------------
def cargar_archivo_csv(nombre_archivo:str):
    """archivo csv

    Args:
        nombre_archivo (str): Nombre del archivo
        
    """
    with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")
        for linea in archivo.readlines():
            archivo = {}
            linea = linea.strip("\n").split(",")
            id, user, likes, dislikes,followers = linea
            archivo["id"] = int(id)
            archivo["user"] = user
            archivo["likes"] = int(likes)
            archivo["dislikes"] = int(dislikes)
            archivo["followers"] = int(followers)
            lista.append(archivo)
            return lista
# ----------------------------------------------------------------
def imprimir_lista (posts):
    """Imprime la lista de posts en un formato tabular.

    Args:
    posts (list): Lista de listas donde cada lista contiene los datos de un post.
                  Cada lista debe contener al menos los siguientes elementos en orden:
                  - ID
                  - Nombre
                  - LIKES
                  - DISLIKES
                  - FOLLOWERS
    """
    print("                      LISTA DE POSTS")
    print("ID     Nombre            LIKES       DISLIKES    FOLLOWERS")
    print("------------------------------------------------------------------------")
    for post in posts:
        print(f"{post["id"]}    {post["user"]:17}    {post["likes"]:10}    {post["dislikes"]:10}     {post["followers"]:10}")
# ----------------------------------------------------------------
    

def asignar_numeros(posts) :
    """ asigna los numeros random
    Args:
        posts (type): description

    Returns:
        type: description
    """
    import random
    for post in posts :
        post["likes"] = random.randint(500,3000)
        post["dislikes"] = random.randint(300,3500)
        post["followers"] = random.randint(10000,20000)
    return posts
# ----------------------------------------------------------------


def crear_archivo_csv(posts:list, nombre):
    """crea un archivo csv con la lista que pasa por parametro

    Args:
        lista (list): lista con datos para crear archivo
    """

    csv_file = f"{nombre}.csv"

    with open(csv_file, 'w', newline='') as file:
        encabezado = "id,user,likes,dislikes,followers\n"
        file.write(encabezado)
        for post in posts:
            row = f'{post["id"]},{post["user"]},{post["likes"]},{post["dislikes"]},{post["followers"]}\n'
            file.write(row)
    print(f'{csv_file} fue creado correctamente.')

# ----------------------------------------------------------------
def mejores_posts(posts):
    """filtra y crea archivo de los mejores posts

    Args:
        posts (type): lista
    """
    mejores = []
    for post in posts :
        if(post["likes"] > 2000):
            mejores.append(post)

    if(len(mejores) > 0):
        crear_archivo_csv(mejores, "mejores")

# ----------------------------------------------------------------
def filtro_haters(posts):
    """ filtra y crea un archivo de los haters

    Args:
        posts (type): lista
    """
    haters = []
    for post in posts :
        if(post["dislikes"] > post["likes"]):
            haters.append(post)

    if(len(haters) > 0):
        crear_archivo_csv(haters,"haters")


# ----------------------------------------------------------------


def promedio_followers(posts):
    """promedia followers

    Args:
        posts (type): lista

    Returns:
        type: el promedio solo de los followers
    """
    total_followers = 0
    for post in posts:
        total_followers += post["followers"]
        promedio = total_followers / len(posts)

    return promedio
# ----------------------------------------------------------------


def mostrar_mas_popular(posts):
    """
    Muestra el nombre del usuario con el post más likeado y el número de likes.

    Args:
    posts (list): Lista de diccionarios donde cada diccionario contiene datos de un post.


    """
    if not posts:
        print("No hay posts para analizar.")
        return
    
    post_mas_popular = posts[0]
    for post in posts:
        if post[2] > post_mas_popular[2]:  
            post_mas_popular = post
    
    print(f"El usuario con el post más likeado es {post_mas_popular[1]} con {post_mas_popular[2]} likes.")  

def ordeno_lista(posts):
    """
    Ordena la lista de posts 

    Args:
    posts (list): Lista .
    Returns:
    list: Lista de posts ordenada por el nombre de usuario.
    """
    n = len(posts)
    for i in range(n):
        for j in range(0, n-i-1):
            if posts[j][1] > posts[j+1][1]:
                posts[j], posts[j+1] = posts[j+1], posts[j]
    return posts
# ----------------------------------------------------------------
def ordenar_y_guardar_json(posts, nombre_archivo_json):
    """
    Ordena los datos por nombre de usuario en orden ascendente y los guarda en un archivo JSON.

    Args:
    posts (list): Lista 
    nombre_archivo_json (str): Nombre del archivo JSON donde se guardarán los datos ordenados.
    """
    # Ordenar la lista de posts por nombre de usuario
    posts_ordenados = ordeno_lista(posts)

    # Convertir la lista ordenada a formato JSON
    posts_json = []
    for post in posts_ordenados:
        post_dict = {
            "id": post["id"],
            "users": post["user"],
            "likes": post["likes"],
            "dislikes": post["dislikes"],
            "followers": post["followers"]
        }
        posts_json.append(post_dict)

    # Guardar la lista ordenada en un archivo JSON
    with open(nombre_archivo_json, "w", encoding="UTF-8") as archivo_json:
        json.dump(posts_json, archivo_json, ensure_ascii=False, indent=4)
    
    print(f"Los datos ordenados han sido guardados en {nombre_archivo_json}.")
    
    
    
def limpiar_pantalla ():
    """limpia la pantalla

    Returns:
        _type_: limpia la terminal
    """
    return system ("cls")
# ----------------------------------------------------------------

def pausar ():
    """_summary_

    Returns:
        _type_: pausa el sistema en cada iteracion
    """
    return system("pause")
# ----------------------------------------------------------------

def menu():
    """crea un menu

    Returns:
        _type_: ingresa la opcion del menu
    """
    limpiar_pantalla()
    print("   MENU DE OPCIONES : ")
    print("1- Cargar archivo csv")
    print("2- mostar archivo ")
    print("3- cargar datos")
    print("4- crear un archivo con mejores posts ")
    print("5- crea un archivo con los haters ")
    print("6- muestra el promedio de followers ")
    print("7- crea un JSON por nombre de user ascendente  ")
    print("8- mostrar mas polpular  ")
    print("9- salir del programa  ")
    
    
    return input (" ingrese el nro de opcion que desea : ")
   