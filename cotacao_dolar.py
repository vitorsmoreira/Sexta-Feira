import requests

from gtts import gTTS  # Converte texto em voz.
from playsound import playsound  # Toca o áudio.


def capturar_requisicao():
    """Captura a requisição da API para cotação de moedas.

    Returns:
        Responses: requisição da API para cotação de moedas.
    """    
    
    url = "http://economia.awesomeapi.com.br/json/last/USD-BRL"
    r = requests.get(url)    
    
    return r


def converter_json(requisicao) -> dict:
    """Converte requisicao em um dicionário.

    Args:
        requisicao (Response): requisição da API de cotação
        de moedas.

    Returns:
        dict: dicionário contendo as informações da contação
        entre duas moedas.
    """    
    
    return requisicao.json()
    

def pegar_cotacao(cotacao: dict) -> float:
    """Pega o valor da moeda.

    Args:
        cotacao (dict): dicionário contendo todas as informações
        da cotação da moeda.

    Returns:
        float: valor em real da moeda.
    """    
    
    dolar_str = cotacao['USDBRL']
    cotacao_dolar = float(dolar_str["bid"])
    cotacao_dolar = round(cotacao_dolar, 2)
    
    return cotacao_dolar


def separar_real_centavo(cotacao_dolar: float) -> tuple:
    """Separa e armazena os reais e os centavos.

    Args:
        cotacao_dolar (float): valor da cotação em real.

    Returns:
        tuple: tupla contendo os reais e os centavos
        do valor da cotação.
    """    
    
    dolar_str = str(cotacao_dolar)
    reais, centavos = dolar_str.split(".")
    
    return reais, centavos


def escrever_mensagem(real: str, centavo: str) -> str:
    """Cria a mensagem que será falada pelo programa.

    Args:
        real (str): quantidade de reais da cotação em real.
        centavo (str): quantidade de centavos da cotação em real.

    Returns:
        str: mensagem a ser falada pela Sexta-Feira.
    """    
    
    msg = f"O dólar está valendo {real} reais e {centavo} centavos."
    
    return msg


def falar_mensagem(mensagem: str) -> None:
    """Reproduz a mensagem em forma de áudio.

    Args:
        mensagem (str): mensagem a ser lida pela Sexta-Feira.
    """

    audio = gTTS(mensagem, lang="pt")
    audio.save("msg.mp3")
    playsound("msg.mp3")
    

def principal() -> None:
    """Função que chama todas as outras.
    """    
    
    r = capturar_requisicao()
    cotacao_dict = converter_json(r)
    dolar = pegar_cotacao(cotacao_dict)
    reais, centavos = separar_real_centavo(dolar)
    msg = escrever_mensagem(reais, centavos)
    falar_mensagem(msg)
    
    
principal()
