#importar el modulo Unittest
import unittest
#Importar el modulo gestor_tareas
from gestor_tareas import GestorTareas, Tarea

#Definir la clase de prueba
class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        #crear una instancia de GestorTareas
        self.gestor = GestorTareas()
        
        #Agregar tareas de ejemplo con diferentes prioridades
        self.tarea1 = self.gestor.agregar_tarea("Realizar tarea", "Elaborar tarea de testing", "alta")
        self.tarea2 = self.gestor.agregar_tarea("Estudiar python", "Pruebas unitarias", "normal")
        self.tarea3 = self.gestor.agregar_tarea("Proyecto integradora", "Avanzar con el desarrollo", "baja")
        
    def test_agregar_tarea(self):
        # Agregar una nueva tarea
        tarea = self.gestor.agregar_tarea("Tarea prueba", "Aprender a hacer pruebas SW", "normal")
        
        # Verificar que la tarea se agregó correctamente
        self.assertEqual(tarea.titulo, "Tarea prueba")
        self.assertEqual(tarea.descripcion, "Aprender a hacer pruebas SW")
        self.assertEqual(tarea.prioridad, "normal")
        self.assertFalse(tarea.completada)
        self.assertEqual(tarea.id, 4)
    
    def test_eliminar_tarea(self):
        # Eliminar una tarea existente
        resultado = self.gestor.eliminar_tarea(self.tarea1.id)
        self.assertTrue(resultado)
        
        # Intentar eliminar una tarea inexistente
        resultado = self.gestor.eliminar_tarea(5)
        self.assertFalse(resultado)
    
    def test_buscar_tarea_por_id(self):
        # Buscar una tarea existente
        tarea = self.gestor.buscar_tarea_por_id(self.tarea2.id)
        self.assertEqual(tarea, self.tarea2)
        
        # Buscar una tarea inexistente
        tarea = self.gestor.buscar_tarea_por_id(999)
        self.assertIsNone(tarea)
    
    def test_marcar_tarea_completada(self):
        # Marcar una tarea existente como completada
        resultado = self.gestor.marcar_tarea_completada(self.tarea3.id)
        self.assertTrue(resultado)
        self.assertTrue(self.tarea3.completada)
        
        # Intentar marcar una tarea inexistente como completada
        resultado = self.gestor.marcar_tarea_completada(999)
        self.assertFalse(resultado)
    
    def test_listar_tareas(self):
        # Listar todas las tareas
        todas_las_tareas = self.gestor.listar_tareas()
        self.assertEqual(len(todas_las_tareas), 3)
        
        # Listar tareas pendientes
        tareas_pendientes = self.gestor.listar_tareas(pendientes=True)
        self.assertEqual(len(tareas_pendientes), 3)
    
    def test_filtrar_tareas_por_prioridad(self):
        # Filtrar tareas por prioridad alta
        tareas_alta = self.gestor.filtrar_tareas_por_prioridad("alta")
        self.assertEqual(len(tareas_alta), 1)
        
        # Filtrar tareas por prioridad normal
        tareas_normal = self.gestor.filtrar_tareas_por_prioridad("normal")
        self.assertEqual(len(tareas_normal), 1)
        
        # Filtrar tareas por prioridad baja
        tareas_baja = self.gestor.filtrar_tareas_por_prioridad("baja")
        self.assertEqual(len(tareas_baja), 1)
        
        # Filtrar tareas por prioridad inexistente
        tareas_inexistente = self.gestor.filtrar_tareas_por_prioridad("inexistente")
        self.assertEqual(len(tareas_inexistente), 0)
    
    def test_validacion_prioridades_no_validas(self):
        # Comprobar que se lanza una excepción cuando se utiliza una prioridad no válida
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("Tarea inválida", "Descripción", "muy alta")
    
    def test_comparacion_tareas(self):
        # Comprobar que dos tareas con el mismo ID pero diferentes atributos se consideran iguales
        tarea_duplicada = Tarea(self.tarea1.id, "Título diferente", "Descripción diferente", "normal")
        self.assertEqual(self.tarea1, tarea_duplicada)
        
        # Comprobar que dos tareas con diferente ID se consideran diferentes
        tarea_diferente = Tarea(999, "Título", "Descripción", "alta")
        self.assertNotEqual(self.tarea1, tarea_diferente)
        
        # Comprobar que la tarea no es igual a un objeto de otro tipo
        self.assertNotEqual(self.tarea1, "no es una tarea")
        
if __name__ == "__main__":
    unittest.main()