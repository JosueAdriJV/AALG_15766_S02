votos = {1:0 , 2:0 , 3:0 , 4:0}

voto = int(input("Ingrese un voto (0 = terminar): " ))

while voto != 0:

    if voto >= 1 and voto <= 4 :
        votos[voto] += 1
    else:
       print("Voto invalido")

    voto = int(input("Ingrese un voto (0 = terminar): " ))

total_votos = sum(votos.values())
print("resultados:")

for candidato, cantidad_votos in votos.items():
    
    porcentaje = (cantidad_votos / total_votos) * 100 if total_votos > 0 else 0
    print(f"Candidato {candidato}: {cantidad_votos} votos ({porcentaje:.2f}%)")

