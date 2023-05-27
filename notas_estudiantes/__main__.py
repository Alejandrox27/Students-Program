from notas_estudiantes.modelos.Estudiantes import Estudiantes
from notas_estudiantes.modelos.estudiante import Estudiante
import heapq
import pickle
import os

def menu():
    print('inserte una de las siguientes opciones:')
    print('1. Agregar nuevos estudiantes')
    print('2. Agregar notas a los estudiantes')
    print('3. Eliminar estudiantes retirados.')
    print('4. Ver un top 5 de los mejores estudiantes según su promedio')
    print('5. Buscar a un estudiante por su codigo')
    print('6. Ver los puestos de todos los estudiantes')
    print('0. Salir.')

def continuar():
    print()
    input('inserte enter para continuar...')
    print()

def listar_estudiantes(estudiantes):
    """
    hace una secuencia de todos los estudiantes en la lista
    por su id y nombre
    """
    for e in estudiantes:
        print(f'{e.id} - {e.nombre}')
def abrir_archivo():
    nombre_archivo = 'notas_estudiantes/estudiantes.pickle'
    while True:
        try:
            opcion = int(input('¿Desea abrir la información de los estudiantes?\n'
                            '1. Si\n'
                            '2. No\n>>>'))
            if opcion == 1 or opcion == 2:
                break
        except ValueError as e:
            print('MENSAJE: Debe ser un valor entero 1 o 2.')
            
    if opcion == 1:
        with open(nombre_archivo, 'rb') as f:
            estudiantes = pickle.load(f)
            return estudiantes
        
    return None
    

def guardar_archivo(Estudiantes):
    nombre_archivo = 'notas_estudiantes/estudiantes.pickle'
    while True:
        try:
            opcion = int(input('¿Desea guardar la información de los estudiantes?\n'
                            '1. Si\n'
                            '2. No\n>>>'))
            if opcion == 1 or opcion == 2:
                break
        except ValueError as e:
            print('MENSAJE: Debe ser un valor entero 1 o 2.')
            
    if opcion == 1:
        with open(nombre_archivo, 'wb') as f:
            pickle.dump(Estudiantes,f)
        return True
    else:
        return False


def main():
    eestudiantes = Estudiantes()
    
    if os.path.isfile('notas_estudiantes/estudiantes.pickle'):
        estudiantes_1 = abrir_archivo()
        
        if estudiantes_1:
            eestudiantes.estudiantes = estudiantes_1.estudiantes
            eestudiantes.promedios_id = estudiantes_1.promedios_id
    while True:
        while True:
            
            try:
                menu()
                print()
                opcion = int(input('--->'))
                if 0 <= opcion < 7:
                    break
                else:
                    print('MENSAJE: La opción debe ser un valor entre 0 y 6.')
                    continuar()
            except ValueError as e:
                print('MENSAJE:',e)
                continuar()
                
        if opcion == 0:
            break
        
        elif opcion == 1:
            while True:
                try:
                    id = int(input('inserte el id del estudiante en concreto: '))
                    break
                except ValueError as e:
                    print('MENSAJE:',e)
                    continuar()
            
            while True:
                try:
                    nombre = input('inserte el nombre del estudiante: ')
                    break
                except ValueError as e:
                    print('MENSAJE:',e) 
                    continuar()
                    
            nuevo_estudiante = Estudiante(id, nombre)
            eestudiantes.Agregar_estudiantes(nuevo_estudiante)
            print()
            print('el estudiante ha sido agregado con exito.')
            continuar()
        
        elif opcion == 2:
            if len(eestudiantes.estudiantes):
                while True:
                    print()
                
                    try:
                        while True:
                            listar_estudiantes(eestudiantes.estudiantes)
                            
                            id = int(input('inserte el id del estudiante para agregar sus notas: '))
                            estudiante = eestudiantes.buscar_estudiante(id)
                            if estudiante == None:
                                print()
                                print('MENSAJE: Debe agregar un estudiante de la lista')
                                continuar()
                                continue
                            break
                        nota = float(input('inserte la nota a agregar: '))
                        break
                    except ValueError as e:
                        print('ERROR:',e)
                        continuar()
                
                estudiante = eestudiantes.buscar_estudiante(id)
                
                if len(estudiante.notas) < 5:
                    estudiante.notas.append(nota)
                    print()
                    eestudiantes.orden_estudiantes(estudiante)
                    if len(estudiante.notas) == 5:
                        estudiante.promedio = round((sum(estudiante.notas)) / (len(estudiante.notas)),2)
                        
                        for e in eestudiantes.estudiantes:
                            if e.promedio == None:
                                continue
                            eestudiantes.promedios_id[e.id] = e.promedio
                    
                        prom = sorted([(v,k) for k,v in eestudiantes.promedios_id.items()],reverse = True)
                        num = 1
                        for e in prom:
                            estudiante = eestudiantes.buscar_estudiante(e[1])
                            estudiante.puesto = num
                            num += 1
                            
                    continuar()
                else:
                    print()
                    print('NOTA: solo se pueden agregar 5 notas por estudiante')
                    
                    continuar()
                
                
            else:
                print('todavia no hay ningun estudiante agregado\nagrege un estudiante con la opción 1.')
                continuar()
                
        elif opcion == 3:
            if len(eestudiantes.estudiantes):
                while True:
                    
                    try:
                        while True:
                            listar_estudiantes(eestudiantes.estudiantes)
                
                            id = int(input('inserte el id del estudiante a eliminar: '))
                            estudiante = eestudiantes.buscar_estudiante(id)
                            if estudiante == None:
                                print()
                                print('MENSAJE: Debe agregar un estudiante de la lista')
                                continuar()
                                continue
                            break
                    
                        
                        confirmacion = int(input('Quiere eliminar a {} con codigo {}?'
                                             '\n1. Sí'
                                             '\n2. No'
                                             '\n>>>'.format(estudiante.nombre,id)))
                        
                        if confirmacion == 1:                     
                            eestudiantes.estudiantes.remove(estudiante)
                            if len(eestudiantes.promedios_id):
                                eestudiantes.promedios_id.pop(id)
                            print()
                            print('MENSAJE: El estudiante ha sido eliminado con exito.')
                            continuar()
                            break
                            
                        elif confirmacion == 2:
                            print('Perfecto, se ha cancelado la opción.')
                            break
                            
                        else:
                            print('MENSAJE: elije 1 o 2')
                    except ValueError as e:
                        print('ERROR:',e)
                        continuar()
                        
                
            else:
                print('MENSAJE: Aún no ha agragado a ningun estudiante.')
                continuar()
                
        elif opcion == 4:
            if len(eestudiantes.estudiantes):
                for e in eestudiantes.estudiantes:
                    if e.promedio == None:
                        continue
                    eestudiantes.promedios_id[e.id] = e.promedio
                prom = sorted([(v,k) for k,v in eestudiantes.promedios_id.items()],reverse = True)
                num = 1
                for e in prom:
                    estudiante = eestudiantes.buscar_estudiante(e[1])
                    estudiante.puesto = num
                    num += 1
                print('\n---------------------Top 5 mejores estudiantes---------------------\n')
                for e in heapq.nlargest(5,prom):
                    estudiante = eestudiantes.buscar_estudiante(e[1])
                    eestudiantes.orden_estudiantes_top(estudiante)
                    print()
                    
                continuar()
            else:
                print()
                print('MENSAJE: Aún no se ha agregado a ningun estudiante')
                continuar()
        
        elif opcion == 5:
            if len(eestudiantes.estudiantes):
                
                
                while True:
                    try:
                        listar_estudiantes(eestudiantes.estudiantes)
                
                        id = int(input('inserte el id del estudiante a buscar: '))
                        estudiante = eestudiantes.buscar_estudiante(id)
                        if estudiante == None:
                            print()
                            print('MENSAJE: Debe agregar un estudiante de la lista')
                            continuar()
                            continue
                        break
                    except ValueError as e:
                        print('ERROR:',e)
                        continuar()
                estudiante = eestudiantes.buscar_estudiante(id)
                print()
                eestudiantes.orden_estudiantes(estudiante)
                continuar()
            else:
                print('Todavia no ha agregado a algun estudiante.')
                continuar()
                
        elif opcion == 6:
            if len(eestudiantes.estudiantes):
                for e in eestudiantes.estudiantes:
                    if e.promedio == None:
                        continue
                    eestudiantes.promedios_id[e.id] = e.promedio
                    
                prom = sorted([(v,k) for k,v in eestudiantes.promedios_id.items()],reverse = True)
                num = 1
                for e in prom:
                    estudiante = eestudiantes.buscar_estudiante(e[1])
                    print(f'{num}. {estudiante.id} - {estudiante.nombre} ----------> {e[0]}')
                    num += 1
                continuar()
            else:
                print()
                print('MENSAJE: Aún no ha ingresado a algun estudiante')
                continuar()
                
    if guardar_archivo(eestudiantes):
        print('MENSAJE: La información se ha guardado con exito.')
        
    else:
        print('MENSAJE: La información no se guardó.')
    continuar()
    
    print('El programa ha finalizado.')
    
if __name__ == '__main__':
    main()