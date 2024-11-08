from collections import deque

# Definimos un nodo de árbol que representa un grado y sus estudiantes
class Grado:
    def __init__(self, nombre_grado, estudiantes=None):
        self.nombre_grado = nombre_grado  # Nombre del grado, como "Grado 12", "Grado 11", etc.
        self.estudiantes = estudiantes or []  # Lista de estudiantes en el grado
        self.hijos = []  # Lista de grados de menor nivel (ej., el siguiente grado)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

# Función para hacer el recorrido por niveles y mostrar los estudiantes
def recorrido_por_niveles(raiz):
    if not raiz:
        return

    cola = deque([raiz])  # Usamos una cola para el recorrido BFS

    while cola:
        # Procesamos el nodo actual
        nodo_actual = cola.popleft()
        print(f"{nodo_actual.nombre_grado}: {', '.join(nodo_actual.estudiantes)}")

        # Agregamos los hijos del nodo actual a la cola
        for hijo in nodo_actual.hijos:
            cola.append(hijo)

# Ejemplo de uso
# Creamos el árbol de grados
grado12 = Grado("Grado 12", ["Ana", "Carlos", "Laura"])
grado11 = Grado("Grado 11", ["Pedro", "Sofía"])
grado10 = Grado("Grado 10", ["Juan", "Isabel"])
grado9 = Grado("Grado 9", ["Luis", "Marta"])

# Establecemos la jerarquía
grado12.agregar_hijo(grado11)
grado11.agregar_hijo(grado10)
grado10.agregar_hijo(grado9)

# Llamamos a la función para mostrar el recorrido por niveles
recorrido_por_niveles(grado12)
