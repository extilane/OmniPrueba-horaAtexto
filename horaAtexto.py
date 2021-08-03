# -----------------------------------------------------------
# Prueba tecnica para proceso de reclutamiento en Omni
#
# 2021 Guillermo Alonso Avila Chaves, Alajuela, Costa Rica
# email gach151195@gmail.com
# -----------------------------------------------------------

import re
import sys
from const import *

def validacionHora(hora):
    """ Funcion que valida el formato deseado [horas]:[minutos][am/pm]
    Argumentos:
    hora -- Debe ser un string con el formato [horas]:[minutos][am/pm]
    Salida:
    Un True si cumple el formato esperado de 12 horas y un false si no cumple el formato.
    """
    return bool(re.match(formatoRE, hora))

def horario(hora, momento):
    """Funcion que menciona cual horario es mañana, tarde o noche
    Argumentos:
    hora -- Debe ser un int de 1 hasta 12
    momento -- Debe ser string AM o PM
    Salida:
    La palabra tarde, noche o mañana.
    """
    if ((hora <= 6 and hora >= 1) or hora == 12) and momento == "PM":
        return "tarde"
    if hora >= 6 and momento == "PM":
        return "noche"
    else:
        return "mañana"
    
def extraccionConversion(hora):
    """Funcion que extrae el valor individualmente de la hora, minuto y AM o PM.
    Argumentos:
    hora -- Debe ser un string con el siguiete formato [horas]:[minutos][am/pm]
    Salida:
    Es una lista con 3 elementos el 0 es la hora, el 1 son los minutos y tercero son el AM o PM.
    """    
    registros = re.search(formatoRE, hora)
    return [int(registros.group(1)),int(registros.group(2)),registros.group(3)]

def constructorOraciones(hora, minuto, momento):
    """Funcion que genera la frase de salida para el programa.
    Argumentos:
    hora -- Debe ser un int entre 1 y 12 que es la hora.
    minuto -- Debe ser un int entre 0 y 59 que son minutos.
    momento -- Debe ser un string con los valores AM o PM.
    Salida:
    Es un string con el hora en redaccion.
    """
    if hora == 12 and minuto == 0 and momento == "AM":
        return "Es media noche"
    if hora == 12 and minuto == 0 and momento == "PM":
        return "Es medio día"
    if hora == 1 and minuto == 0:
        return "Es la " +distNum[hora] +" "+distNum[minuto] +" de la " +horario(hora,momento)
    if hora == 1:
        return "Son la " +distNum[hora] +" y "+distNum[minuto]+" de la "+horario(hora,momento)
    if minuto == 0:
        return "Son las "+distNum[hora]+" "+distNum[minuto]+" de la "+horario(hora,momento)
    else:
        return "Son las "+distNum[hora]+" y "+distNum[minuto]+" de la " + horario(hora,momento)
    
def horaTexto(hora):
    """Es la funcion principal del programa donde se valida, se parsea y se transforma la hora en redaccion.
    Argumentos:
    hora -- Debe ser un string con el formato [horas]:[minutos][am/pm]
    Salida:
    Es un string con el hora en redaccion.
    """
    hora = hora.upper()
    if validacionHora(hora):
        registrosParcedos = extraccionConversion(hora)
        horas = registrosParcedos[0]
        minuto = registrosParcedos[1]
        momento = registrosParcedos[2]
        return constructorOraciones(horas, minuto, momento)
    else:
        raise ValueError("Formato Incorrecto")
        
print(horaTexto(sys.argv[1]))  
    
    
    
    
