# Trabajo Final Primer Bimestre

El Archivo ***configuracion.py*** solo contiene información de las configuraciones posibles configuraciones.
Por el momento solo contiene la cadena conector a la base de datos

Para empezar con el proyecto se hace lo siguiente:

* En primer lugar se crean las tablas que componen a la base de datos ejecutando el archivo:

	* genera_tablas.py

* Luego para evitar errores o falta de datos, la ejecución de los archivos .py debe ser el siguiente:

	* ingresa_provincias.py
	* ingresa_cantones.py
	* ingresa_parroquias.py
	* ingresa_establecimientos.py

* Y finalmente se ejecutan cada uno de los archivos de consulta_.py. El contenido de cada consulta se muestra a continuación

	* consulta1.py
		* Todos los establecimientos de la provincia de Loja.
		* Todos los establecimientos del cantón de Loja.
	* consulta2.py
		* Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
		* Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
	* consulta3.py
		* Los cantones que tiene establecimientos con 0 número de profesores
		* Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
	* consulta4.py
		* Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.
		* Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
	* consulta5.py
		* Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
		* Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.