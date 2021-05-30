from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Establecimiento, Parroquia
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

# Ciclo para obtener todos los atributos para la tabla Establecimiento
for row in read:
    # Variable que devuelve la parroquia de cada establecimiento
    parroquias = session.query(Parroquia).filter_by(id = row[6]).first()
    # Se crea cada objeto de tipo Establecimiento
    est = Establecimiento(  id = row[0],
                            nombre_establecimiento = row[1], 
                            distrito = row[8], 
                            sostenimiento = row[9],
                            tipo = row[10], 
                            modalidad = row[11], 
                            jornada = row[12], 
                            acceso = row[13], 
                            num_Estudiantes = int(row[14]),
                            num_Docentes = int(row[15]),
                            parroquia = parroquias)
    # Se agregan los datos de est a la BD
    session.add(est) 

# Se confirman los cambios 
session.commit()