from dao.libro_dao import LibroDAO
from models.libro import Libro

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
        

def main():
    print("==== BIBLIOTECA UNIVARSITARIA ====")
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


if __name__ == "__main__":
    main()
    
