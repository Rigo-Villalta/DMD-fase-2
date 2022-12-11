from tempfile import NamedTemporaryFile
import shutil
import csv
# Createmos un archivo temporal con el modo escribir "w"
parque_vehicular_modificado = NamedTemporaryFile(mode="w", delete=False)
fields = [
    "TIPO_PLACA", 
    "ANIO_DE_FABRICACION",# 1
    "CILINDRADA", #2
    "CANTIDAD_DE_CILINDROS", "CANTIDAD_DE_PUERTAS", "VALOR_DEL_VEHICULO",
    "COLORES", "FECHA_DE_IMPORTACION", "IMP_VALOR_DEL_VEHICULO",
    "FECHA_DE_INGRESO", "ANIO_INGRESO", "MES_INGRESO", "CLASE",
    "PERTENENCIA", "MARCA", "MODELO", "CAPACIDAD", "DES_CAPACIDAD",
    "COMBUSTIBLE", "ADUANA", "CONDICION_INGRESO", "PROPIETARIO_DEPARTAMENTO",
    "PROPIETARIO_MUNICIPIO","ESTADO"
    ]


# Abrimos nuestro archivo en modo escribir
with open("parque_vehicular.csv", "r") as parque_vehicular, parque_vehicular_modificado:
    # Creo un nuevo archivo csv en modo escritura, ahí guardamos lo ocupado
    lectura_de_archivo = csv.DictReader(parque_vehicular, fieldnames=fields)
    writer = csv.DictWriter(parque_vehicular_modificado, fieldnames=fields)
    # En Python cada fila se vuelve una lista, iteramos el archivo en cada lista
    for fila in lectura_de_archivo:
        # ahora vamos a tratar de modificar de que cada campo que queremos limpiar
        # lo haremos con los campos que nos han dado algún problema, CILINDRADA y ANIO_DE_FABRICACION:
        try:
            # convertimos el dato en entero
            nueva_cilindrada = int(fila[1])
            nuevo_anio_de_fabricacion = float(fila[2])
            nueva_fila = [
                fila[0], nueva_cilindrada, nuevo_anio_de_fabricacion,
                fila[3], fila[4], fila[5], fila[6], fila[7],
                fila[8], fila[9], fila[10], fila[11], fila[12],
                fila[13], fila[14], fila[15], fila[16], fila[17],
                fila[18], fila[19], fila[20], fila[21],  fila[22],
                fila[23]
            ]
            writer.writerow(nueva_fila)
        except:
            # si falla se ignora la fila
            pass
#Al terminar la iteracion guradamos el nuevo archvio
shutil.move(parque_vehicular_modificado.name, "parque_vehicular_modificado.csv")