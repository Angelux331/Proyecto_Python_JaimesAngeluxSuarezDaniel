import os
from utils.jsonFileHandler import *
import time
from datetime import datetime

def findDictionary(dataList, key, value):
  info = {}
  for i in range(len(dataList)):
    if dataList[i].get(key) == value:
      info["index"] = i
      info["data"] = dataList[i]
      break
  return info

def limpieza():
  os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
  input("Presione Enter para continuar...")

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
  print("== Categorias ==\n")
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
  limpieza()
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  total_general = 0
  print("== Total de Gastos ==\n")
  for categoria in categorias:
    gastos = data["Gastos"]["Categoria"][categoria]
    total_categoria = sum(gasto["monto"] for gasto in gastos)
    total_general += total_categoria
    print(f"{categoria}: {total_categoria}")
  print(f"\nTotal General de Gastos: {total_general}\n")
  pausar()

def calculossemanales(archivogastos):
  limpieza()
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  total_general = 0
  print("== Total de Gastos Semanales ==\n")
  for categoria in categorias:
    gastos = data["Gastos"]["Categoria"][categoria]
    total_categoria = sum(gasto["monto"] for gasto in gastos)
    total_general += total_categoria
    print(f"{categoria}: {total_categoria}")
  print(f"\nTotal General de Gastos Semanales: {total_general}\n")
  pausar()

def validarmonto():
    """Valida que el monto sea un número positivo"""
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
    """Función mejorada para validar fechas"""
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Fecha inválida. Usa el formato YYYY-MM-DD. Ejemplo: 2025-12-03")


def filtrarporfechas(archivogastos):
    """Filtra gastos por rango de fechas"""
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
    """Calcula el total de gastos de la última semana"""
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
        total_cat = sum(g["monto"] for g in gastos if hace_semana <= datetime.strptime(g["fecha"], "%Y-%m-%d").date() <= hoy)
        if total_cat > 0:
            print(f"{categoria}: {total_cat}")
            total_semanal += total_cat
    
    print(f"\nTotal Semanal: {total_semanal}\n")
    pausar()


def calcularmensual(archivogastos):
    """Calcula el total de gastos del mes actual"""
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
            print(f"{categoria}: {total_cat}")
            total_mensual += total_cat
    
    print(f"\nTotal Mensual: {total_mensual}\n")
    pausar()


def calculahistorico(archivogastos):
    """Calcula el total histórico de todos los gastos"""
    calculostotales(archivogastos)


def generarreporte(archivogastos, periodo):
    """Genera un reporte formateado según el periodo especificado"""
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
            gastos_filtrados[cat] = [g for g in data["Gastos"]["Categoria"][cat] 
                                     if datetime.strptime(g["fecha"], "%Y-%m-%d").date() == fecha_filtro]
    
    elif periodo == "semanal":
        titulo = "REPORTE SEMANAL (Últimos 7 días)"
        hace_semana = (hoy - timedelta(days=7)).date()
        gastos_filtrados = {}
        for cat in categorias:
            gastos_filtrados[cat] = [g for g in data["Gastos"]["Categoria"][cat]
                                     if hace_semana <= datetime.strptime(g["fecha"], "%Y-%m-%d").date() <= hoy.date()]
    
    elif periodo == "mensual":
        titulo = "REPORTE MENSUAL (Mes actual)"
        gastos_filtrados = {}
        for cat in categorias:
            gastos_filtrados[cat] = [g for g in data["Gastos"]["Categoria"][cat]
                                     if datetime.strptime(g["fecha"], "%Y-%m-%d").month == hoy.month 
                                     and datetime.strptime(g["fecha"], "%Y-%m-%d").year == hoy.year]
    
    else:  # histórico
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
