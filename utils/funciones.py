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
  print("== Todos los Gastos ==\n")
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  for categoria in categorias:
    if len(data["Gastos"]["Categoria"][categoria]) == 0:
      continue
    print(f"--- {categoria} ---")
    gastos = data["Gastos"]["Categoria"][categoria]
    for gasto in gastos:
      print(f"Descripción: {gasto['descripcion']}, Monto: {gasto['monto']}, Fecha: {gasto['fecha']}")
    print("\n")
  pausar()
  

def vergastosporcategoria(archivogastos, categoria):
  limpieza()
  print(f'== Gastos en {categoria} ==\n')
  data = read_json(archivogastos)
  categorias = data["Gastos"]["Categoria"].keys()
  for cat in categorias:
    if cat == categoria:
      gastos = data["Gastos"]["Categoria"][cat]
      if len(gastos) == 0:
        print("No hay gastos registrados en esta categoría.")
        pausar()
        return
      for gasto in gastos:
        print(f"Descripción: {gasto['descripcion']}, Monto: {gasto['monto']}, Fecha: {gasto['fecha']}")
      print("\n")
  pausar()