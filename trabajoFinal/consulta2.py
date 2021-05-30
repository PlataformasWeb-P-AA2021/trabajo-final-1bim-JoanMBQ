from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_ # se importa el operador or

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import * 

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
consulta1 = session.query(Parroquia)\
    .join(Establecimiento)\
    .filter(Establecimiento.jornada == 'Nocturna').all()

# Se imprimen los resultados
print("PARROQUIAS CON ESTABLIMIENTOS UNICAMENTO CON JORDNADA NOCTURNA\n")
for x in consulta1:
    print("Cod Parroquia: %-7s || Parroquia: %s" % 
        (x.id, x.nombre_parroquia))
print("\n\n")

#---------------------------------------------------------------

# Los cantones que tiene establecimientos como número de estudiantes tales como:
# 448, 450, 451, 454, 458, 459
consulta2 = session.query(Canton)\
    .join(Parroquia, Establecimiento)\
    .filter(or_(
        Establecimiento.num_Estudiantes == 448 , 
        Establecimiento.num_Estudiantes == 450,
        Establecimiento.num_Estudiantes == 451,
        Establecimiento.num_Estudiantes == 454,
        Establecimiento.num_Estudiantes == 458,
        Establecimiento.num_Estudiantes == 459)).all()

# Se imprimen los resultados
print("CANTONES CON ESTABLECIMIENTOS CON: 448, 450, 451, 454, 458, 459 ESTUDIANTES:\n")
for x in consulta2:
    print("Cod Cantón: %-5s || Cantón: %s" % 
        (x.id, x.nombre_canton))