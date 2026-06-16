import psycopg2
class conexion:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB-NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port =os.getenv("DB_POTR")
        )