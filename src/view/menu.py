class ViewMenu:

    @staticmethod
    def main_menu():
        print("\nORGANIZADOR DE MATERIAS\n")
        print("1. Consultas")
        print("2. Agregar Datos")
        print("3. Limpiar Pantalla")
        print("4. Salir")

    @staticmethod
    def query_menu():
        print("\nCONSULTAS:\n")
        print("1. Promedio")
        print("2. Créditos")
        print("3. Materias Cursables")
        print("4. Materias Aprobadas")
        print("5. Estado de Carrera")
        print("6. Volver")

    @staticmethod
    def upload_menu():
        print("\nMODIFICACIÓN DATOS:\n")
        print("1. Materia Aprobada")
        print("2. Borrar Nota")
        print("3. Aplazo")
        print("4. Volver")

    @staticmethod
    def grades_menu():
        print("\nCONSULTA DE PROMEDIO:\n")
        print("1. Promedio sin CBC")
        print("2. Promedio con CBC")
        print("3. Volver")
