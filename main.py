from utils.menu import *
from utils.funciones import *
from utils.menuscontenido import *
import time

# Ruta al archivo JSON donde se almacenan todos los gastos
archivogastos = './data/gastos.json'

# Bucle principal del programa: muestra el menú principal y deriva a los submenús
while True:
  # Muestra el menú principal y devuelve la opción elegida por el usuario
  choise = menu("Menu Principal: Gestor de Gastos", menuPrincipal.values())
  match choise:
    # =========================
    # OPCIÓN 1: AGREGAR GASTO
    # =========================
    case 1:
      # Selección y validación de categoría de gasto
      while True:
        limpieza()  # Limpia la pantalla o el contexto visual del programa
        mostrarcategorias(archivogastos)  # Muestra las categorías disponibles según el JSON
        categoria = input("Ingrese la categoría del gasto: ").capitalize()
        # Valida que la categoría exista en el archivo de gastos
        if validarcategoria(archivogastos, categoria) == True:
          break
        else:
          # Si no es válida, vuelve a pedir una categoría
          continue

      print("== Agregar Gasto ==")
      # Crea el diccionario con los datos del nuevo gasto
      gasto = {
        "monto": validarmonto(),              # Pide y valida el monto numérico
        "fecha": ingresarfecha(),             # Pide y valida la fecha del gasto
        "descripcion": input("Ingrese una descripción del gasto: ").capitalize()
      }
      # Agrega el gasto al archivo JSON dentro de la categoría seleccionada
      AgregarGasto(gasto, archivogastos, categoria)
      print("\n¡Gasto agregado exitosamente!")
      pausar()  # Espera una tecla o similar antes de continuar
      
    # =========================
    # OPCIÓN 2: LISTAR GASTOS
    # =========================
    case 2:
      while True:
        # Submenú para distintas formas de listar los gastos
        choise = menu("Menu Listar Gastos", menuListarGastos.values())
        match choise:
          # Ver todos los gastos registrados sin filtros
          case 1:
            vetodoslosgastos(archivogastos)
          
          # Ver gastos filtrados por una categoría específica
          case 2:
            while True:
              mostrarcategorias(archivogastos)
              categoria = input("Ingrese la categoría a ver: ").capitalize()
              if validarcategoria(archivogastos, categoria) == True:
                vergastosporcategoria(archivogastos, categoria)
                break
              else:
                # Si la categoría no es válida, vuelve al submenú
                break
                
          # Ver gastos filtrando por rango de fechas
          case 3:
            filtrarporfechas(archivogastos)
          
          # Volver al menú principal
          case 4:
            break

    # =======================================
    # OPCIÓN 3: CALCULAR TOTALES DE GASTOS
    # =======================================
    case 3:
      while True:
        # Submenú para distintos tipos de cálculos de totales
        choise = menu("Menu Calcular Total de Gastos", menuCalcularTotalGastos.values())
        match choise:
          # Cálculos generales (por categoría, globales, etc. según implementación)
          case 1:
            calculostotales(archivogastos)
          
          # Cálculo del total de gastos semanal
          case 2:
            calcularsemanal(archivogastos)

          # Cálculo del total de gastos mensual
          case 3:
            calcularmensual(archivogastos)

          # Cálculo histórico (por todo el período registrado)
          case 4:
            calculahistorico(archivogastos)

          # Volver al menú principal
          case 5:
            break

    # =======================================
    # OPCIÓN 4: GENERAR REPORTES DE GASTOS
    # =======================================
    case 4:
      while True:
        # Submenú para generar diferentes tipos de reportes
        choise = menu("Menu Generar Reporte de Gastos", menuGenerarReporte.values())
        match choise:
          # Reporte diario
          case 1:
            generarreporte(archivogastos, "diario")
          
          # Reporte semanal
          case 2:
            generarreporte(archivogastos, "semanal")

          # Reporte mensual
          case 3:
            generarreporte(archivogastos, "mensual")

          # Reporte histórico (todo el período)
          case 4:
            generarreporte(archivogastos, "historico")

          # Volver al menú principal
          case 5:
            break
      
    # =========================
    # OPCIÓN 5: SALIR
    # =========================
    case 5:
      print("Saliendo del programa...")
      time.sleep(1)  # Pequeña pausa antes de cerrar
      break
