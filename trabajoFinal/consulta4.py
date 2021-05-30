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

# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores. 
consultaEst = session.query(Establecimiento)\
    .filter(Establecimiento.num_Docentes > 100)\
    .order_by(Establecimiento.num_Estudiantes).all()

# Se imprimen los resultados
print("ESTABLECIMIENTOS CON MÁS DE 100 PROFESORES ORDENADOS POR EL NUMERO DE ESTUDIANTES\n")
for x in consultaEst:
    print("Código AMIE: %-10s || Num Estudiantes %-5s || Institución: %s" % 
        (x.id, x.num_Estudiantes, x.nombre_establecimiento))
print("\n\n")

#---------------------------------------------------------------

# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
consultaEst = session.query(Establecimiento)\
    .filter(Establecimiento.num_Docentes > 100)\
    .order_by(Establecimiento.num_Docentes).all()

# Se imprimen los resultados
print("ESTABLECIMIENTOS CON MÁS DE 100 PROFESORES ORDENADOS POR EL NUMERO DE DOCENTES\n")
for x in consultaEst:
    print("Código AMIE: %-10s || Num Docentes %-5s || Institución: %s" % 
        (x.id, x.num_Docentes, x.nombre_establecimiento))
