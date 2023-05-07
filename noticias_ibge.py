import requests # Biblioteca para realizar requisições.

from gtts import gTTS  # Converte texto em voz.
from playsound import playsound  # Toca o áudio.


def capturar_requisicao():
    """Captura requisição do site do IBGE.

    Returns:
        Response: retorna a requisicação do site do IBGE.
    """    
    
    url = "http://servicodados.ibge.gov.br/api/v3/noticias/?de=05-01-2023"
    r = requests.get(url)    
    
    return r


def pegar_noticia(r) -> str:
    """Pega a última notícia requisitada.

    Args:
        r (Response): requisição do site da IBGE.

    Returns:
        str: retorna o texto do título da notícia do IBGE.
    """    
    
    r_json = r.json()
    json_items = r_json["items"]
    primeira_noticia = json_items[-1]
    
    return primeira_noticia["titulo"]


def falar_mensagem(mensagem: str) -> None:
    """Reproduz a mensagem em forma de áudio.

    Args:
        mensagem (str): mensagem a ser lida pela Sexta-Feira.
    """

    audio = gTTS(mensagem, lang="pt")
    audio.save("msg.mp3")
    playsound("msg.mp3")
    
    
def principal() -> None:
    """Função que chama todas as outras funções.
    """    
    
    
    requisicao = capturar_requisicao()
    msg = pegar_noticia(requisicao)
    falar_mensagem(msg)
    

principal()
