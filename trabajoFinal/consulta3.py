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

# Los cantones que tiene establecimientos con 0 número de profesores
consulta1 = session.query(Canton)\
    .join(Parroquia, Establecimiento)\
    .filter(Establecimiento.num_Docentes == 0).all()

# Se imprimen los resultados
print("CANTONES CON ESTABLECIMIENTOS CON 0 PROFESORES\n")
for x in consulta1:
    print("Cod Cantón: %-5s || Cantón: %s" % 
        (x.id, x.nombre_canton))
print("\n\n")

#---------------------------------------------------------------

# Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
consulta2 = session.query(Establecimiento)\
    .join(Parroquia)\
    .filter(and_(Parroquia.nombre_parroquia == "CATACOCHA",
                 Establecimiento.num_Estudiantes >= 21))\
    .order_by(Establecimiento.num_Estudiantes).all()

# Se imprimen los resultados
print("ESTABLECIMIENTOS DE CATACOCHA CON 21 O MÁS ESTUDIANTES\n")
for x in consulta2:
    print("Código AMIE: %-10s || Num Estudiantes %-5s || Institución: %s" % 
        (x.id, x.num_Estudiantes, x.nombre_establecimiento))