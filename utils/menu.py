from utils.funciones import *

def menu(title, options):
  """
  Muestra un menú en consola con un título y una lista de opciones, y devuelve
  la opción elegida por el usuario como un entero.

  Parámetros:
    title (str): Título que se mostrará en la cabecera del menú.
    options (iterable): Colección de textos de las opciones que se listarán.

  Retorna:
    int: Número de opción seleccionada por el usuario, entre 1 y len(options).

  Comportamiento:
    - Limpia la pantalla antes de mostrar el menú.
    - Numera automáticamente cada elemento de 'options' empezando en 1.
    - Solicita al usuario que ingrese una opción.
    - Valida que la entrada sea un número entero dentro del rango válido.
    - Repite la solicitud hasta que el usuario ingrese una opción correcta.
  """
  limpieza()        # Limpia la consola antes de mostrar el menú
  choise = 0        # Variable donde se almacenará la opción elegida
  index = 1         # Índice inicial para numerar las opciones

  # Sección visual de cabecera del menú
  print("===========================================")
  print(f"== {title} ==")   # Muestra el título del menú centrado entre separadores
  print("===========================================")
  print("==")

  # Listado numerado de las opciones recibidas
  for item in options:
    print(f"{index}. {item}")
    index += 1

  # Bucle de validación de entrada del usuario
  while True:
    try:
      choise = int(input("--> "))  # Pide la opción al usuario
      # Verifica que la opción esté dentro del rango válido
      if choise not in range(1, len(options) + 1):
        print("--> Opción inválida...")
      else:
        break   # Sale del bucle si la opción es correcta
    except ValueError:
      # Maneja el caso en que el usuario no ingrese un número entero
      print("Su elección debe ser un número...")
  
  # Devuelve la opción elegida para que el llamador la procese
  return choise
