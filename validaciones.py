def mostrar_menu():
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por tipo de arreglo")
        print("2. Búsqueda de arreglos por rango de precio")
        print("3. Actualizar precio de arreglo")
        print("4. Agregar arreglo")
        print("5. Eliminar arreglo")
        print("6. Salir")
        print(" =====================================")

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

