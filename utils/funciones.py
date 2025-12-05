import os
from utils.jsonFileHandler import *
from datetime import datetime

def limpieza():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("Presione Enter para continuar...")

def validacioninput(coso):
    while True:
        try:
            return input(coso)
        except KeyboardInterrupt:
            print("\n[!] esta vez no")

def validarcategoria(archivogastos, categoria):
    data = read_json(archivogastos)
    categorias = data["Gastos"]["Categoria"].keys()
    if categoria not in categorias:
        print("La categoría ingresada no existe. Por favor, intente de nuevo.")
        pausar()
        return False
    return True

def AgregarGasto(gasto, archivogastos, categoria):
    data = read_json(archivogastos)
    data["Gastos"]["Categoria"][categoria].append(gasto)
    write_json(archivogastos, data)

def mostrarcategorias(archivosgastos):
    limpieza()
    titulo = "━━ Categorias ━━"
    print(f"{'━'*50}")
    print(f"{titulo:^50}")
    print(f"{'━'*50}\n")
    
    data = read_json(archivosgastos)
    categorias = data["Gastos"]["Categoria"].keys()
    for categoria in categorias:
        print(f"- {categoria}")

def ingresarfecha():
    while True:
        fecha = input("Ingrese la fecha YYYYMMDD: ").strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Fecha inválida. Usa el formato YYYY-MM-DD. Ejemplo: 2025-12-02")

def vetodoslosgastos(archivogastos):
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
    titulo = "== Todos los Gastos =="
    print(f"{'━'*50}")
    print(f"{titulo:^50}")
    print(f"{'━'*50}\n")
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
    limpieza()
    data = read_json(archivogastos)
    categorias = data["Gastos"]["Categoria"].keys()
    print(f'━━ Gastos en {categoria} ━━\n')
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
    limpieza()
    data = read_json(archivogastos)
    categorias = data["Gastos"]["Categoria"].keys()
    total_general = 0
    titulo = "━━ Total de Gastos ━━"
    print(f"{'━'*50}")
    print(f"{titulo:^50}")
    print(f"{'━'*50}\n")
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
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Fecha inválida. Usa el formato YYYY-MM-DD. Ejemplo: 2025-12-03")

def filtrarporfechas(archivogastos):
    limpieza()
    titulo = "━━ Filtrar Gastos por Rango de Fechas ━━"
    print(f"{'━'*50}")
    print(f"{titulo:^50}")
    print(f"{'━'*50}\n")
    
    fecha_inicio = ingresarfecha("Ingrese fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = ingresarfecha("Ingrese fecha de fin (YYYY-MM-DD): ")
  
    if fecha_inicio > fecha_fin:
        print("La fecha de inicio no puede ser posterior a la fecha fin.")
        pausar()
        return
  
    data = read_json(archivogastos)
    categorias = data["Gastos"]["Categoria"].keys()
    gastos_encontrados = False
  
    print(f"\n━━ Gastos entre {fecha_inicio} y {fecha_fin} ━━\n")
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
  limpieza()
  from datetime import datetime, timedelta
  
  print("━━ Total de Gastos de la Última Semana ━━\n")
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
  limpieza()
  from datetime import datetime
  
  print("━━ Total de Gastos del Mes Actual ━━\n")
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
  calculostotales(archivogastos)

def generarreporte(archivogastos, periodo):
    limpieza()
    from datetime import datetime, timedelta
    
    # Leer datos de gastos
    data = read_json(archivogastos)
    categorias = data["Gastos"]["Categoria"].keys()
    
    hoy = datetime.now()
    
    # Filtrar gastos según el período
    if periodo == "diario":
        titulo = "REPORTE DIARIO"
        fecha_filtro = hoy.date()
        gastos_filtrados = {
            cat: [g for g in data["Gastos"]["Categoria"][cat] 
                  if datetime.strptime(g["fecha"], "%Y-%m-%d").date() == fecha_filtro]
            for cat in categorias
        }
    elif periodo == "semanal":
        titulo = "REPORTE SEMANAL (Últimos 7 días)"
        hace_semana = (hoy - timedelta(days=7)).date()
        gastos_filtrados = {
            cat: [g for g in data["Gastos"]["Categoria"][cat] 
                  if hace_semana <= datetime.strptime(g["fecha"], "%Y-%m-%d").date() <= hoy.date()]
            for cat in categorias
        }
    elif periodo == "mensual":
        titulo = "REPORTE MENSUAL (Mes actual)"
        gastos_filtrados = {
            cat: [g for g in data["Gastos"]["Categoria"][cat] 
                  if datetime.strptime(g["fecha"], "%Y-%m-%d").month == hoy.month and
                     datetime.strptime(g["fecha"], "%Y-%m-%d").year == hoy.year]
            for cat in categorias
        }
    else:
        titulo = "REPORTE HISTÓRICO COMPLETO"
        gastos_filtrados = data["Gastos"]["Categoria"]

    # Mostrar reporte por pantalla
    print(f"{'━'*50}")
    print(f"{titulo:^50}")
    print(f"{'━'*50}\n")
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
    
    print(f"\n{'━'*50}")
    print(f"{'     TOTAL GENERAL:':<30} ${total_general:>10.2f}")
    print(f"{'━'*50}\n")
    
    # Guardar reporte en JSON
    reporte = {
        "titulo": titulo,
        "fecha_generacion": hoy.strftime('%Y-%m-%d %H:%M:%S'),
        "total_general": total_general,
        "gastos_por_categoria": gastos_filtrados
    }
    
    print('Desea guardar el reporte en un archivo JSON? (s/n)')
    guardar = input("--> ").strip().lower()
    if guardar == 's':  
      # Crear carpeta si no existe
      if not os.path.exists("reportes"):
          os.makedirs("reportes")
      
      # Nombre del archivo con fecha y hora
      nombre_archivo = f"reportes/reporte_{periodo}_{hoy.strftime('%Y%m%d_%H%M%S')}.json"
      write_json(nombre_archivo, reporte)
      
      print(f"[INFO] Reporte guardado en: {nombre_archivo}")
      pausar()
    else:
      print("Reporte no guardado.")
      pausar()
