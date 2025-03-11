import unittest
# Importamos la clase de prueba original
from test_gestor_tareas import TestGestorTareas

def ejecutar_test(test_name, descr):
    print(f"\n=== Ejecutando prueba: {descr} ===")
    suite = unittest.TestSuite()
    suite.addTest(TestGestorTareas(test_name))
    runner = unittest.TextTestRunner(verbosity=2) 
    runner.run(suite)

def main():
    opciones = {
        "1": ("test_eliminar_tarea", "Eliminación de tareas (existentes e inexistentes)"),
        "2": ("test_buscar_tarea_por_id", "Búsqueda de tareas por ID"),
        "3": ("test_marcar_tarea_completada", "Marcar tareas como completadas"),
        "4": ("test_listar_tareas", "Listar todas las tareas"),
        "5": ("test_filtrar_tareas_por_prioridad", "Filtrar tareas por prioridad"),
        "6": ("test_validacion_prioridades_no_validas", "Validación de prioridades"),
        "7": ("test_comparacion_tareas", "Comparación de tareas"),
        "8": ("test_agregar_tarea", "Agregar tarea"),
    }
    
    while True:
        print("\n=== MENÚ DE PRUEBAS DEL GESTOR DE TAREAS ===")
        for key, (_, desc) in opciones.items():
            print(f"{key}. {desc}")
        print("9. Ejecutar todas las pruebas")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "0":
            print("Saliendo del programa...")
            break
        elif opcion == "9":
            unittest.main(argv=['first-arg-is-ignored'], exit=False)
        elif opcion in opciones:
            ejecutar_test(*opciones[opcion])
        else:
            print("Opción no válida")
            
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()