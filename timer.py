# Módulo que trabalha com tempo.
from datetime import datetime


def separar_frase(frase: str) -> list:
    
    return frase.split()
        

def separar_tempo(frase: list) -> str:
    
    
    for tempo in frase:
        if (frase[-1].upper() == "HORAS" or
        frase[-1].upper() == "HORA"):
            return "horas"
        elif (frase[-1].upper() == "MINUTOS" or
            frase[-1].upper() == "MINUTO"):
            return "minutos"
        elif (frase[-1].upper() == "SEGUNDOS" or
            frase[-1].upper() == "SEGUNDO"):
            return "segundos"
        else:
            return "erro"
    

def capturar_momento_atual() -> datetime:
    
    return datetime.now()