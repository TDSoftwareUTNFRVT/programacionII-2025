import mysql.connector
from mysql.connector import Error


class ConexionMySQL:
    
    def __init__(self, host='localhost', database='EjemploBD', user='root', password=''):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conexion = None
        self.cursor = None
    
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            
            if self.conexion.is_connected():
                self.cursor = self.conexion.cursor()
                print("Conexión exitosa a MySQL")
                
                info_servidor = self.conexion.get_server_info()
                print(f"Información del servidor: MySQL {info_servidor}")
                
                self.cursor.execute("SELECT DATABASE();")
                bd_actual = self.cursor.fetchone()
                print(f"Base de datos actual: {bd_actual[0]}")
                
                return True
                
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return False
    
    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")
    
    def ejecutar_consulta(self, query, parametros=None):
        try:
            if parametros:
                self.cursor.execute(query, parametros)
            else:
                self.cursor.execute(query)
            
            return self.cursor.fetchall()
            
        except Error as e:
            print(f"Error en consulta: {e}")
            return None
    
    def ejecutar_comando(self, query, parametros=None):
        try:
            if parametros:
                self.cursor.execute(query, parametros)
            else:
                self.cursor.execute(query)
            
            self.conexion.commit()
            return True
            
        except Error as e:
            print(f"Error en comando: {e}")
            self.conexion.rollback()
            return False


class Usuario:
    
    def __init__(self, nombre, email, edad, usuario_id=None, fecha_creacion=None):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.fecha_creacion = fecha_creacion
    
    def __str__(self):
        return f"Usuario(ID: {self.usuario_id}, Nombre: {self.nombre}, Email: {self.email}, Edad: {self.edad})"
    
    def validar(self):
        if not self.nombre or not self.email:
            return False, "Nombre y email son obligatorios"
        
        if self.edad and (self.edad < 0 or self.edad > 150):
            return False, "La edad debe estar entre 0 y 150 años"
        
        if '@' not in self.email:
            return False, "Email debe tener formato válido"
        
        return True, "Datos válidos"


class GestorUsuarios:
    
    def __init__(self, conexion_db):
        self.db = conexion_db
    
    def crear_tabla(self):
        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            edad INT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        if self.db.ejecutar_comando(crear_tabla_sql):
            print("Tabla 'usuarios' creada o verificada correctamente")
            return True
        return False
    
    def insertar_usuario(self, usuario):
        es_valido, mensaje = usuario.validar()
        if not es_valido:
            print(f"Error de validación: {mensaje}")
            return False
        
        insertar_sql = "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)"
        parametros = (usuario.nombre, usuario.email, usuario.edad)
        
        if self.db.ejecutar_comando(insertar_sql, parametros):
            usuario.usuario_id = self.db.cursor.lastrowid
            print(f"Usuario '{usuario.nombre}' insertado correctamente (ID: {usuario.usuario_id})")
            return True
        return False
    
    def obtener_todos_usuarios(self):
        consulta_sql = "SELECT id, nombre, email, edad, fecha_creacion FROM usuarios"
        resultados = self.db.ejecutar_consulta(consulta_sql)
        
        if resultados is not None:
            usuarios = []
            for fila in resultados:
                usuario = Usuario(
                    nombre=fila[1],
                    email=fila[2],
                    edad=fila[3],
                    usuario_id=fila[0],
                    fecha_creacion=fila[4]
                )
                usuarios.append(usuario)
            return usuarios
        return []
    
    def buscar_usuario_por_email(self, email):
        buscar_sql = "SELECT id, nombre, email, edad, fecha_creacion FROM usuarios WHERE email = %s"
        resultados = self.db.ejecutar_consulta(buscar_sql, (email,))
        
        if resultados and len(resultados) > 0:
            fila = resultados[0]
            return Usuario(
                nombre=fila[1],
                email=fila[2],
                edad=fila[3],
                usuario_id=fila[0],
                fecha_creacion=fila[4]
            )
        return None
    
    def actualizar_usuario(self, usuario):
        es_valido, mensaje = usuario.validar()
        if not es_valido:
            print(f"Error de validación: {mensaje}")
            return False
        
        actualizar_sql = "UPDATE usuarios SET nombre = %s, email = %s, edad = %s WHERE id = %s"
        parametros = (usuario.nombre, usuario.email, usuario.edad, usuario.usuario_id)
        
        if self.db.ejecutar_comando(actualizar_sql, parametros):
            print(f"Usuario '{usuario.nombre}' actualizado correctamente")
            return True
        return False
    
    def eliminar_usuario(self, usuario_id):
        eliminar_sql = "DELETE FROM usuarios WHERE id = %s"
        
        if self.db.ejecutar_comando(eliminar_sql, (usuario_id,)):
            print(f"Usuario con ID {usuario_id} eliminado correctamente")
            return True
        return False
    
    def mostrar_usuarios(self, usuarios):
        if not usuarios:
            print("No hay usuarios registrados")
            return
        
        print("\nLista de usuarios:")
        print("-" * 80)
        print(f"{'ID':<5} {'Nombre':<20} {'Email':<30} {'Edad':<5} {'Fecha Creación'}")
        print("-" * 80)
        
        for usuario in usuarios:
            edad_str = str(usuario.edad) if usuario.edad else 'N/A'
            print(f"{usuario.usuario_id:<5} {usuario.nombre:<20} {usuario.email:<30} {edad_str:<5} {usuario.fecha_creacion}")
        
        print(f"\nTotal de usuarios: {len(usuarios)}")


class AplicacionUsuarios:
    
    def __init__(self):
        self.db = ConexionMySQL()
        self.gestor = None
    
    def inicializar(self):
        print("Sistema de Gestión de Usuarios - Versión OOP")
        print("=" * 60)
        
        if not self.db.conectar():
            print("No se pudo conectar a la base de datos")
            return False
        
        self.gestor = GestorUsuarios(self.db)
        
        if not self.gestor.crear_tabla():
            print("No se pudo crear la tabla")
            return False
        
        return True
    
    def ejecutar_ejemplo(self):
        print("\nInsertando usuarios de ejemplo...")
        
        usuarios_ejemplo = [
            Usuario("Juan Pérez", "juan.perez@email.com", 25),
            Usuario("María González", "maria.gonzalez@email.com", 30),
            Usuario("Carlos Rodríguez", "carlos.rodriguez@email.com", 22),
            Usuario("Ana López", "ana.lopez@email.com", 28)
        ]
        
        for usuario in usuarios_ejemplo:
            self.gestor.insertar_usuario(usuario)
        
        print("\nConsultando todos los usuarios...")
        usuarios = self.gestor.obtener_todos_usuarios()
        self.gestor.mostrar_usuarios(usuarios)
        
        print("\nBuscando usuario por email...")
        usuario_encontrado = self.gestor.buscar_usuario_por_email("juan.perez@email.com")
        if usuario_encontrado:
            print(f"   {usuario_encontrado}")
        else:
            print("   Usuario no encontrado")
        
        if usuario_encontrado:
            print("\nActualizando usuario...")
            usuario_encontrado.edad = 26
            self.gestor.actualizar_usuario(usuario_encontrado)
    
    def finalizar(self):
        if self.db:
            self.db.desconectar()


def main():
    app = AplicacionUsuarios()
    
    try:
        if app.inicializar():
            app.ejecutar_ejemplo()
        else:
            print("❌ Error al inicializar la aplicación")
            print("\n📋 Verifique:")
            print("• Que MySQL esté ejecutándose")
            print("• Las credenciales de conexión")
            print("• Que exista la base de datos 'EjemploBD'")
    
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    finally:
        app.finalizar()


if __name__ == "__main__":
    main()