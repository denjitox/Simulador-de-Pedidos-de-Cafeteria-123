# Instructivo de funcionamiento detallado

Este documento explica cómo ejecutar y entender el `Simulador de Pedidos de Cafeteria.py`.

1) Requisitos
- Python 3.8 o superior.
- (Opcional) Entorno virtual recomendado.

2) Preparación del entorno
- Abrir PowerShell en la carpeta del proyecto:

```powershell
Set-Location -Path "C:\Users\emiliano\.vscode\Nueva carpeta"
```

- Crear y activar entorno virtual (opcional):

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

3) Dependencias
- Si el proyecto requiere paquetes externos, crea un archivo `requirements.txt` con las dependencias y ejecuta:

```powershell
pip install -r requirements.txt
```

4) Estructura y puntos clave del script
- Archivo principal: `Simulador de Pedidos de Cafeteria.py`.
- Punto de entrada: ejecutar el archivo en Python.
- Flujo general esperado:
  - Inicialización de la cafetería y menú.
  - Creación de clientes y pedidos.
  - Procesamiento de pedidos (cálculo de totales, tiempos simulados, etc.).

5) Ejecución
- Para ejecutar el simulador desde PowerShell:

```powershell
python "Simulador de Pedidos de Cafeteria.py"
```

- Si el script acepta argumentos (por ejemplo, número de clientes o modo simulación), se pueden pasar así:

```powershell
python "Simulador de Pedidos de Cafeteria.py" --clientes 10 --modo rapido
```

6) Parámetros comunes (ejemplos sugeridos)
- `--clientes N`: número de clientes a simular.
- `--semilla S`: semilla para el generador aleatorio para reproducibilidad.
- `--salida archivo.txt`: guardar resultados en un archivo.

7) Salida esperada
- En consola: resumen de cada pedido, totales y tiempos.
- Archivo de salida (si se especifica): registro detallado por línea.

8) Ejemplos rápidos
- Ejecutar 5 clientes y guardar salida:

```powershell
python "Simulador de Pedidos de Cafeteria.py" --clientes 5 --salida resultados.txt
```

9) Depuración y mensajes comunes
- Si el script no arranca: verificar versión de Python y que el archivo exista en la carpeta actual.
- Errores de importación: crear/activar el entorno virtual e instalar dependencias.
- Problemas con permisos al escribir archivos: ejecutar PowerShell con permisos suficientes o cambiar la ruta de salida.

10) Cómo extender o integrar
- Añadir opciones CLI con `argparse` si aún no existen.
- Extraer la lógica principal a funciones para poder escribir tests unitarios.

11) Contacto
- Si quieres que adapte el instructivo a parámetros exactos del script (nombre de opciones reales, formatos de salida), dame el contenido de `Simulador de Pedidos de Cafeteria.py` o indica qué opciones quieres.
