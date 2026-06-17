from models.libro import libro
class Prestamo:

    #Constructor
    def __init__(self, id, libro, usuario, fecha_prestamo, fecha_devolución, estado):
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolución = fecha_devolución
        self.estado = estado 

    def registrar_devolución(self, fecha_devolución):
        self.fecha_devolución = fecha_devolución
        self.estado = "Devuelto"
        self.libro.devolver()



