from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Parroquia, Canton
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

# Arreglo que almacenará todos los valores obtenidos de las columnas que componen al obj Parroquia
listaPqa = []

# Ciclo para obtener todas los cantones del csv
for row in read:
    parroquias = row[4] + "|" + row[6] + "|" + row[7]
    # Se agrega la variable anterior a la lista
    listaPqa.append(parroquias)
# Se obtienen los valores unicos de la lista "listaPqa"
listaPqa = list(set(listaPqa))

# Ciclo para obtener todos los atributos unicos a la tabla Parroquia
for row in listaPqa:
    # Variable que devuelve el canton de cada parroquia
    consultaCanton = session.query(Canton).filter_by(id = row.split("|")[0]).first()
    # Se crea cada objeto de tipo Parroquia
    pqa = Parroquia(    id = row.split("|")[1], 
                        nombre_parroquia = row.split("|")[2], 
                        canton = consultaCanton)
    # Se agregan los datos de pqa a la BD
    session.add(pqa)

# Se confirman los cambios 
session.commit()