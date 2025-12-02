from utils.menu import *
from utils.funciones import *
from utils.menuscontenido import *
import time

while True:
  choise = menu("Menu Principal: Gestor de Gastos", menuPrincipal.values())
  match choise:
    case 1:
      pass

    case 2:
      while True:
        choise = menu("Menu Listar Gastos", menuListarGastos.values())
        match choise:
          case 1:
            pass
          
          case 2:
            pass

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