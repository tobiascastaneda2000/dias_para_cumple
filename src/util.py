from datetime import datetime

def cantidad_de_dias_en_anio(ano):
    # Función que determina si un año es bisiesto.
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return 366
    else:
        return 365

def calcular_diferencia_anios(dias, anio):
    aux_dias = dias
    anios = 0
    anio_aux = anio
    total_dias = cantidad_de_dias_en_anio(anio)
    while aux_dias >= total_dias:
        
        aux_dias = aux_dias - total_dias
        anios += 1
        anio_aux += 1  # Avanzamos al siguiente año
        total_dias = cantidad_de_dias_en_anio(anio)
    return anios

def calcular_diferencia_de_dias(str1, str2):
    d_act = datetime.strptime(str1, "%d/%m/%Y")
    d_nac = datetime.strptime(str2, "%d/%m/%Y")

    diferencia = d_act - d_nac

    return diferencia.days