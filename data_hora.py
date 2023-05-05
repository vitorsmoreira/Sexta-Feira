# Módulo que manipula o tempo em Python.
from datetime import datetime

from gtts import gTTS  # Converte texto em voz.
from playsound import playsound  # Toca o áudio.


def capturar_momento_atual():
    """Captura o momento atual.

    Returns:
        datetime: momento atual.
    """

    return datetime.now()


def capturar_tempo(agora: datetime) -> tuple[int, int]:
    """Pega a hora atual.

    Args:
        agora (datetime): momento atual capturado pela máquina.

    Returns:
        tuple(int, int): tupla contendo a hora 
        e o minuto atual.
    """

    return agora.hour, agora.minute


def capturar_data() -> tuple[int, int, int]:
    """Pega dia, mês e ano atuais.

    Returns:
       tuple(int, int, int): tupla contendo o dia, mês 
       e ano atual.
    """

    dia = datetime.today().day
    mes = datetime.today().month
    ano = datetime.today().year

    return dia, mes, ano


def nomear_mes(mes: int) -> str:
    """Retorna o mês em sua versão por extenso.

    Args:
        mes (int): mês em formato de número.

    Returns:
        str: mês em sua versão escrita por extenso.
    """

    # Dicionário contendo o mês e seu nome por extenso.
    dict_mes = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }

    # Transforma o número do mês em nome do mês por extenso.
    return dict_mes[mes]


def escrever_mensagem(
        hora: int, minuto: int, dia: int, mes_extenso: str, ano: int) -> str:
    """Escreve a mensagem que será lida pela Sexta-Feira.

    Args:
        hora (int): horário atual.
        minuto (int): minuto atual.
        dia (int): dia atual.
        mes_extenso (str): mês atual por extenso.
        ano (int): ano atual

    Returns:
        str: mensagem que será lida pela Sexta-Feira.
    """

    mensagem = f"Agora são:\n" \
        f"{hora} horas e {minuto} minutos\n" \
        f"do dia {dia} de {mes_extenso} de {ano}."

    return mensagem


def falar_mensagem(mensagem: str) -> None:
    """Reproduz a mensagem em forma de áudio.

    Args:
        mensagem (str): mensagem a ser lida pela Sexta-Feira.
    """

    audio = gTTS(mensagem, lang="pt")
    audio.save("msg.mp3")
    playsound("msg.mp3")


def principal():
    """Função que chama todas as outras.
    """

    momento_atual = capturar_momento_atual()
    hora, minuto = capturar_tempo(momento_atual)
    dia, mes, ano = capturar_data()
    nome_mes = nomear_mes(mes)
    mensagem = escrever_mensagem(hora, minuto, dia, nome_mes, ano)
    falar_mensagem(mensagem)


principal()
