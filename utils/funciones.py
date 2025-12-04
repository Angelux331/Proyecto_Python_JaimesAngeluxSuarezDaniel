import os
from utils.jsonFileHandler import *
from datetime import datetime


def limpieza():
  """
  Limpia la consola según el sistema operativo.

  - En Windows usa el comando 'cls'.
  - En sistemas tipo Unix (Linux/macOS) usa el comando 'clear'.
  """
  os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
  """
  Pausa la ejecución hasta que el usuario presione Enter.

  Se usa para que el usuario pueda leer la información mostrada
  antes de continuar con la siguiente pantalla.
  """
  input("Presione Enter para continuar...")


def validarcategoria(archivogastos, categoria):
  """
  Verifica que una categoría exista en el archivo de gastos.

  Parámetros:
    archivogastos (str): Ruta al archivo JSON de gastos.
    categoria (str): Nombre de la categoría a validar.

  Retorna:
    bool: True si la categoría existe, False en caso contrario.

  Si la categoría no existe, muestra un mensaje, pausa la ejecución
  y devuelve False para que el llamador pueda volver a pedir un valor.
  """
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  if categoria not in categorias:
    print("La categoría ingresada no existe. Por favor, intente de nuevo.")
    pausar()
    return False
  return True


def AgregarGasto(gasto, archivogastos, categoria):
  """
  Agrega un nuevo gasto en una categoría específica del archivo JSON.

  Parámetros:
    gasto (dict): Datos del gasto con claves 'monto', 'fecha' y 'descripcion'.
    archivogastos (str): Ruta al archivo JSON de gastos.
    categoria (str): Categoría donde se almacenará el gasto.

  El gasto se añade a la lista de la categoría y luego se guarda el JSON.
  """
  data = read_json(archivogastos)
  data["Gastos"]["Categoria"][categoria].append(gasto)
  write_json(archivogastos, data)


def mostrarcategorias(archivosgastos):
  """
  Muestra en pantalla todas las categorías registradas en el archivo de gastos.

  Limpia la pantalla, imprime un encabezado y lista cada categoría en una línea.
  """
  limpieza()
  print("== Categorias ==\n")
  data = read_json(archivosgastos)
  categorias = data["Gastos"]["Categoria"].keys()
  for categoria in categorias:
    print(f"- {categoria}")


def ingresarfecha():
  """
  Solicita al usuario una fecha en formato YYYY-MM-DD y valida su formato.

  Retorna:
    str: Fecha válida ingresada por el usuario.

  Si el formato es incorrecto, muestra un mensaje y vuelve a pedir la fecha.
  """
  while True:
    fecha = input("Ingrese la fecha YYYYMMDD: ").strip()
    try:
      datetime.strptime(fecha, "%Y-%m-%d")
      return fecha
    except ValueError:
      print("Fecha inválida. Usa el formato YYYY-MM-DD. Ejemplo: 2025-12-02")


def vetodoslosgastos(archivogastos):
  """
  Muestra todos los gastos registrados en todas las categorías.

  - Verifica primero si existen gastos.
  - Imprime cada gasto con un formato de tabla: descripción, monto y fecha.
  - Si no hay gastos, informa al usuario y pausa.
  """
  limpieza()
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  validar = 0
  for categoria in categorias:
    validar += len(data["Gastos"]["Categoria"][categoria])
  if validar == 0:
    print("No hay gastos registrados.")
    pausar()
    return
  print("== Todos los Gastos ==\n")
  for categoria in categorias:
    print(f"--- {categoria} ---")
    gastos = data["Gastos"]["Categoria"][categoria]
    for gasto in gastos:
      print(f"┏{'━' * 42}┳{'━' * 15}┳{'━' * 14}┓")
      print(f"┃ {gasto['descripcion']:<40} ┃ ${gasto['monto']:>12,.2f} ┃ {gasto['fecha']:^12} ┃")
      print(f"┗{'━' * 42}┻{'━' * 15}┻{'━' * 14}┛")
    print("\n")
  pausar()
  

def vergastosporcategoria(archivogastos, categoria):
  """
  Muestra todos los gastos correspondientes a una categoría específica.

  Parámetros:
    archivogastos (str): Ruta al archivo JSON de gastos.
    categoria (str): Nombre de la categoría a consultar.

  Si la categoría no tiene gastos, muestra un mensaje informativo.
  """
  limpieza()
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  print(f'== Gastos en {categoria} ==\n')
  for cat in categorias:
    if cat == categoria:
      gastos = data["Gastos"]["Categoria"][cat]
      if len(gastos) == 0:
        print("No hay gastos registrados en esta categoría.")
        pausar()
        return
      for gasto in gastos:
        print(f"┏{'━' * 42}┳{'━' * 15}┳{'━' * 14}┓")
        print(f"┃ {gasto['descripcion']:<40} ┃ ${gasto['monto']:>12,.2f} ┃ {gasto['fecha']:^12} ┃")
        print(f"┗{'━' * 42}┻{'━' * 15}┻{'━' * 14}┛")
      print("\n")
  pausar()


def calculostotales(archivogastos):
  """
  Calcula y muestra el total de gastos por categoría y el total general.

  - Recorre todas las categorías.
  - Suma los montos de cada una.
  - Imprime una tabla con el total por categoría y el total global.
  """
  limpieza()
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  total_general = 0
  print("== Total de Gastos ==\n")
  for categoria in categorias:
    gastos = data["Gastos"]["Categoria"][categoria]
    total_categoria = sum(gasto["monto"] for gasto in gastos)
    total_general += total_categoria
    print(f"┏{'━' * 42}┳{'━' * 14}┓")
    print(f"┃ {categoria:<40} ┃ {total_categoria:<12,.2f} ┃")
    print(f"┗{'━' * 42}┻{'━' * 14}┛")
  print(f"\n┏{'━' * 42}┳{'━' * 14}┓")
  print(f"┃ {'Total General de Gastos:':<40} ┃ {total_general:<12,.2f} ┃")
  print(f"┗{'━' * 42}┻{'━' * 14}┛\n")
  pausar()


def validarmonto():
  """
  Solicita y valida que el monto del gasto sea un número positivo.

  Retorna:
    float: Monto válido mayor que 0.

  Maneja entradas no numéricas y montos menores o iguales a cero,
  mostrando mensajes de error y repitiendo la solicitud.
  """
  while True:
    try:
      monto = input("Ingrese el monto del gasto: ").strip()
      monto = float(monto)
      if monto <= 0:
        print("El monto debe ser mayor a 0. Intente nuevamente.")
        continue
      return monto
    except ValueError:
      print("Ingrese un número válido.")


def ingresarfecha(mensaje="Ingrese la fecha (YYYY-MM-DD): "):
  """
  Solicita una fecha al usuario con un mensaje personalizado y valida el formato.

  Parámetros:
    mensaje (str): Texto a mostrar al pedir la fecha.

  Retorna:
    str: Fecha válida en formato YYYY-MM-DD.
  """
  while True:
    fecha = input(mensaje).strip()
    try:
      datetime.strptime(fecha, "%Y-%m-%d")
      return fecha
    except ValueError:
      print("Fecha inválida. Usa el formato YYYY-MM-DD. Ejemplo: 2025-12-03")


def filtrarporfechas(archivogastos):
  """
  Filtra y muestra los gastos que se encuentran dentro de un rango de fechas.

  Flujo:
    - Pide fecha de inicio y fin.
    - Valida que inicio <= fin.
    - Muestra los gastos por categoría dentro del intervalo.
    - Si no hay gastos en el rango, informa al usuario.
  """
  limpieza()
  print("== Filtrar Gastos por Rango de Fechas ==\n")
  fecha_inicio = ingresarfecha("Ingrese fecha de inicio (YYYY-MM-DD): ")
  fecha_fin = ingresarfecha("Ingrese fecha de fin (YYYY-MM-DD): ")
  
  if fecha_inicio > fecha_fin:
    print("La fecha de inicio no puede ser posterior a la fecha fin.")
    pausar()
    return
  
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  gastos_encontrados = False
  
  print(f"\n== Gastos entre {fecha_inicio} y {fecha_fin} ==\n")
  for categoria in categorias:
    gastos = data["Gastos"]["Categoria"][categoria]
    gastos_filtrados = [g for g in gastos if fecha_inicio <= g["fecha"] <= fecha_fin]
    
    if gastos_filtrados:
      gastos_encontrados = True
      print(f"--- {categoria} ---")
      for gasto in gastos_filtrados:
        print(f"┏{'━' * 42}┳{'━' * 15}┳{'━' * 14}┓")
        print(f"┃ {gasto['descripcion']:<40} ┃ ${gasto['monto']:>12,.2f} ┃ {gasto['fecha']:^12} ┃")
        print(f"┗{'━' * 42}┻{'━' * 15}┻{'━' * 14}┛")
  
  if not gastos_encontrados:
    print("No se encontraron gastos en ese rango de fechas.")
  pausar()


def calcularsemanal(archivogastos):
  """
  Calcula y muestra el total de gastos de los últimos 7 días.

  - Toma la fecha actual y resta 7 días.
  - Suma los gastos por categoría dentro de ese intervalo.
  - Imprime los subtotales por categoría y el total semanal.
  """
  limpieza()
  from datetime import datetime, timedelta
  
  print("== Total de Gastos de la Última Semana ==\n")
  hoy = datetime.now().date()
  hace_semana = hoy - timedelta(days=7)
  
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  total_semanal = 0
  
  for categoria in categorias:
    gastos = data["Gastos"]["Categoria"][categoria]
    total_cat = sum(
      g["monto"]
      for g in gastos
      if hace_semana <= datetime.strptime(g["fecha"], "%Y-%m-%d").date() <= hoy
    )
    if total_cat > 0:
      print(f"┏{'━' * 42}┳{'━' * 14}┓")
      print(f"┃ {categoria:<40} ┃ {total_cat:<12,.2f} ┃")
      print(f"┗{'━' * 42}┻{'━' * 14}┛")
      total_semanal += total_cat
  print(f"\n┏{'━' * 42}┳{'━' * 14}┓")
  print(f"┃ {'Total Semanal':<40} ┃ {total_semanal:<12,.2f} ┃")
  print(f"┗{'━' * 42}┻{'━' * 14}┛\n")
  pausar()


def calcularmensual(archivogastos):
  """
  Calcula y muestra el total de gastos del mes actual.

  - Usa el mes y año actuales.
  - Suma los gastos cuyas fechas pertenecen a ese mes.
  - Muestra subtotales por categoría y el total mensual.
  """
  limpieza()
  from datetime import datetime
  
  print("== Total de Gastos del Mes Actual ==\n")
  hoy = datetime.now()
  mes_actual = hoy.month
  anio_actual = hoy.year
  
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  total_mensual = 0
  
  for categoria in categorias:
    gastos = data["Gastos"]["Categoria"][categoria]
    total_cat = 0
    for g in gastos:
      fecha_gasto = datetime.strptime(g["fecha"], "%Y-%m-%d")
      if fecha_gasto.month == mes_actual and fecha_gasto.year == anio_actual:
        total_cat += g["monto"]
    
    if total_cat > 0:
      print(f"┏{'━' * 42}┳{'━' * 14}┓")
      print(f"┃ {categoria:<40} ┃ {total_cat:<12,.2f} ┃")
      print(f"┗{'━' * 42}┻{'━' * 14}┛")
      total_mensual += total_cat
  print(f"\n┏{'━' * 42}┳{'━' * 14}┓")
  print(f"┃ {'Total Mensual':<40} ┃ {total_mensual:<12,.2f} ┃")
  print(f"┗{'━' * 42}┻{'━' * 14}┛\n")
  pausar()


def calculahistorico(archivogastos):
  """
  Calcula el total histórico de todos los gastos registrados.

  Actualmente reutiliza la función 'calculostotales', que ya calcula
  los totales por categoría y el total general.
  """
  calculostotales(archivogastos)


def generarreporte(archivogastos, periodo):
  """
  Genera un reporte formateado de gastos según el período indicado.

  Parámetros:
    archivogastos (str): Ruta al archivo JSON de gastos.
    periodo (str): Tipo de reporte a generar. Valores soportados:
                   'diario', 'semanal', 'mensual', 'historico'.

  El reporte incluye:
    - Título y fecha/hora de generación.
    - Listado de gastos por categoría y período.
    - Subtotales por categoría.
    - Total general del reporte.
  """
  limpieza()
  from datetime import datetime, timedelta
  
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  
  hoy = datetime.now()
  
  if periodo == "diario":
    titulo = "REPORTE DIARIO"
    fecha_filtro = hoy.date()
    gastos_filtrados = {}
    for cat in categorias:
      gastos_filtrados[cat] = [
        g for g in data["Gastos"]["Categoria"][cat]
        if datetime.strptime(g["fecha"], "%Y-%m-%d").date() == fecha_filtro
      ]
  
  elif periodo == "semanal":
    titulo = "REPORTE SEMANAL (Últimos 7 días)"
    hace_semana = (hoy - timedelta(days=7)).date()
    gastos_filtrados = {}
    for cat in categorias:
      gastos_filtrados[cat] = [
        g for g in data["Gastos"]["Categoria"][cat]
        if hace_semana <= datetime.strptime(g["fecha"], "%Y-%m-%d").date() <= hoy.date()
      ]
  
  elif periodo == "mensual":
    titulo = "REPORTE MENSUAL (Mes actual)"
    gastos_filtrados = {}
    for cat in categorias:
      gastos_filtrados[cat] = [
        g for g in data["Gastos"]["Categoria"][cat]
        if datetime.strptime(g["fecha"], "%Y-%m-%d").month == hoy.month
        and datetime.strptime(g["fecha"], "%Y-%m-%d").year == hoy.year
      ]
  
  else:
    titulo = "REPORTE HISTÓRICO COMPLETO"
    gastos_filtrados = data["Gastos"]["Categoria"]
  
  print(f"{'='*50}")
  print(f"{titulo:^50}")
  print(f"{'='*50}\n")
  print(f"Fecha de generación: {hoy.strftime('%Y-%m-%d %H:%M')}\n")
  
  total_general = 0
  for categoria, gastos in gastos_filtrados.items():
    if gastos:
      print(f"\n--- {categoria} ---")
      subtotal = 0
      for gasto in gastos:
        print(f"┏{'━' * 42}┳{'━' * 15}┳{'━' * 14}┓")
        print(f"┃ {gasto['descripcion']:<40} ┃ ${gasto['monto']:>12,.2f} ┃ {gasto['fecha']:^12} ┃")
        print(f"┗{'━' * 42}┻{'━' * 15}┻{'━' * 14}┛")
        subtotal += gasto["monto"]
      print(f"┏{'━' * 42}┳{'━' * 15}┓")
      print(f"┃ {'Subtotal ' + categoria + ':':<40} ┃ ${subtotal:<12.2f} ┃")
      print(f"┗{'━' * 42}┻{'━' * 15}┛")
      total_general += subtotal
  
  print(f"\n{'='*50}")
  print(f"{'     TOTAL GENERAL:':<30} ${total_general:>10.2f}")
  print(f"{'='*50}\n")
  pausar()
