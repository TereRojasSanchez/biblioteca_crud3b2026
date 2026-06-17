from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:
    def obtener_todo(self):
        conexion = conexion.obetener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELE * FROM libro")
        registros = cursor.fetchall()

        libros = []
        for registro in registro:
            libro = libro(
                id = registro[0],
                titulo = registro[1],
                autor = registro[2],
                isbn = registro[3],
                disponible = registro[4],
            )
            libros.apped(libro)
        cursor.close()
        conexion.close()
        return libros
    
    #INSERT
    def insertar(self,libro):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """ 
        INSERT INTO libro(titulo,autor,isbn,disponible)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(sql,(
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible

        ))
        conexion.commit()
        cursor.close()
        conexion.close()

        #UPDATE
        def actualizar(self, libro):
            conexion = conexion.obtener_conexion()
            cursor = conexion.cursor()

            sql = """"
            UPDATE libro
            SET titulo = %s, autor = %s, isbn = %s, disponible = %s
            WHERE id = %s
            """

            cursor.execute(sql, (
                           libro.titulo,
                           libro.autor,
                           libro.isbn,
                           libro.disponible
                           libro.id
                            ) )
            
            conexion.commit()
            cursor.close()
            conexion.close()

        #DELETE
        def eliminar(self,id):
            conexion = conexion.obtener_conexion()
            cursor = conexion.cursor()

            cursor.execute("DELETE FROM libro WHERE id = %s", (id))

            conexion.commit()
            cursor.close()
            conexion.close()

       