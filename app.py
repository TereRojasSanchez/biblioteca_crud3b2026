import flet as ft
from dao.libro_dao import LibroDAO

from ui.main_window import main_window
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

def ver_libros():
    try:
        libro_dao = LibroDAO()
        lista = libro_dao.obtener_todo()

        if len(lista) ==0:
            print("No hay libros registrados")
        else:
            for libro in lista:
                print(f"id: {libro.id} {libro.titulo} {libro.autor} {libro.isbn} {libro.disponible}")
        print("\n Conexion exitosa con la base de datos")

    except Exception as e:
        print("Error")
        print(e)

def insertar_libro():
    print("INSERTAR UN NUEVO LIBRO")
    titulo = input("Escribe el titulo: ")
    autor = int(input("Escribe el id del autor: "))
    isbn = input("Escribe el isbn")
    disponible = True
    try:
        libro_dao = LibroDAO()
        ultimo_id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(ultimo_id, titulo, autor, isbn, disponible )
        libro_dao.insertar(libro)
        print("Insercion del nuevo libro fue exitosa")
    except Exception as e:
        print("Error al insertar el libro")
        print(e)

def actualizar_libro():
    try: 
        libro_dao = LibroDAO()
        print("Lista de libros disponibles")
        libro_dao.obtener_todo()
        id = int=(input("Seleccione el id del libro a actualizar"))
        titulo = input("Escribe el titulo: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el isbn ")
        disponible = bool(input("Escribe s esta diponible:"))
        libro = Libro(id, titulo,autor,isbn,disponible)
        libro_dao.actualizar(libro)
        print("El libro fue actualizado con exito: ")
    except Exception as e:
        print("ERROR al actualizar el libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles")
        libro_dao.obtener_todo()
        id = int(input("Escriba el id del libro a eliminar:"))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el libro{id}")
        print(e)

def menu_libros():
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro existente")
    opcion = int(input("Selecciona una opcion (1-4):"))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()

    
def menu_usuarios():
    print("1. Ver todos los usuarios")
    print("2. Insertar un nuevo usuario")
    print("3. Actualizar un usuario")
    print("4. Eliminar un usuario")
    opcion = int(input("Selecciona una opcion (1-4):"))

    match opcion:
        case 1:
            ver_usuarios()
        case 2:
            insertar_usuario()
        case 3:
            actualizar_usuario()
        case 4:
            eliminar_usuario()

ft.app(target=main_window)
    
        

# def main():
#     print("==== BIBLIOTECA UNIVARSITARIA ====")
#     print("Menu de opciones:")
#     print("1. Libros")
#     print("2. usuarios")
#     opcion = int(input("Escribe tu opcion:"))
#     match opcion:
#         case 1: menu_libros()
#         case 2: menu_usuarios()
#     print("Saliendo del sistesma de Biblioteca universitaria .......")



    
# def ver_usuarios():
#     try:
#         usuario_dao = UsuarioDAO()
#         lista = usuario_dao.obtener_todo()

#         if len(lista) ==0:
#             print("No hay usuarios registrados")
#         else:
#             for usuario in lista:
#                 print(f"id: {usuario.id} {usuario.nombre} {usuario.matricula} {usuario.carrera} {usuario.correo} {usuario.activo}")
#         print("\n Conexion exitosa con la base de datos")

#     except Exception as e:
#         print("Error")
#         print(e)

# def insertar_usuario():
#     print("INSERTAR UN NUEVO USUARIO")
#     nombre = input("Escribe el nombre del usuario: ")   
#     matricula = (input("Escribe la matricula:  "))
#     carrera = (input("Escribe la carrera: "))
#     correo = input("Ingrese el correo:" )
#     activo = True
#     try:
#         usuario_dao = UsuarioDAO()
#         ultimo_id = usuario_dao.obtener_ultimo_id() + 1
#         usuario = Usuario(ultimo_id, nombre, matricula, carrera, correo, activo )
#         usuario_dao.insertar(usuario)
#         print("Insercion del usuario fue exitosa")
#     except Exception as e:
#         print("Error al insertar usuario")
#         print(e)

# def actualizar_usuario():
#     try:
#         usuario_dao = UsuarioDAO()

#         print("Lista de usuarios")
#         lista = usuario_dao.obtener_todo()

#         for usuario in lista:
#             print(f"id: {usuario.id} - {usuario.nombre} - {usuario.matricula}")

#         id = int(input("Seleccione el id del usuario a actualizar: "))
       
#         nombre = input("Escribe el nombre: ")
#         matricula = input("Escribe la matricula del usuario")
#         carrera = input("Escribe la carrera: ")
#         correo = input("Escribe el correo: ")
#         activo = True
        

#         usuario = Usuario(id, nombre,  matricula, carrera, correo, activo)
#         usuario_dao.actualizar(usuario)

#         print("El usuario fue actualizado con exito")

#     except Exception as e:
#         print("ERROR al actualizar usuario")
#         print(e)

# def eliminar_usuario():
#     try:
#         usuario_dao = UsuarioDAO()
#         print("Lista de usuarios disponibles")
#         lista = usuario_dao.obtener_todo()
#         for usuario in lista:
#             print(f"id: {usuario.id} - {usuario.nombre} - {usuario.matricula}") #Esto se lo añadi de mas yo para que salga la lista de usuarios


#         usuario_dao.obtener_todo()
#         id = int(input("Escriba el id del usuario a eliminar:"))
#         usuario_dao.eliminar(id)
#         print(f"El usuario {id} ha sido eliminado con éxito")
#     except Exception as e:
#         print(f"Error al eliminar usuario{id}")
#         print(e)




# if __name__ == "__main__":
#     main()
