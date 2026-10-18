# leer_excel.py — Cargar el consolidado Excel de finanzas (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_excel.py

# TODO 1: importa pandas
# TODO 2: carga data/ventas.xlsx indicando la hoja correcta
# TODO 3: imprime las dimensiones y las primeras filas

#Para leer el archivo exel hay que señalar en que hoja esta la información que
# se quiere leer : sheet_name "ventas"
ventasss= pd.read_excel("data/ventas.xlsx", sheet_name="ventas")

#Imprime las primeras 5 filas 
print(ventasss.head())

#Imprime las dimenciones 
print(ventasss.shape)
