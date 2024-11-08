def buscar_estudiante(lista_estudiantes, nombre_buscado):
    izquierda, derecha = 0, len(lista_estudiantes) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_estudiantes[medio] == nombre_buscado:
            return f"{nombre_buscado} se encuentra en la lista en la posición {medio}."
        elif lista_estudiantes[medio] < nombre_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return f"{nombre_buscado} no se encuentra en la lista."

# Ejemplo de uso
# Lista ordenada alfabéticamente
lista_estudiantes = ["Ana", "Elsi", "Juna"]

# Búsqueda de un estudiante específico
nombre_buscado = "Elsi"
resultado = buscar_estudiante(lista_estudiantes, nombre_buscado)
print(resultado)

# Ejemplo de estudiante que no está en la lista
nombre_buscado_no_encontrado = "Carlos"
resultado_no_encontrado = buscar_estudiante(lista_estudiantes, nombre_buscado_no_encontrado)
print(resultado_no_encontrado)
