# Definimos la clase Catalogo
class Catalogo:
    # Lista de productos, compartida por todas las instancias de Catalogo.
    productos = []

    # ---------------------------------------------------------------
    # Método para agregar un producto al catálogo
    def agregar_producto(self, codigo, nombre, descripcion, cantidad, precio, imagen):
        # Verificamos si el producto ya existe en el catálogo
        if self.consultar_producto(codigo):
            return False

        # Creamos un nuevo producto en forma de diccionario
        nuevo_producto = {
            'codigo': codigo,
            'nombre': nombre,       
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen
        }
        
        # Agregamos el nuevo producto a la lista de productos en el catálogo
        self.productos.append(nuevo_producto)
        return True
    
    # ---------------------------------------------------------------
    # Método para consultar un producto por código
    def consultar_producto(self, codigo):
        # Buscamos el producto en la lista de productos
        for producto in self.productos:
            if producto['codigo'] == codigo:
                return producto
        return None
    
    # ---------------------------------------------------------------
    # Método para modificar los detalles de un producto
    def modificar_producto(self, codigo,nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                # Actualizamos los detalles del producto con los nuevos valores
                producto['nombre'] = nuevo_nombre
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen

                return True
        return False
    
    # ---------------------------------------------------------------
    # Método para listar todos los productos en el catálogo
    def listar_productos(self):
        # Imprimimos un encabezado
        print("-" * 50)
        # Recorremos la lista de productos e imprimimos sus detalles
        for producto in self.productos:
            print(f"Código.....: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen']}")
            print("-" * 50)

    # ---------------------------------------------------------------
    # Método para eliminar un producto por código
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                # Eliminamos el producto de la lista de productos
                self.productos.remove(producto)
                return True
        return False
    
    # ---------------------------------------------------------------
    # Método para mostrar los detalles de un producto por código
    def mostrar_producto(self, codigo):
        # Consultamos el producto por su código
        producto = self.consultar_producto(codigo)
        if producto:
            # Imprimimos los detalles del producto
            print("-" * 50)
            print(f"Código.....: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen']}")
            print("-" * 50)
        else:
            print("Producto no encontrado.")

# -------------------------------------------------------------------
# Ejemplo de uso de la clase Catalogo
# -------------------------------------------------------------------
catalogo = Catalogo()
catalogo.agregar_producto(1,'Maki', 'Roll con el alga por fuera, arroz y langostinos.', 10, 10000, 'maki.jpg')
catalogo.agregar_producto(2, 'Nigiri','Bocado de arroz cubierto de salmón.', 10, 12000, 'nigiri.jpg')
catalogo.listar_productos()
catalogo.mostrar_producto(1)
catalogo.eliminar_producto(1)
catalogo.listar_productos()