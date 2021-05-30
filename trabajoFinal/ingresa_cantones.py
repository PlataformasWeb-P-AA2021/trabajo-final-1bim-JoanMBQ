from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia, Canton
# se importa información del archivo configuracion
from configuracion import cadena_base_datos

import csv

# se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Abre el archivo csv
data = open('../data/Listado-Instituciones-Educativas.csv')
# Lee el csv y separa cada columna con el delimitador "|"
read = csv.reader(data, delimiter='|')

next(read)# Salta la primera fila del csv

# Arreglo que almacenará todos los valores obtenidos de las columnas que componen al obj Canton
listaCanton = []

# Ciclo para obtener todos los cantones del csv
for row in read:
    cantones = row[2] + "|" + row[4] + "|" + row[5]
    # Se agrega la variable anterior a la lista
    listaCanton.append(cantones)
# Se obtienen los valores unicos de la lista "listaCanton"
listaCanton = list(set(listaCanton))


# Ciclo para obtener todos los atributos unicos a la tabla Canton
for row in listaCanton:
    # Variable que devuelve la provincia de cada canton
    consultaProvincia = session.query(Provincia).filter_by(id = row.split("|")[0]).first()
    # Se crea cada objeto de tipo Canton
    canton = Canton(id = row.split("|")[1], 
                    nombre_canton = row.split("|")[2], 
                    provincia = consultaProvincia)
    # Se agregan los datos de canton a la BD
    session.add(canton)

# Se confirman los cambios 
session.commit()