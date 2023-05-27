class Estudiantes():
    def __init__(self):
        self.estudiantes = []
        self.promedios_id = {}
    
    def Agregar_estudiantes(self, nuevo_estudiante):
        """
        Función que agrega un estudiante a la lista de estudiantes
        
        Parameters:
        id: id del estudiante
        nombre: nombre del estudiante
        lista: lista de los estudiantes
        
        Returns:
        El nuevo estudiate agregado a la lista.
        """
        self.estudiantes.append(nuevo_estudiante)
        
    def buscar_estudiante(self, id):
        """
        Busca a un estudiante por su id
        
        Parameters:
        id: id del estudiante
        estudiantes: lista de los estudiantes
        
        Returns:
        información del estudiante sí se encuentra
        None: si no se encuentra el estudiante
        """
        for e in self.estudiantes:
            if e.id == id:
                return e
        return None
        
    def orden_estudiantes(self,e):
        print('id:',e.id)
        print('nombre:', e.nombre)
        print('notas:',e.notas)
        print('puesto:', e.puesto)
        print('promedio:', e.promedio)
            
    def orden_estudiantes_top(self, e):
        print('\n---------------- puesto: {} ----------------\n'.format(e.puesto))
        print('id:',e.id)
        print('nombre:', e.nombre)
        print('notas:',e.notas)
        print('promedio:', e.promedio)
            