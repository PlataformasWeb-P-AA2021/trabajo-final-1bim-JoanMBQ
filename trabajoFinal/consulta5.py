from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import * 

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por nombre de parroquia que tengan más de
# 20 profesores y la cadena "Permanente" en tipo de educación.
consultaEst = session.query(Establecimiento)\
    .join(Parroquia)\
    .filter(and_(Establecimiento.num_Docentes > 20 , Establecimiento.tipo\
        .like("%Permanente%")))\
    .order_by(Parroquia.nombre_parroquia).all()

# Se imprimen los resultados
print("ESTABLECIMIENTOS ORDENADOS POR NOMBRE CON MÁS DE 20 PROFESORES\n")
for x in consultaEst:
    print("Código AMIE: %-10s || Num Docentes %-5s || Institución: %s" % 
        (x.id, x.num_Docentes, x.nombre_establecimiento))
print("\n\n")

#---------------------------------------------------------------

# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.
consultaEst = session.query(Establecimiento)\
    .filter(Establecimiento.distrito == "11D02")\
    .order_by(Establecimiento.sostenimiento).all()

# Se imprimen los resultados
print("ESTABLECIMIENTOS ORDENADOS POR SOSTENIMIENTO DEL DISTRTIO 11D02")
for x in consultaEst:
    print("Código AMIE: %-10s || Sostenimiento %-15s || Institución: %s" % 
        (x.id, x.sostenimiento, x.nombre_establecimiento))