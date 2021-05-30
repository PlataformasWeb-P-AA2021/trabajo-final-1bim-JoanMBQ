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

# Todos los establecimientos de la provincia de Loja.
consulta1 = session.query(Establecimiento)\
    .join(Parroquia, Canton, Provincia)\
    .filter(Provincia.nombre_provincia == 'LOJA').all()

# Se imprimen los resultados
print("ESTABLECIMIENTOS DE LA PROVINCIA DE LOJA\n")
for x in consulta1:
    print("Código AMIE: %-10s || Sostenimiento %-15s || Institución: %s" % 
        (x.id, x.sostenimiento, x.nombre_establecimiento))
print("\n\n")

#---------------------------------------------------------------

# Todos los establecimientos del cantón de Loja.
consulta2 = session.query(Establecimiento)\
    .join(Parroquia, Canton)\
    .filter(Canton.nombre_canton == 'LOJA').all()

# Se imprimen los resultados
print("ESTABLECIMIENTOS DEL CANTON DE LOJA\n")
for x in consulta2:
    print("Código AMIE: %-10s || Sostenimiento %-15s || Institución: %s" % 
        (x.id, x.sostenimiento, x.nombre_establecimiento))
print("\n\n")
