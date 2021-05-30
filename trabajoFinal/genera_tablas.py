from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Creación de la tabla Provincia con todos sus atributos
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(String(10), primary_key=True)
    nombre_provincia = Column(String(100), nullable=False)
    cantones = relationship("Canton", back_populates="provincia")

# Creación de la tabla Canton con todos sus atributos
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(String(10), primary_key=True)
    nombre_canton = Column(String(100), nullable=False)
    parroquias = relationship("Parroquia", back_populates="canton")
    provincia_id = Column(String(10), ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="cantones")

# Creación de la tabla Parroquia con todos sus atributos
class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(String(10), primary_key=True)
    nombre_parroquia = Column(String(100), nullable=False)
    establecimiento = relationship("Establecimiento", back_populates="parroquia")
    canton_id = Column(String(10), ForeignKey('canton.id'))
    canton = relationship("Canton", back_populates="parroquias")

# Creación de la tabla Establecimiento con todos sus atributo
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(String(10), primary_key=True)
    nombre_establecimiento = Column(String(100), nullable=False)
    distrito = Column(String(100), nullable=False)
    sostenimiento = Column(String(100), nullable=False)
    tipo = Column(String(100), nullable=False)
    modalidad = Column(String(100), nullable=False)
    jornada = Column(String(100), nullable=False)
    acceso = Column(String(100), nullable=False)
    num_Estudiantes = Column(Integer, nullable=False)
    num_Docentes = Column(Integer, nullable=False)
    parroquia_id = Column(String(10), ForeignKey('parroquia.id'))
    parroquia = relationship("Parroquia", back_populates="establecimiento")

Base.metadata.create_all(engine)
