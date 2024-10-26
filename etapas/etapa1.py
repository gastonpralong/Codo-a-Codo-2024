productos = []

def agregar_producto(codigo,nombre, descripcion, cantidad, precio, imagen):

    if consultar_producto(codigo):
        return False  # Ya existe un producto con el mismo código, no se agrega.

    nuevo_producto = {
        'codigo': codigo,  
        'nombre': nombre,            # Asigna el valor del argumento 'nombre' al atributo 'codigo' del nuevo producto.
        'descripcion': descripcion,      # Asigna el valor del argumento 'categoria' al atributo 'descripcion' del nuevo producto.
        'cantidad': cantidad,        # Asigna el valor del argumento 'cantidad' al atributo 'cantidad' del nuevo producto.
        'precio': precio,            # Asigna el valor del argumento 'precio' al atributo 'precio' del nuevo producto.
        'imagen': imagen            # Asigna el valor del argumento 'imagen' al atributo 'imagen' del nuevo producto.
      }

      # Y lo agregamos a nuestro arreglo.
    productos.append(nuevo_producto) # Agrega el nuevo producto a la lista 'productos'.
    return True

# Función para consultar un producto a partir de su código
# -------------------------------------------------------------------
def consultar_producto(codigo):
   # Recorremos la lista de productos...
    for producto in productos:
        # Y si el nombre es el correcto,
        if producto['codigo'] == codigo:
            # Regresamos el diccionario correspondiente.
            return producto
    # Si el bucle finaliza sin encontrar el producto,
    # regresamos "falso."
    return False

# Función para modificar los datos de un producto a partir de su código
# -------------------------------------------------------------------
def modificar_producto(codigo,nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen):
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # ...actualizamos los valores de cada clave del diccionario
            producto['nombre'] = nuevo_nombre
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            # Como no hay otro producto con ese código, salimos del bucle.
            return True
            # Si llegamos aquí, el producto no existe.      
    return False


# Función para obtener un listado de los productos en pantalla
# -------------------------------------------------------------------
def listar_productos():
    """
    Muestra en pantalla un listado de los productos existentes.
    """
    # Recorremos la lista de productos...
    print("-" * 50)
    for producto in productos:
        # Y mostramos los datos de cada uno de ellos.
        print(f"Código: {producto['codigo']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")
        print(f"Imagen: {producto['imagen']}")
        print("-" * 50)

# -------------------------------------------------------------------
# Función para eliminar un producto a partir de su código
# -------------------------------------------------------------------

def eliminar_producto(codigo):
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # ...lo quitamos de la lista.
            productos.remove(producto)
            # Como no hay otro producto con ese código, salimos del bucle.
            return True
    # Si llegamos aquí, el producto no existe.
    return False


# Agregamos productos a la lista:
agregar_producto(1,'Maki', 'Roll con el alga por fuera, arroz y langostinos.', 10, 10000, 'maki.jpg')
agregar_producto(2, 'Nigiri','Bocado de arroz cubierto de salmón.', 10, 12000, 'nigiri.jpg')
agregar_producto(3, 'Onigiri','Bocado de arroz rellena o mezclada con otros ingredientes.', 15, 11500, 'onigiri.jpg')
agregar_producto(4, 'Uramaki','Roll de arroz relleno de alga nori, salmón y aguacate. ', 8, 10000, 'uramaki.jpg')
agregar_producto(5, 'Uramaki Tempura','Roll de arroz relleno de alga nori y salmón envuelto en una deliciosa tempura ', 8, 12000, 'uramakitempura.jpg')
agregar_producto(6, 'Nigiri Especial','Bocado de arroz cubierto de salmón y salsa.', 10, 12000, 'nigiriespecial.jpg')
agregar_producto(7, 'Combinado','Productos de sushi combinados.', 10, 12000, 'combinados.jpg')
agregar_producto(8,'Maki Especial', 'Roll con el alga por fuera, arroz y langostinos y salsa.', 10, 10000, 'makiespecial.jpg')
agregar_producto(9,'Kimbap', 'Roll con el alga por fuera, arroz y verduras.', 12, 15000, 'kimbap.jpg')
agregar_producto(10, 'Nigiri de Atún','Bocado de arroz cubierto de atún.', 10, 11000, 'nigirideatun.jpg')

# Eliminamos un producto del stock.
#eliminar_producto(5)  

#Consultar un producto por su código
#producto = consultar_producto(1)
#if producto:
    #print(f"Producto encontrado: {producto['nombre']}")
#else:
#     print("Producto no encontrado.")

# Modificar un producto por su código
 #modificar_producto(1,'Maki', 'Roll con el alga por fuera, arroz y langostinos.', 10, 10000, 'maki.jpg')

# Listamos todos los productos en pantalla
listar_productos()