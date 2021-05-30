from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia
# se importa información del archivo configuracion
from configuracion import cadena_base_datos

import csv

# Se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Abre el archivo csv
data = open('../data/Listado-Instituciones-Educativas.csv')
# Lee el csv y separa cada columna con el delimitador "|"
read = csv.reader(data, delimiter='|')

next(read)# Salta la primera fila del csv

# Arreglo que almacenará todos los valores obtenidos de las columnas que componen al obj Provincia
listaProv = [] 

# Ciclo para obtener todas las provincias del csv
for row in read:
    provincias = row[2] + "|" + row[3]
    # Se agrega la variable anterior a la lista
    listaProv.append(provincias)
# Se obtienen los valores unicos de la lista "listaProv"
listaProv = list(set(listaProv))


# Ciclo para obtener todos los atributos unicos a la tabla Provincia
for row in listaProv:
    # Se crea cada objeto de tipo Provincia
    prov = Provincia(id = row.split("|")[0], nombre_provincia = row.split("|")[1])
    # Se agregan los datos de prov a la BD
    session.add(prov)

# Se confirman los cambios 
session.commit()
