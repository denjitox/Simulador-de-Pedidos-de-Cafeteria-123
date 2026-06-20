# Simulador de Pedidos de Cafetería

Descripción
- Proyecto en Python que simula pedidos en una cafetería. Contiene la lógica principal en `Simulador de Pedidos de Cafeteria.py`.

Archivos importantes
- `Simulador de Pedidos de Cafeteria.py` — código principal.
- `diagram.mmd` — diagrama UML en formato Mermaid.

Requisitos
- Python 3.8 o superior.

Instrucciones básicas de ejecución
1. Abrir PowerShell en la carpeta del proyecto:

```powershell
Set-Location -Path "C:\Users\emiliano\.vscode\Nueva carpeta"
```

2. (Opcional) Crear y activar un entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

3. Ejecutar el simulador:

```powershell
python "Simulador de Pedidos de Cafeteria.py"
```

funcionamiento:
El mozo inicia sesión con su nombre y una clave simple, para trabajar en su propia sesión. Arma el
pedido de cada cliente eligiendo productos de un menú organizado por categorías (bebidas, salado,
dulce), cada uno con su precio. Puede agregar extras a ciertos productos (por ejemplo, leche o
crema al café), que suman al precio. El sistema calcula el total en vivo e incorpora automáticamente
una propina del 10%. Al finalizar el pedido, emite el ticket y la venta se suma al total del día.
El gerente administra el menú: incorpora productos, los organiza por categoría y modifica precios,
con validaciones para evitar incoherencias. También consulta el cierre del día, que consolida las
ventas de todos los mozos.

Actores
Mozo y Gerente.

Clases principales (5)
Producto (abstracta) y sus tipos · Extra (decorador) · Pedido · Mozo · Cafetería.

Conceptos de POO aplicados
■ Abstracción y herencia: jerarquía de productos del menú.
■ Encapsulamiento: precios y clave como atributos privados.
■ Polimorfismo: cada producto resuelve su precio y descripción.
■ Patrón de diseño: Decorator para los extras de los productos.
■ Relación entre objetos: agregación (la Cafetería agrupa Mozos; cada Mozo agrupa sus Pedidos).
