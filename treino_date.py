from datetime import datetime, timedelta


agora = datetime.now()
timer = timedelta(seconds=10)

termino = agora + timer

while datetime.now() < termino:
    print("Checado!")

print(termino)