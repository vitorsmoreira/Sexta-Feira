# Módulo que trabalha com tempo.
from datetime import datetime, timedelta
import time


def separar_frase(frase: str) -> list:
    
    return frase.split()
        
        
def capturar_momento_atual() -> datetime:
    """Captura o momento atual.

    Returns:
        datetime: momento atual.
    """

    return datetime.now()

        
def verificar_hora(frase: list) -> int:
    
    for i in range(len(frase)):
        if (frase[i].upper() == "HORAS" or
        frase[i].upper() == "HORA"):
            return int(frase[i - 1])
    
    return 0
        
        
def verificar_minuto(frase: list) -> int:
    
    for i in range(len(frase)):
        if (frase[i].upper() == "MINUTOS" or
        frase[i].upper() == "MINUTO"):
            return int(frase[i - 1])
        
    return 0
        
        
def verificar_segundo(frase: list) -> int:
    
    for i in range(len(frase)):
        if (frase[i].upper() == "SEGUNDOS" or
        frase[i].upper() == "SEGUNDO"):
            return int(frase[i - 1])
        
    return 0


def temporizar(
    hora: int, minuto: int, 
    segundo: int, momento_atual: datetime) -> datetime:
    
    timer = timedelta(hours=hora, minutes=minuto, seconds=segundo)
    termino = momento_atual + timer
    
    return termino
    

def principal(comando: str) -> None:
    
    agora = capturar_momento_atual()
    frase = separar_frase(comando)
    print(frase)
    horario = verificar_hora(frase)
    minutagem = verificar_minuto(frase)
    segundo = verificar_segundo(frase)
    
    fim_timer = temporizar(horario, minutagem, segundo, agora)
    
    while datetime.now() < fim_timer:
        # Colocar algo codigo
        time.sleep(1)
    
    print("Fim do timer!")
    

print(datetime.now())
principal("Sexta-Feira, timer de 1 minuto")
print(datetime.now())
