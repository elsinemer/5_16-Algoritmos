def buscar_calificacion(matriz, calificacion_buscada, estudiantes, materias):
    # Verificamos que la calificación esté en el rango permitido
    if calificacion_buscada < 1 or calificacion_buscada > 12:
        print("La calificación debe estar entre 1 y 12.")
        return None
    
    for i, fila in enumerate(matriz):
        for j, calificacion in enumerate(fila):
            if calificacion == calificacion_buscada:
                return (estudiantes[i], materias[j])  # Retornamos el nombre del estudiante y la materia
    return None  # Si no se encuentra la calificación

# Ejemplo de uso
# Matriz de calificaciones
matriz_calificaciones = [
    [8, 10, 12],  # Calificaciones de Juna
    [5, 6, 11],   # Calificaciones de Elsi
    [7, 3, 4],    # Calificaciones de Ana
]

# Lista de estudiantes y materias
estudiantes = ["Juna", "Elsi", "Ana"]
materias = ["Matemáticas", "Ciencias", "Historia"]

calificacion_buscada = 11
resultado = buscar_calificacion(matriz_calificaciones, calificacion_buscada, estudiantes, materias)

if resultado:
    estudiante, materia = resultado
    print(f"La calificación {calificacion_buscada} se encuentra en {estudiante} en la materia {materia}.")
else:
    print(f"La calificación {calificacion_buscada} no se encontró en la matriz.")
