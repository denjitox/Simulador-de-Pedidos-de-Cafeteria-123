# Instructivo de funcionamiento detallado

Este documento explica cómo entender `Simulador de Pedidos de Cafeteria.py`.

- El programa no usa argumentos de línea de comandos; funciona con un menú interactivo.

1) Menú principal del programa
Al iniciar, el sistema muestra estas opciones:

1. `Sesión de mozo`
2. `Administración (Gerente)`
3. `Cierre del día`
4. `Salir`

2) Sesión de mozo
Esta opción permite a un mozo crear pedidos y consultar su total.

- El sistema pide nombre y clave.
- Si el mozo no existe o la clave es incorrecta, se crea una nueva cuenta automáticamente.

Dentro de la sesión de mozo el menú tiene estas opciones:

1. `Ver menú`
   - Muestra los productos disponibles agrupados por categoría.

2. `Crear pedido`
   - El mozo selecciona productos del menú uno por uno.
   - Para cada producto se pregunta si desea agregar un extra.
   - Si elige agregar un extra, ingresa nombre y precio del extra.
   - Para terminar el pedido, escribe `listo` cuando se solicita el nombre del producto.
   - Al finalizar, el pedido se registra y se imprime el ticket con:
     - descripción de cada artículo
     - subtotal
     - propina (10%)
     - total final

3. `Ver total del día`
   - Muestra el total acumulado de todos los pedidos registrados por ese mozo.

4. `Cerrar sesión`
   - Vuelve al menú principal.

3) Administración (Gerente)
Esta opción requiere la clave fija `admin`.

Dentro del menú de administración:

1. `Agregar producto`
   - Ingresa nombre, precio y categoría (`bebida`, `salado` o `dulce`).
   - El producto se agrega al menú si no existe.

2. `Modificar precio`
   - Ingresa el nombre del producto existente y su nuevo precio.
   - Actualiza el precio en el menú.

3. `Ver menú`
   - Muestra el menú actual con todos los productos.

4. `Volver`
   - Regresa al menú principal.

4) Cierre del día
- Muestra el total vendido por cada mozo y el total general del día.
- Se usa para cerrar la jornada y verificar ganancias.

5) Menú inicial del simulador
Cuando arranca el programa, se carga un menú inicial con estos productos:

- `Café` - bebida
- `Té` - bebida
- `Sándwich de jamón` - salado
- `Medialunas` - dulce
- `Pastel de chocolate` - dulce

6) Consejo para uso
- Usa `Ver menú` antes de crear pedidos para comprobar los productos disponibles.
- Escribe `listo` para terminar la selección de productos en un pedido.
- Si necesitas cambiar precios o agregar nuevos productos, entra como gerente con clave `admin`.

7) Ejemplo de flujo rápido
1. Ejecutar el programa:

```powershell
python "Simulador de Pedidos de Cafeteria.py"
```

2. Seleccionar `1. Sesión de mozo`.
3. Ingresar nombre y clave.
4. Elegir `2. Crear pedido`.
5. Seleccionar productos y extras.
6. Escribir `listo` para finalizar el pedido.
7. Ver el ticket generado en consola.

8) Errores comunes
- `Producto no encontrado.`: escribir exactamente el nombre del producto mostrado en el menú.
- `El precio debe ser positivo.`: ingresar un número mayor a 0 al cargar o modificar precios.
- `Acceso denegado.` en administración: usar la clave `admin`.
