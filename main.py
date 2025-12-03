from utils.menu import *
from utils.funciones import *
from utils.menuscontenido import *
import time

archivogastos = './data/gastos.json'

while True:
  choise = menu("Menu Principal: Gestor de Gastos", menuPrincipal.values())
  match choise:
    case 1:
      while True:
        limpieza()
        mostrarcategorias(archivogastos)
        categoria = input("Ingrese la categoría del gasto: ").capitalize()
        if validarcategoria(archivogastos, categoria) == True:
          break
        else:
          continue
      print("== Agregar Gasto ==")
      gasto = {
        "monto": float(input("Ingrese el monto del gasto: ")),
        "categoria": categoria,
        "fecha": ingresarfecha(),
        "descripcion": input("Ingrese una descripción del gasto: ").capitalize()
      }
      AgregarGasto(gasto, archivogastos, categoria)
      
    case 2:
      while True:
        choise = menu("Menu Listar Gastos", menuListarGastos.values())
        match choise:
          case 1:
            vetodoslosgastos(archivogastos)
          
          case 2:
            while True:
              mostrarcategorias(archivogastos)
              categoria = input("Ingrese la categoría a ver: ").capitalize()
              if validarcategoria (archivogastos, categoria) == True:
                vergastosporcategoria(archivogastos, categoria)
              else:
                continue
          case 3:
            pass

          case 4:
            break

    case 3:
      while True:
        choise = menu("Menu Calcular Total de Gastos", menuCalcularTotalGastos.values())
        match choise:
          case 1:
            pass
          
          case 2:
            pass

          case 3:
            pass

          case 4:
            break

    case 4:
      while True:
        choise = menu("Menu Generar Reporte de Gastos", menuGenerarReporte.values())
        match choise:
          case 1:
            pass
          
          case 2:
            pass

          case 3:
            pass

          case 4:
            break
      
    case 5:
      print("Saliendo del programa...")
      time.sleep(1)
      break
