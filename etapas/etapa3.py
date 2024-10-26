#--------------------------------------------------------------------
# Instalar con pip install mysql-connector-python
import mysql.connector
#--------------------------------------------------------------------

class Catalogo:
    """
    Esta clase proporciona métodos para administrar un catálogo de productos
    almacenados en una base de datos MySQL.
    """
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        """
        Inicializa una instancia de Catalogo y crea una conexión a la base de datos.

        Args:
            host (str): La dirección del servidor de la base de datos.
            user (str): El nombre de usuario para acceder a la base de datos.
            password (str): La contraseña del usuario.
            database (str): El nombre de la base de datos.
        """
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # El parámetro dictionary=True configura el cursor para que,
        # cuando se recuperen resultados de una consulta, estos se 
        # almacenen en un diccionario en lugar de una tupla. 
        self.conector = self.conn.cursor(dictionary=True)
        # Si la tabla 'productos' no existe, la creamos
        self.conector.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,                  
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255))''')
        self.conn.commit()

    #----------------------------------------------------------------
    def agregar_producto(self, codigo, nombre, descripcion, cantidad, precio, imagen):
        """
        Agrega un nuevo producto a la base de datos.

        Args:
            codigo (int): El código del producto.
            nombre (str): El nombre del producto.
            descripcion (str): La descripción del producto.
            cantidad (int): La cantidad en stock del producto.
            precio (float): El precio del producto.
            imagen (str): La URL de la imagen del producto.

        Returns:
            bool: True si el producto se agregó con éxito, False si ya existe un producto con el mismo código.
        """
        # Verificamos si ya existe un producto con el mismo código
        self.conector.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        producto_existe = self.conector.fetchone()
        if producto_existe:
            return False

        # Si no existe, agregamos el nuevo producto a la tabla
        sql = f"INSERT INTO productos \
               (codigo, nombre, descripcion, cantidad, precio, imagen_url) \
               VALUES \
               ({codigo},'{nombre}','{descripcion}', {cantidad}, {precio}, '{imagen}')"
        self.conector.execute(sql)
        self.conn.commit()
        return True

    #----------------------------------------------------------------
    def consultar_producto(self, codigo):
        """
        Consulta un producto a partir de su código.

        Args:
            codigo (int): El código del producto a consultar.

        Returns:
            dict: Un diccionario con la información del producto o None si no se encuentra.
        """
        # Consultamos un producto a partir de su código
        self.conector.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.conector.fetchone()

    #----------------------------------------------------------------
    def modificar_producto(self, codigo, nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen):
        """
        Modifica los datos de un producto a partir de su código.

        Args:
            codigo (int): El código del producto a modificar.
            nuevo_nombre (str): El nuevo nombre del producto.
            nueva_descripcion (str): La nueva descripción del producto.
            nueva_cantidad (int): La nueva cantidad en stock del producto.
            nuevo_precio (float): El nuevo precio del producto.
            nueva_imagen (str): La nueva URL de la imagen del producto.
            

        Returns:
            bool: True si se realizó la modificación con éxito, False si no se encontró el producto.
        """
        # Modificamos los datos de un producto a partir de su código
        sql = f"UPDATE productos SET \
                    nombre = '{nuevo_nombre}', \
                    descripcion = '{nueva_descripcion}', \
                    cantidad = {nueva_cantidad}, \
                    precio = {nuevo_precio}, \
                    imagen_url = '{nueva_imagen}' \
                WHERE codigo = {codigo}"
        self.conector.execute(sql)
        self.conn.commit()
        return self.conector.rowcount > 0

    #----------------------------------------------------------------
    def listar_productos(self):
        """
        Muestra en pantalla un listado de todos los productos en la tabla.
        """
        # Mostramos en pantalla un listado de todos los productos en la tabla
        self.conector.execute("SELECT * FROM productos")
        productos = self.conector.fetchall()
        print("-" * 40)
        for producto in productos:
            print(f"Código.....: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print("-" * 40)

    #----------------------------------------------------------------
    def eliminar_producto(self, codigo):
        """
        Elimina un producto de la tabla a partir de su código.

        Args:
            codigo (int): El código del producto a eliminar.

        Returns:
            bool: True si se eliminó el producto con éxito, False si no se encontró el producto.
        """
        # Eliminamos un producto de la tabla a partir de su código
        self.conector.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.conector.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_producto(self, codigo):
        """
        Muestra los datos de un producto a partir de su código.

        Args:
            codigo (int): El código del producto a mostrar.
        """
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código.....: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")

#--------------------------------------------------------------------
# Ejemplo de uso con MariaDB
catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')

# Agregamos productos a la tabla
catalogo.agregar_producto(1,'Maki', 'Roll con el alga por fuera, arroz y langostinos.', 10, 10000, 'maki.jpg')
catalogo.agregar_producto(2, 'Nigiri','Bocado de arroz cubierto de salmón.', 10, 12000, 'nigiri.jpg')
catalogo.agregar_producto(3, 'Onigiri','Bocado de arroz rellena o mezclada con otros ingredientes.', 15, 11500, 'onigiri.jpg')
catalogo.agregar_producto(4, 'Uramaki','Roll de arroz relleno de alga nori, salmón y aguacate. ', 8, 10000, 'uramaki.jpg')
catalogo.agregar_producto(5, 'Uramaki Tempura','Roll de arroz relleno de alga nori y salmón envuelto en una deliciosa tempura ', 8, 12000, 'uramakitempura.jpg')
catalogo.agregar_producto(6, 'Nigiri Especial','Bocado de arroz cubierto de salmón y salsa.', 10, 12000, 'nigiriespecial.jpg')
catalogo.agregar_producto(7, 'Combinado','Productos de sushi combinados.', 10, 12000, 'combinados.jpg')
catalogo.agregar_producto(8,'Maki Especial', 'Roll con el alga por fuera, arroz y langostinos y salsa.', 10, 10000, 'makiespecial.jpg')
catalogo.agregar_producto(9,'Kimbap', 'Roll con el alga por fuera, arroz y verduras.', 12, 15000, 'kimbap.jpg')
catalogo.agregar_producto(10, 'Nigiri de Atún','Bocado de arroz cubierto de atún.', 10, 11000, 'nigirideatun.jpg')

# Consultamos un producto y lo mostramos
producto = catalogo.consultar_producto(1)
if producto:
    print(f"Producto encontrado: {producto['descripcion']}")
else:
    print("Producto no encontrado.")

# Modificamos un producto y lo mostramos
catalogo.modificar_producto(1,'Maki', 'Roll con el alga por fuera, arroz y salmón.', 10, 15000, 'maki.jpg')
catalogo.mostrar_producto(1)

# Listamos todos los productos
catalogo.listar_productos()

# Eliminamos un producto
# catalogo.eliminar_producto(2)
# catalogo.listar_productos()
