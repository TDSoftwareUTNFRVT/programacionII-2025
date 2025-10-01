
import mysql.connector
from mysql.connector import Error


def conectar_mysql():
   
    try:
       
        conexion = mysql.connector.connect(
            host='localhost',          # Servidor MySQL
            database='EjemploBD',      # Nombre de la base de datos
            user='root',               # Usuario MySQL
            password=''                # Contraseña MySQL (cambiar según tu configuración)
        )
        
        if conexion.is_connected():
            print("Conexión exitosa a MySQL")
            info_servidor = conexion.get_server_info()
            print(f"Información del servidor: MySQL {info_servidor}")
            
            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            bd_actual = cursor.fetchone()
            print(f"Base de datos actual: {bd_actual[0]}")
            
            return conexion
            
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None


def crear_tabla_usuarios(conexion):
    
    try:
        cursor = conexion.cursor()
        
        crear_tabla = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            edad INT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        cursor.execute(crear_tabla)
        print("Tabla 'usuarios' creada o verificada correctamente")
        
    except Error as e:
        print(f"Error al crear tabla: {e}")


def insertar_usuario(conexion, nombre, email, edad):
    
    try:
        cursor = conexion.cursor()
        
        insertar_sql = "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)"
        datos_usuario = (nombre, email, edad)
        
        cursor.execute(insertar_sql, datos_usuario)
        conexion.commit()
        
        print(f"Usuario '{nombre}' insertado correctamente (ID: {cursor.lastrowid})")
        
    except Error as e:
        print(f"Error al insertar usuario: {e}")


def consultar_usuarios(conexion):
    
    try:
        cursor = conexion.cursor()
        
        consulta_sql = "SELECT id, nombre, email, edad, fecha_creacion FROM usuarios"
        cursor.execute(consulta_sql)
        
        usuarios = cursor.fetchall()
        
        print("\n Lista de usuarios:")
        print("-" * 80)
        print(f"{'ID':<5} {'Nombre':<20} {'Email':<30} {'Edad':<5} {'Fecha Creación'}")
        print("-" * 80)
        
        for usuario in usuarios:
            id_usuario, nombre, email, edad, fecha = usuario
            print(f"{id_usuario:<5} {nombre:<20} {email:<30} {edad or 'N/A':<5} {fecha}")
        
        print(f"\nTotal de usuarios: {len(usuarios)}")
        
    except Error as e:
        print(f"Error al consultar usuarios: {e}")


def buscar_usuario_por_email(conexion, email):
    try:
        cursor = conexion.cursor()
        
        
        buscar_sql = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(buscar_sql, (email,))
        
        usuario = cursor.fetchone()
        
        if usuario:
            print(f"\n Usuario encontrado:")
            print(f"   ID: {usuario[0]}")
            print(f"   Nombre: {usuario[1]}")
            print(f"   Email: {usuario[2]}")
            print(f"   Edad: {usuario[3] or 'N/A'}")
            print(f"   Fecha de creación: {usuario[4]}")
        else:
            print(f"No se encontró usuario con email: {email}")
            
    except Error as e:
        print(f"Error al buscar usuario: {e}")


def main():
    
    print("Ejemplo de conexión a MySQL")
    print("=" * 50)
    
    conexion = conectar_mysql()
    
    if conexion:
        try:
            crear_tabla_usuarios(conexion)
            
            print("\nInsertando usuarios de ejemplo...")
            insertar_usuario(conexion, "Juan Pérez", "juan.perez@email.com", 25)
            insertar_usuario(conexion, "María González", "maria.gonzalez@email.com", 30)
            insertar_usuario(conexion, "Carlos Rodríguez", "carlos.rodriguez@email.com", 22)
            
            consultar_usuarios(conexion)
            
            print("\nBuscando usuario por email...")
            buscar_usuario_por_email(conexion, "juan.perez@email.com")
            
        except Exception as e:
            print(f"Error en operaciones: {e}")
        
        finally:
            if conexion.is_connected():
                conexion.close()
                print("\nConexión cerrada")
    
    else:
        print("No se pudo establecer conexión con MySQL")
        print("\nVerifique:")
        print("• Que MySQL esté ejecutándose")
        print("• Las credenciales de conexión")
        print("• Que exista la base de datos 'EjemploBD'")


if __name__ == "__main__":
    main()
