# Módulo que trabalha com tempo.
from datetime import datetime, timedelta
import time

# Importa bibliotecas de voz.
from gtts import gTTS  # Converte texto em voz.
from playsound import playsound  # Toca o áudio.


def separar_frase(frase: str) -> list:
    """Separa as palavras da frase.

    Args:
        frase (str): frase que será avaliada para temporizar o timer.

    Returns:
        list: palavras retiradas do timer.
    """    
    return frase.split()
        
        
def capturar_momento_atual() -> datetime:
    """Captura o momento atual.

    Returns:
        datetime: momento atual.
    """

    return datetime.now()

        
def verificar_hora(frase: list) -> int:
    """Verifica se o temporizador contará o horário.

    Args:
        frase (list): frase a ser avaliada para ver se tem de
        contabilizar horário.

    Returns:
        int: quantidade de horário a ser contabilizado.
    """    
    
    for i in range(len(frase)):
        if (frase[i].upper() == "HORAS" or
        frase[i].upper() == "HORA" or
        frase[i].upper() == "HORAS," or
        frase[i].upper() == "HORA," or
        frase[i].upper() == "HORAS." or
        frase[i].upper() == "HORA."):
            return int(frase[i - 1])
    
    return 0
        
        
def verificar_minuto(frase: list) -> int:
    """Verifica se o temporizador contará a minutagem.

    Args:
        frase (list): frase a ser avaliada para ver se tem de
        contabilizar minutagem. 

    Returns:
        int: quantidade de minutagem a ser contabilizada.
    """    
    
    for i in range(len(frase)):
        if (frase[i].upper() == "MINUTOS" or
        frase[i].upper() == "MINUTO" or
        frase[i].upper() == "MINUTOS," or
        frase[i].upper() == "MINUTO," or
        frase[i].upper() == "MINUTOS." or
        frase[i].upper() == "MINUTO."):
            return int(frase[i - 1])
        
    return 0
        
        
def verificar_segundo(frase: list) -> int:
    """Verifica se o temporizador contará os segundos.

    Args:
        frase (list): frase a ser avaliada para ver se tem de
        contabilizar os segundos.

    Returns:
        int: quantidade de segundos a ser contabilizados.
    """    
    
    for i in range(len(frase)):
        if (frase[i].upper() == "SEGUNDOS" or
        frase[i].upper() == "SEGUNDO" or
        frase[i].upper() == "SEGUNDOS," or
        frase[i].upper() == "SEGUNDO," or
        frase[i].upper() == "SEGUNDOS." or
        frase[i].upper() == "SEGUNDO."):
            return int(frase[i - 1])
        
    return 0


def temporizar(
    hora: int, minuto: int, 
    segundo: int, momento_atual: datetime) -> datetime:
    """Calcula o tempo que o timer terminará.

    Args:
        hora (int): horas do timer a ser contabilizado.
        minuto (int): minutos do timer a ser contabilizado.
        segundo (int): segundos do timer a ser contabilizado.
        momento_atual (datetime): instante temporal registrado na máquina.

    Returns:
        datetime: momento em que terminará o timer na máquina.
    """    
    
    timer = timedelta(hours=hora, minutes=minuto, seconds=segundo)
    termino = momento_atual + timer
    
    return termino


def contar_timer(termino: datetime) -> None:
    """Roda o timer.

    Args:
        termino (datetime): momento na máquina em que o timer irá
        terminar.
    """    
    
    while datetime.now() < termino:
        # Colocar algo codigo
        time.sleep(1)
    
    
def falar_mensagem(mensagem: str) -> None:
    """Reproduz a mensagem em forma de áudio.

    Args:
        mensagem (str): mensagem a ser lida pela Sexta-Feira.
    """

    audio = gTTS(mensagem, lang="pt")
    audio.save("msg.mp3")
    playsound("msg.mp3")
    

def principal(comando: str) -> None:
    """Módulo principal roda que todos as funções do módulo.

    Args:
        comando (str): comando que receberá quanto tempo rodar
        um timer.
    """    
        
    agora = capturar_momento_atual()
    frase = separar_frase(comando)
    print(frase)
    horario = verificar_hora(frase)
    minutagem = verificar_minuto(frase)
    segundo = verificar_segundo(frase)
    fim_timer = temporizar(horario, minutagem, segundo, agora)
    
    falar_mensagem("Começo do timer!")
    contar_timer(fim_timer)
    falar_mensagem("Fim do timer!")
    
    
print(datetime.now())
principal("Sexta-Feira, timer de 30 segundos.")
print(datetime.now())
