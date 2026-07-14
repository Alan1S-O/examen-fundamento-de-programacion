import validaciones
def leer_opcion():
  try:
    opcion = int(input("Ingrese opción: "))
    if 1 <= opcion <= 6:
      return opcion
    else:
      return -1
  except ValueError:
    return -1
def buscar_codigo(codigo, dicc_bodega):
  return codigo.upper() in dicc_bodega
def unidades_tipo(tipo, dicc_arreglos, dicc_bodega):
  total_unidades = 0
  tipo_buscado = tipo.lower().strip()
  for cod, datos in dicc_arreglos.items():
    if datos[1].lower() == tipo_buscado:
      if cod in dicc_bodega:
        total_unidades += dicc_bodega[cod][1]
  print(f"El total de unidades disponibles es: {total_unidades}")
def busqueda_precio(p_min, p_max, dicc_arreglos, dicc_bodega):
  resultados = []
  for cod, datos_bodega in dicc_bodega.items():
    precio = datos_bodega[0]
    unidades = datos_bodega[1]
    if p_min <= precio <= p_max and unidades > 0:
      nombre = dicc_arreglos[cod][0]
      resultados.append(f"{nombre}--{cod}")
  if resultados:
    resultados.sort()
    print(f"Los arreglos encontrados son: {resultados}")
  else:
    print("No hay arreglos en ese rango de precios.")
def actualizar_precio(codigo, nuevo_precio, dicc_bodega):
  cod_upper = codigo.upper()
  if buscar_codigo(cod_upper, dicc_bodega):
    dicc_bodega[cod_upper][0] = nuevo_precio
    return True
  return False
def agregar_arreglo(codigo, nombre, tipo, color, tamano, tarjeta_bool, temporada, precio, unidades, dicc_arreglos, dicc_bodega):
  cod_upper = codigo.upper()
  if buscar_codigo(cod_upper, dicc_bodega):
    return False
  dicc_arreglos[cod_upper] = [nombre, tipo, color, tamano, tarjeta_bool, temporada]
  dicc_bodega[cod_upper] = [precio, unidades]
  return True
def eliminar_arreglo(codigo, dicc_arreglos, dicc_bodega):
  cod_upper = codigo.upper()
  if buscar_codigo(cod_upper, dicc_bodega):
    del dicc_arreglos[cod_upper]
    del dicc_bodega[cod_upper]
    return True
  return False
def main():
  arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno']
  }
  bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6]
  }

  ejecutando = True
  while ejecutando:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")
    opcion = leer_opcion()
    if opcion == 1:
      tipo = input("Ingrese tipo de arreglo a consultar: ")
      unidades_tipo(tipo, arreglos, bodega)
    elif opcion == 2:
      while True:
        try:
          p_min = int(input("Ingrese precio mínimo: "))
          p_max = int(input("Ingrese precio máximo: "))
          if p_min >= 0 and p_max >= 0 and p_min <= p_max:
            break
          else:
            print("Restricción: Los valores deben ser mayores a cero y el mínimo menor o igual al máximo.")
        except ValueError:
          print("Debe ingresar valores enteros")
      busqueda_precio(p_min, p_max, arreglos, bodega)
    elif opcion == 3:
      continuar = 's'
      while continuar == 's':
        cod = input("Ingrese código del arreglo: ")
        precio_str = input("Ingrese nuevo precio: ")
        if validaciones.validar_precio(precio_str):
          nuevo_precio = int(precio_str)
          if actualizar_precio(cod, nuevo_precio, bodega):
            print("Precio actualizado")
          else:
            print("El código no existe")
        else:
          print("Precio inválido. Debe ser un entero positivo.")
        continuar = input("¿Desea actualizar otro precio (s/n)?: ").lower().strip()

        
    elif opcion == 4:
      cod = input("Ingrese código del arreglo: ")
      nom = input("Ingrese nombre: ")
      tip = input("Ingrese tipo: ")
      col = input("Ingrese color principal: ")
      tam = input("Ingrese tamaño (S/M/L): ")
      tarj = input("¿Incluye tarjeta? (s/n): ").lower().strip()
      temp = input("Ingrese temporada: ")
      pre_str = input("Ingrese precio: ")
      uni_str = input("Ingrese unidades: ")
      es_valido = True
      if not validaciones.validar_codigo_vacio(cod):
        print("Error: El código no puede estar vacío.")
        es_valido = False
      elif buscar_codigo(cod, bodega):
        print("El código ya existe")
        es_valido = False
      elif not validaciones.validar_nombre(nom):
        print("Error: El nombre no puede estar vacío.")
        es_valido = False
      elif not validaciones.validar_tipo(tip):
        print("Error: El tipo no puede estar vacío.")
        es_valido = False
      elif not validaciones.validar_color(col):
        print("Error: El color principal no puede estar vacío.")
        es_valido = False
      elif not validaciones.validar_tamano(tam):
        print("Error: El tamaño debe ser 'S', 'M' o 'L'.")
        es_valido = False
      elif not validaciones.validar_tarjeta(tarj):
        print("Error: La tarjeta debe responderse con 's' o 'n'.")
        es_valido = False
      elif not validaciones.validar_temporada(temp):
        print("Error: La temporada no puede estar vacía.")
        es_valido = False
      elif not validaciones.validar_precio(pre_str):
        print("Error: El precio debe ser un número entero mayor que cero.")
        es_valido = False
      elif not validaciones.validar_unidades(uni_str):
        print("Error: Las unidades deben ser un número entero mayor o igual a cero.")
        es_valido = False
      if es_valido:
        tarjeta_bool = True if tarj == 's' else False
        precio = int(pre_str)
        unidades = int(uni_str)
        if agregar_arreglo(cod, nom, tip, col, tam, tarjeta_bool, temp, precio, unidades, arreglos, bodega):
          print("Arreglo agregado")
        else:
          print("El código ya existe")
    elif opcion == 5:
      cod = input("Ingrese código del arreglo a eliminar: ")
      if eliminar_arreglo(cod, arreglos, bodega):
        print("Arreglo eliminado")
      else:
        print("El código no existe")
    elif opcion == 6:
      print("Programa finalizado.")
      ejecutando = False
    else:
      print("Debe seleccionar una opción válida")
if __name__ == "__main__":
  main()
    
    
    

