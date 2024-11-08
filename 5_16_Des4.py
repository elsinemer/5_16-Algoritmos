def ordenar_por_promedio(estudiantes):
    n = len(estudiantes)
    
    # Algoritmo de selección
    for i in range(n):
        # Suponemos que el primer elemento no ordenado tiene el promedio más alto
        max_index = i
        for j in range(i + 1, n):
            if estudiantes[j][1] > estudiantes[max_index][1]:
                max_index = j
                
        # Intercambiamos el estudiante con el promedio más alto encontrado
        # en la porción no ordenada con el primer elemento no ordenado
        estudiantes[i], estudiantes[max_index] = estudiantes[max_index], estudiantes[i]
    
    return estudiantes

# Ejemplo de uso
# Lista de estudiantes y sus promedios (nombre, promedio)
lista_estudiantes = [
    ("Ana", 88),
    ("Elsi", 92),
    ("Juna", 75),
    ("Carlos", 85)
]

# Ordenamos la lista
lista_ordenada = ordenar_por_promedio(lista_estudiantes)

# Mostramos la lista ordenada
print("Estudiantes ordenados por promedio (de mayor a menor):")
for estudiante, promedio in lista_ordenada:
    print(f"{estudiante}: {promedio}")
