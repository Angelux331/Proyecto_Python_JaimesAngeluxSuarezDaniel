from utils.menu import *
from utils.funciones import *
from utils.menuscontenido import *
import time
from utils.jsonFileHandler import *

archivogastos = './data/gastos.json'
estructura = {
    "Gastos": {
        "Categoria": {
            "Transporte": [],
            "Comida": [],
            "Servicios": [],
            "Entretenimiento": [],
            "Salud": [],
            "Educacion": [],
            "Otros": []
        }
    }
}

initialize_json(archivogastos, estructura)
while True:
  choise = menu("Menu Principal: Gestor de Gastos", menuPrincipal.values())
  match choise:
    case 1:
      while True:
        limpieza()
        mostrarcategorias(archivogastos)
        categoria = input("Ingrese la categoría del gasto: ").capitalize()
        if validarcategoria(archivogastos, categoria):
          break
        else:
          continue

      print("== Agregar Gasto ==")
      gasto = {
        "monto": validarmonto(),
        "fecha": ingresarfecha(),
        "descripcion": input("Ingrese una descripción del gasto: ").capitalize()
      }
      AgregarGasto(gasto, archivogastos, categoria)
      print("\n¡Gasto agregado exitosamente!")
      pausar()
      
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
              if validarcategoria(archivogastos, categoria):
                vergastosporcategoria(archivogastos, categoria)
                break
              else:
                break
          case 3:
            filtrarporfechas(archivogastos)
          case 4:
            break

    case 3:
      while True:
        choise = menu("Menu Calcular Total de Gastos", menuCalcularTotalGastos.values())
        match choise:
          case 1:
            calculostotales(archivogastos)
          case 2:
            calcularsemanal(archivogastos)
          case 3:
            calcularmensual(archivogastos)
          case 4:
            calculahistorico(archivogastos)
          case 5:
            break

    case 4:
      while True:
        choise = menu("Menu Generar Reporte de Gastos", menuGenerarReporte.values())
        match choise:
          case 1:
            generarreporte(archivogastos, "diario")
          case 2:
            generarreporte(archivogastos, "semanal")
          case 3:
            generarreporte(archivogastos, "mensual")
          case 4:
            generarreporte(archivogastos, "historico")
          case 5:
            break
      
    case 5:
      print("Saliendo del programa...")
      time.sleep(1)
      break
