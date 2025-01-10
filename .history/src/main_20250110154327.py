from datetime import datetime
from exceptions import MyAppValueError

def calculador_dos_fechas(str1, str2):
     #str1 = input("Introduce una fecha actual (dd/mm/yyyy):")
     #str2 = input("Introduce una fecha de nacimiento, para medir cuantos dias faltan (dd/mm/yyyy):")

     try:
         fecha_actual = datetime.strptime(str1, "%d/%m/%Y")
         fecha_nacimiento = datetime.strptime(str2, "%d/%m/%Y")
     except ValueError:
         raise MyAppValueError("ERROR. No cumple con el formato indicado")
     

     if(fecha_actual < fecha_nacimiento):
         raise MyAppValueError("ERROR. La fecha actual debe ser mayor a la de nacimiento")
 
     proximo_cumple = fecha_nacimiento.replace(year=fecha_actual.year)

     if proximo_cumple < fecha_actual:
        proximo_cumple = proximo_cumple.replace(year=fecha_actual.year + 1)


     diferencia = (proximo_cumple - fecha_actual).days
     return diferencia
    


def funcion_principal():
     print("Hola!! Esta funcion calcula los dias que faltan transcurrir para tu proximo cumpleaños.\n Para ello ingresa los siguientes datos")
     str1 = input("Primero ingresa la FECHA ACTUAL (dd/mm/yyyy):")
     str2 = input("Ahora ingresa una FECHA DE NACIMIENTO (dd/mm/yyyy):")

     try:
         dias = calculador_dos_fechas(str1, str2)
         print("Estos son los dias que faltan para tu proximo cumpleaños")
         print(dias)
     except MyAppValueError as e:
         print(e)
         print("Volve a intentarlo")

     
#LLAMADO DE FUNCION
funcion_principal()