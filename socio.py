import os
import json
from dataclasses import dataclass, asdict


# nro_socios: int 

path = os.path.dirname(os.path.abspath(__file__))
path = path + '\\static\\socios.json'

@dataclass
class Socio():
    # _nro_socio: int
    _dni: str
    _nombre: str
    _apellido: str


    @classmethod
    def crear_socio(cls):
        dni: str = input('Ingrese el DNI del socio: ')
        nombre: str = input('Ingrese el nombre del socio: ')
        apellido: str = input('Ingrese el apellido del socio: ')

        socio = asdict(Socio(dni, nombre, apellido))
        # socio = asdict(socio)

        if os.path.isfile(path):

            with open(path, 'r') as archivo:
                data = json.load(archivo)

            with open(path, 'w') as archivo:
                data.append(socio)
                json.dump(data, archivo, default=str)
                print('Socio agregado al archivo')

        else:
            with open(path, 'w') as archivo:
                print('Se creó el archivo socios.json')
                json.dump([socio], archivo, default=str)
                print('Socio agregado al archivo')

    @classmethod
    def mostrar_socios(cls):
        if os.path.isfile(path):

            with open(path) as archivo:
                socios = json.load(archivo)

                for socio in socios:
                    print(socio)

        else:
            print('Aún no hay socios cargados!')
