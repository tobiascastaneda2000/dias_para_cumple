import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Importar la función desde src.main
from src.main import calculador_dos_fechas


#str1 = input("Introduce una fecha actual (dd/mm/yyyy):")
#str2 = input("Introduce una fecha de nacimiento, para medir cuantos dias faltan (dd/mm/yyyy):")

#SI el dia y mes de nacimiento TODAVIA  no paso este año

def test_aun_no_paso_cumple_el_mismo_mes_hace_un_Anio():
    assert calculador_dos_fechas("01/03/2000", "09/03/1999") == 8

def test_aun_no_paso_cumple_el_mismo_mes_hace_5_anios():
    assert calculador_dos_fechas("08/01/2025", "20/01/1995") == 12

def test_aun_no_paso_cumple_el_proximo_mes():
    assert calculador_dos_fechas("01/03/2000", "01/04/1999") == 31

def test_aun_no_paso_cumple_el_mismo_mes_hace_diez_anios():
    assert calculador_dos_fechas("01/03/2001", "02/03/1990") == 1

def test_aun_no_paso_cumplira_en_mas_de_un_mes():
    assert calculador_dos_fechas("01/03/2003", "01/05/2000") == 61

#SI el dia y mes de nacimiento YA pasaron este año

def test_cumple_ya_paso_un_anio_antes():
    assert calculador_dos_fechas("30/01/2000", "20/01/1999") == 356

def test_cumple_ya_paso_mismo_anio():
    assert calculador_dos_fechas("30/01/2000", "20/01/2000") == 356


def test_cumple_ya_paso_tres_anio_antes():
    assert calculador_dos_fechas("30/01/2000", "20/01/1997") == 356

def test_cumple_ya_paso_cinco_anio_antes():
    assert calculador_dos_fechas("30/01/2000", "20/01/1995") == 356

def test_cumple_ya_paso_diez_anio_antes():
    assert calculador_dos_fechas("30/01/2000", "20/01/1990") == 356

def test_cumple_ya_paso_cien_anio_antes():
    assert calculador_dos_fechas("30/01/2000", "20/01/1900") == 356

def test_cumple_ya_paso_mismo_anio_no_bisiesto():
    assert calculador_dos_fechas("30/01/1999", "20/01/1999") == 355

