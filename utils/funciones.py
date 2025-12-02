import os
from utils.jsonFileHandler import *

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

def AgregarGasto(gasto, archivogastos, categoria):
  data = read_json(archivogastos)
  data["Gastos"]["Categoria"][categoria].append(gasto)
  write_json(archivogastos, data)
