import random

# Lista das piadas
piadas = [
    "Por que o cachorro entrou no cinema? Para assistir ao uivernil!",
    "O que é que é verde e que corre muito? A alface-pé-de-coelho!",
    "Por que a galinha atravessou a rua? Para chegar ao bar do outro lado!",
    "O que é que é amarelo e que escreve? Um lápis de banana!",
    "Por que a água foi presa? Porque ela matou a sede!",
    "Por que o pato foi ao dentista? Porque ele tinha cárie de pato!",
    "Qual o país que é redondo e mora no Japão? O Japãobol!",
    "O que o pato disse para a pata? Vem Quá!",
    "Por que o menino estava falando ao telefone deitado? Para não cair a ligação",
    "Por que a abelha foi no médico? Porque ela estava se sentindo zumbi!",
    "Por que o gato mia? Porque ele não sabe falar!",
    "Qual é a cidade brasileira que não tem táxi? Uberlândia",
    "O que é que é uma bola verde no céu? Uma ervilha voadora!",
    "Por que o policial não usa sabão? Porque ele prefere deter gente",
    "Por que a planta não responde? Porque ela é mudinha",
    "Por que a girafa tem um pescoço comprido? Para alcançar os galhos mais altos!",
]


def contar_piada():
    # Escolhe uma piada aleatoriamente da lista
    piada = random.choice(piadas)

    print(piada)  # Substituir para a voz da sexta-feira
    # Para chamar a execução do módulo de piadas, use contar_piada()
