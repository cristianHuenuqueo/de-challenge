## Funcionamiento
- Se debe instalar python en el sistema operativo
- La ejecución del ETL se puede automatizar en Windows en el administrador de tareas o en Linux con crontab
- Para la ejecución manual se debe descargar Spyder desde la url https://github.com/spyder-ide/spyder/releases/latest/download/Spyder_64bit_full.exe y realizar la instalación

## Resultados
- Al ejecutar el ETL los datos resultantes quedarán en la carpeta del proyecto resultados_datos

## Librería y métodos utilizados
- Se utilizó Pandas para realizar el ETL
- Se importan datos a trabajar con Pandas 
  - Para las funciones mejores y peores juegos por consola/empresa:
    - Creación de listas para guardar datos de iteraciones por consola
    - Se obtuvieron los 10 valores más altos en la columna metascore iterando por consola, guardándolos en un arreglo
    - Luego se realizó una query en Pandas con el mínimo y máximo del arreglo para filtrar dataframe
    - Se utilizó función de Pandas rank() para rankiar metascore por consola
    - Ingreso de datos en listas creadas
    - Ingreso de listas a Dataframe con los datos procesados
    - Exportación a csv separados por pipe (|)
 - Para las funciones de mejores y peores juegos para todas las consolas
  - Se utilizó función rank() de Python
  - Se ordena dataframe según su necesidad y se renombran columnas
  - Filtro de registros en el ranking menor e igual a 10
  - Exportación a csv separados por pipe (|)
