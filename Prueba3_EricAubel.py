import csv
prestamos = []
nombre_profe=("Pablo Saldaña")
sigla=("BIY1101")
seccion=("008D")

def validar_entradas (rut, nombre, documento, num_note):
    if not rut or not nombre or not documento or not num_note:
        print("Todos los campos son obligatorios para realizar el prestamo")
        return False   
    return True



def validar_prestamo (rut, nombre, documento, num_note):
    if validar_entradas (rut, nombre, documento, num_note):
        prestamos.append ({
            'rut': rut,
            'nombre': nombre,
            'documento':documento,
            'Número notebook': num_note
        })
    else:
        print("Ha fallado el préstamo, porfavor intentelo de nuevo")
    return  

def regresar_prestamo (rut):
    for prestamo in prestamos:
        if prestamo ['rut']==rut:
            prestamos.remove (rut)
            print(f"El notebook ha sido devuelto con éxito por {rut}")
        else:
            print("Ha fallado la devolución, porfavor intentélo de nuevo")
    return

def modif_prestamo (rut, num_note, nuevo_numero_note):
    for prestamo in prestamos:
        if prestamo ['rut']==rut:
            prestamos.remove(num_note)
            prestamos.append (nuevo_numero_note) 
    print(f"El notebook {num_note} ha sido cambiado exitosamente por{rut} a {nuevo_numero_note}")
    return
def lista_notebooks ():
    filename=f"{nombre_profe},{'','_'}, {sigla},{seccion}.csv"
    with open (filename, mode='r', newline=''):
        print(filename)
    return
def terminar_clase ():
    if not prestamos:
        print("Todos los notebook han sido devueltos, la clase termina")
    else:
        print("Faltan notebooks por entregar, nadie sale hasta que estén todos los aparatos") 

def main():
    global prestamos, nombre_profe, sigla, seccion 
    prestamos =[]
    validar_prestamo('20791625-0', 'Eric Aubel', 'carnet', '001')

main() 