import json
import os

# Archivo de guardado
ARCHIVO = 'tareas.json'

# Cargar tareas si existe el archivo
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r') as f:
            return json.load(f)
    return []

# Guardar tareas
def guardar_tareas(tareas):
    with open(ARCHIVO, 'w') as f:
        json.dump(tareas, f)

# Menú principal
def menu():
    tareas = cargar_tareas()
    while True:
        print("\n1. Agregar tarea\n2. Ver tareas\n3. Buscar tarea\n4. Actualizar tarea\n5. Eliminar tarea\n6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            descripcion = input("Descripción: ")
            tareas.append({'id': len(tareas) + 1, 'desc': descripcion, 'estado': 'pendiente'})
            guardar_tareas(tareas)
            print("Tarea agregada exitosamente.")
        elif opcion == '2':
            for t in tareas:
                print(f"ID: {t['id']}, Desc: {t['desc']}, Estado: {t['estado']}")
        elif opcion == '3':
            busqueda = input("Buscar por descripción: ")
            encontrados = [t for t in tareas if busqueda.lower() in t['desc'].lower()]
            for t in encontrados:
                print(f"ID: {t['id']}, Desc: {t['desc']}, Estado: {t['estado']}")
            if not encontrados:
                print("No se encontraron tareas.")
        elif opcion == '4':
            id_t = int(input("ID a actualizar: "))
            for t in tareas:
                if t['id'] == id_t:
                    t['estado'] = 'completada'
                    guardar_tareas(tareas)
                    print("Tarea actualizada.")
                    break
            else:
                print("ID no encontrado.")
        elif opcion == '5':
            id_t = int(input("ID a eliminar: "))
            tareas = [t for t in tareas if t['id'] != id_t]
            guardar_tareas(tareas)
            print("Tarea eliminada.")
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")

menu()