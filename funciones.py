from os import system
import csv
import random
import os






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
def cargar_archivo_csv(nombre_archivo_data:str):
    posts = []
    try:
        with open (get_path_actual(nombre_archivo_data), "r", encoding="UTF-8") as archivo_csv:
            contenido = csv.reader(archivo_csv, delimiter=',')
            next(contenido)
            for fila in contenido:
                posts.append(fila)

        if len(posts) > 0:
            return posts
    except:
        return "No se logro cargar el archivo correctamente."
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
    for post in posts[0]:
        print(f"{post[0]}    {post[1]:17}    {post[2]:10}    {post[3]:10}     {post[4]:10}")

# ----------------------------------------------------------------
    

def asignar_numeros(posts) :
    """ asigna los numeros random
    Args:
        posts (_type_): _description_

    Returns:
        _type_: _description_
    """
    import random
    for post in posts[0] :
        post[2] = random.randint(500,3000)
        post[3] = random.randint(300,3500)
        post[4] = random.randint(10000,20000)
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
        writer = csv.writer(file)
        for post in posts:
            row = f'{post[0]},{post[1]},{post[2]},{post[3]},{post[4]}\n'
            file.write(row)
    print(f'{csv_file} fue creado correctamente.')

# ----------------------------------------------------------------

def mejores_posts(posts):
    """filtra y crea archivo de los mejores posts

    Args:
        posts (_type_): lista
    """
    mejores = []
    for post in posts[0] :
        if(post[2] > 2000):
            mejores.append(post)

    if(len(mejores) > 0):
        crear_archivo_csv(mejores, "mejores" )

# ----------------------------------------------------------------
def filtro_haters(posts):
    """ filtra y crea un archivo de los haters

    Args:
        posts (_type_): lista
    """
    haters = []
    for post in posts[0] :
        if(post[3] > post[2]):
            haters.append(post)

    if(len(haters) > 0):
        crear_archivo_csv(haters,"haters")


# ----------------------------------------------------------------


def promedio_followers(posts):
    """promedia followers

    Args:
        posts (_type_): lista

    Returns:
        _type_: el promedio solo de los followers
    """
    total_followers = 0
    for post in posts[0]:
        total_followers += post[4]
        promedio = total_followers / len(posts[0])

    return promedio
# ----------------------------------------------------------------


def mostrar_mas_popular(posts):
    """
    Muestra el nombre del usuario con el post más likeado y el número de likes.

    Args:
    posts (list): Lista de diccionarios donde cada diccionario contiene datos de un post.
                  Cada diccionario debe tener una clave 'users' y 'likes'.

    """
    if not posts:
        print("No hay posts para analizar.")
        return
    
    post_mas_popular = posts[0]
    for post in posts:
        if post[2] > post_mas_popular[2]:  
            post_mas_popular = post
    
    print(f"El usuario con el post más likeado es {post_mas_popular[1]} con {post_mas_popular[2]} likes.")  


# ----------------------------------------------------------------


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
   