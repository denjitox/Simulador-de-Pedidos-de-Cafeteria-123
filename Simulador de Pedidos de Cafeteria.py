"""Simulador de pedidos de cafetería para TPI.

Este script implementa:
- productos con categorías (bebidas, salados y dulces)
- extras decoradores para cada producto
- pedidos con cálculo de subtotal, propina y total
- registro de mozos y total del día
- administración de menú por gerente
- cierre diario con totales por mozo y total general
"""

from abc import ABC, abstractmethod
import hashlib


class Producto(ABC):
    """Clase base abstracta para un producto del menú."""

    def __init__(self, nombre: str, precio: float, categoria: str):
        self.nombre = nombre
        self._precio = precio
        self.categoria = categoria

    @property
    def precio(self) -> float:
        return self._precio

    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass


class Bebida(Producto):
    def obtener_descripcion(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"


class ProductoSalado(Producto):
    def obtener_descripcion(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"


class ProductoDulce(Producto):
    def obtener_descripcion(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"


class Extra(Producto):
    """Patrón decorador para agregar extras a productos."""

    def __init__(self, producto: Producto, nombre_extra: str, precio_extra: float):
        self.producto = producto
        self.nombre_extra = nombre_extra
        self.precio_extra = precio_extra
        super().__init__(
            nombre=f"{producto.nombre} + {nombre_extra}",
            precio=producto.precio + precio_extra,
            categoria=producto.categoria,
        )

    @property
    def precio(self) -> float:
        return self.producto.precio + self.precio_extra

    def obtener_descripcion(self) -> str:
        return f"{self.producto.obtener_descripcion()} + {self.nombre_extra} (${self.precio_extra:.2f})"


class Pedido:
    """Representa un pedido de la cafetería."""

    def __init__(self, numero_pedido: int):
        self.numero_pedido = numero_pedido
        self.items = []

    def agregar_item(self, item: Producto) -> None:
        self.items.append(item)

    def calcular_subtotal(self) -> float:
        return sum(item.precio for item in self.items)

    def calcular_propina(self) -> float:
        return self.calcular_subtotal() * 0.10

    def calcular_total(self) -> float:
        return self.calcular_subtotal() + self.calcular_propina()

    def emitir_ticket(self) -> str:
        ticket = [f"\n--- TICKET Pedido #{self.numero_pedido} ---"]
        for item in self.items:
            ticket.append(f"  {item.obtener_descripcion()}")
        ticket.append(f"Subtotal: ${self.calcular_subtotal():.2f}")
        ticket.append(f"Propina (10%): ${self.calcular_propina():.2f}")
        ticket.append(f"TOTAL: ${self.calcular_total():.2f}")
        ticket.append("----------------------------")
        return "\n".join(ticket)


class Mozo:
    """Registro y operaciones de un mozo."""

    def __init__(self, nombre: str, clave: str):
        self.nombre = nombre
        self.__clave = hashlib.sha256(clave.encode()).hexdigest()
        self.pedidos = []
        self.numero_pedido_actual = 1
        self.total_dia = 0.0

    def verificar_clave(self, clave: str) -> bool:
        return self.__clave == hashlib.sha256(clave.encode()).hexdigest()

    def crear_pedido(self) -> Pedido:
        pedido = Pedido(self.numero_pedido_actual)
        self.numero_pedido_actual += 1
        return pedido

    def registrar_pedido(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)
        self.total_dia += pedido.calcular_total()
        print(pedido.emitir_ticket())

    def obtener_total_dia(self) -> float:
        return self.total_dia


class Gerente:
    """Rol simple de gerente con clave fija."""

    CLAVE_ADMIN = "admin"

    @classmethod
    def verificar_clave(cls, clave: str) -> bool:
        return clave == cls.CLAVE_ADMIN


class Cafeteria:
    """Gestión de menú y mozos de la cafetería."""

    def __init__(self):
        self.mozos = {}
        self.menu = {}

    def registrar_mozo(self, nombre: str, clave: str) -> Mozo:
        if nombre in self.mozos:
            print(f"El mozo '{nombre}' ya existe. Se reutiliza la sesión.")
            return self.mozos[nombre]
        mozo = Mozo(nombre, clave)
        self.mozos[nombre] = mozo
        print(f"Mozo '{nombre}' registrado exitosamente.")
        return mozo

    def autenticar_mozo(self, nombre: str, clave: str) -> Mozo | None:
        if nombre in self.mozos and self.mozos[nombre].verificar_clave(clave):
            print(f"¡Bienvenido {nombre}!")
            return self.mozos[nombre]
        print("Usuario o contraseña incorrectos.")
        return None

    def agregar_producto(self, nombre: str, precio: float, categoria: str) -> None:
        if precio <= 0:
            print("Error: el precio debe ser positivo.")
            return
        if nombre in self.menu:
            print(f"El producto '{nombre}' ya existe en el menú.")
            return

        producto = None
        categoria = categoria.lower()
        if categoria == "bebida":
            producto = Bebida(nombre, precio, categoria)
        elif categoria == "salado":
            producto = ProductoSalado(nombre, precio, categoria)
        elif categoria == "dulce":
            producto = ProductoDulce(nombre, precio, categoria)
        else:
            print("Categoría no válida. Use 'bebida', 'salado' o 'dulce'.")
            return

        self.menu[nombre] = producto
        print(f"Producto '{nombre}' agregado al menú.")

    def modificar_precio(self, nombre: str, nuevo_precio: float) -> None:
        if nombre not in self.menu:
            print(f"Producto '{nombre}' no encontrado.")
            return
        if nuevo_precio <= 0:
            print("Error: el precio debe ser positivo.")
            return
        self.menu[nombre]._precio = nuevo_precio
        print(f"Precio de '{nombre}' actualizado a ${nuevo_precio:.2f}")

    def mostrar_menu(self) -> None:
        if not self.menu:
            print("El menú está vacío.")
            return

        print("\n=== MENÚ ===")
        categorias = {"bebida": "Bebidas", "salado": "Salado", "dulce": "Dulce"}
        for cat_key, cat_nombre in categorias.items():
            print(f"\n{cat_nombre}:")
            encontrados = False
            for producto in self.menu.values():
                if producto.categoria == cat_key:
                    print(f"  • {producto.obtener_descripcion()}")
                    encontrados = True
            if not encontrados:
                print("  (sin productos)")

    def cierre_dia(self) -> None:
        print("\n=== CIERRE DEL DÍA ===")
        if not self.mozos:
            print("No hay mozos registrados.")
            return

        total_general = 0.0
        for nombre, mozo in self.mozos.items():
            total_mozo = mozo.obtener_total_dia()
            print(f"Mozo {nombre}: ${total_mozo:.2f}")
            total_general += total_mozo
        print(f"TOTAL GENERAL DEL DÍA: ${total_general:.2f}")


def leer_precio(mensaje: str) -> float:
    while True:
        valor = input(mensaje).strip()
        try:
            precio = float(valor)
            if precio <= 0:
                print("Debe ingresar un valor numérico positivo.")
                continue
            return precio
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")


def seleccionar_producto(cafeteria: Cafeteria) -> Producto | None:
    nombre = input("Ingrese nombre del producto (o 'listo' para finalizar): ").strip()
    if nombre.lower() == "listo":
        return None
    producto = cafeteria.menu.get(nombre)
    if producto is None:
        print("Producto no encontrado.")
        return seleccionar_producto(cafeteria)
    return producto


def iniciar_sesion_mozo(cafeteria: Cafeteria) -> Mozo:
    nombre = input("Ingrese su nombre: ").strip()
    clave = input("Ingrese su clave: ").strip()
    mozo = cafeteria.autenticar_mozo(nombre, clave)
    if mozo:
        return mozo
    print("Creando nueva cuenta de mozo...")
    return cafeteria.registrar_mozo(nombre, clave)


def manejar_sesion_mozo(cafeteria: Cafeteria, mozo: Mozo) -> None:
    while True:
        print(f"\n--- Sesión de {mozo.nombre} ---")
        print("1. Ver menú")
        print("2. Crear pedido")
        print("3. Ver total del día")
        print("4. Cerrar sesión")
        opcion = input("Seleccione: ").strip()

        if opcion == "1":
            cafeteria.mostrar_menu()
        elif opcion == "2":
            pedido = mozo.crear_pedido()
            if not cafeteria.menu:
                print("El menú está vacío. No se puede crear un pedido.")
                continue

            while True:
                cafeteria.mostrar_menu()
                producto = seleccionar_producto(cafeteria)
                if producto is None:
                    if pedido.items:
                        mozo.registrar_pedido(pedido)
                    else:
                        print("El pedido está vacío.")
                    break

                agregar_extra = input("¿Agregar extra? (s/n): ").strip().lower()
                if agregar_extra == "s":
                    nombre_extra = input("Nombre del extra: ").strip()
                    precio_extra = leer_precio("Precio del extra: ")
                    producto = Extra(producto, nombre_extra, precio_extra)

                pedido.agregar_item(producto)
                print(f"'{producto.nombre}' agregado al pedido.")
        elif opcion == "3":
            print(f"Total del día: ${mozo.obtener_total_dia():.2f}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def manejar_administracion(cafeteria: Cafeteria) -> None:
    clave_gerente = input("Ingrese clave de gerente: ").strip()
    if not Gerente.verificar_clave(clave_gerente):
        print("Acceso denegado.")
        return

    while True:
        print("\n--- ADMINISTRACIÓN ---")
        print("1. Agregar producto")
        print("2. Modificar precio")
        print("3. Ver menú")
        print("4. Volver")
        opcion = input("Seleccione: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            precio = leer_precio("Precio: ")
            categoria = input("Categoría (bebida/salado/dulce): ").strip()
            cafeteria.agregar_producto(nombre, precio, categoria)
        elif opcion == "2":
            nombre = input("Nombre del producto: ").strip()
            nuevo_precio = leer_precio("Nuevo precio: ")
            cafeteria.modificar_precio(nombre, nuevo_precio)
        elif opcion == "3":
            cafeteria.mostrar_menu()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def preparar_menu_inicial(cafeteria: Cafeteria) -> None:
    cafeteria.agregar_producto("Café", 2.50, "bebida")
    cafeteria.agregar_producto("Té", 2.00, "bebida")
    cafeteria.agregar_producto("Sándwich de jamón", 5.00, "salado")
    cafeteria.agregar_producto("Medialunas", 1.50, "dulce")
    cafeteria.agregar_producto("Pastel de chocolate", 3.50, "dulce")


def main() -> None:
    cafeteria = Cafeteria()
    preparar_menu_inicial(cafeteria)

    while True:
        print("\n--- SISTEMA DE CAFETERÍA ---")
        print("1. Sesión de mozo")
        print("2. Administración (Gerente)")
        print("3. Cierre del día")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mozo = iniciar_sesion_mozo(cafeteria)
            manejar_sesion_mozo(cafeteria, mozo)
        elif opcion == "2":
            manejar_administracion(cafeteria)
        elif opcion == "3":
            cafeteria.cierre_dia()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
