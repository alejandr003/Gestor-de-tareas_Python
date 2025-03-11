class Tarea:
    def __init__(self, tarea_id, titulo, descripcion="", completada=False, prioridad="normal"):
        # Asignamos los valores básicos de la tarea
        self.id = tarea_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada
        
        # Prioridades válidas para validación
        prioridades_validas = ["baja", "normal", "alta"]
        # Verificar que la prioridad proporcionada sea válida
        if prioridad not in prioridades_validas:
            raise ValueError(f"Prioridad inválida. Debe de ser una de: {prioridades_validas}")
        # Asignamos si la prioridad es válida
        self.prioridad = prioridad
        
    def __eq__(self, other):
        # Verificamos primero si el otro objeto es una instancia de Tarea
        if not isinstance(other, Tarea):
            return False
        
        # Si lo es, comparamos por ID (dos tareas son iguales si tienen el mismo ID)
        return self.id == other.id
    
class GestorTareas:
    def __init__(self):
        self.tareas = []
        
        # Contador para asignar IDs únicos a las tareas
        self.contador_id = 0
    
    def agregar_tarea(self, titulo, descripcion="", prioridad="normal"):
        self.contador_id += 1
        # Creamos una nueva tarea con los datos proporcionados
        nueva_tarea = Tarea(self.contador_id, titulo, descripcion, False, prioridad)
        self.tareas.append(nueva_tarea)
        return nueva_tarea
    
    def eliminar_tarea(self, tarea_id):
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                self.tareas.remove(tarea)
                return True
        return False
    
    def buscar_tarea_por_id(self, tarea_id):
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                return tarea
        return None
    
    def marcar_tarea_completada(self, tarea_id):
        tarea = self.buscar_tarea_por_id(tarea_id)
        if tarea:
            tarea.completada = True
            return True
        return False
    
    def listar_tareas(self, pendientes=False):
        if pendientes:
            return [tarea for tarea in self.tareas if not tarea.completada]
        return self.tareas
    
    def filtrar_tareas_por_prioridad(self, prioridad):
        return [tarea for tarea in self.tareas if tarea.prioridad == prioridad]