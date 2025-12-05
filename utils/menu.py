from utils.funciones import *

def menu(title, options):
  choise = 0
  index = 1
  limpieza()
  print("━" * 50)
  print(f"━━ {title:^44} ━━")
  print("━" * 50)
  print("━━")
  for item in options:
    print(f"{index}. {item}")
    index += 1
    
  while True:
    try:
      choise = int(validacioninput("--> "))
      if choise not in range(1, len(options) + 1):
        print("--> Opción inválida...")
      else:
        break
    except ValueError:
      print("Su elección debe ser un número...")

  return choise
