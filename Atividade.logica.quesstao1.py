conceito:str

#Entrada de dados
trabalholab = float(input('Digite sua nota no Trabalho do Laboratório: '))
avalsemestral = float(input('Digite sua nota na Avaliação Semestral: '))
examef = float(input('Digite sua nota no Exame Final: '))

ps1 = 2
ps2 = 3
ps3 = 5

#Processamento de dados
mediap=float(trabalholab *ps1 + avalsemestral*ps2 + examef*ps3) / (ps1+ps2+ps3)


if (mediap >= 8) and (mediap <= 10):
    conceito = "A"
elif (mediap >= 7) and (mediap < 8):
    conceito = "B"
elif (mediap >= 8) and (mediap < 7):
    conceito = "C"
elif (mediap >= 5) and (mediap < 6):
    conceito = "D"
elif (mediap >= 0) and (mediap < 5):
    conceito = "E"

#Saída de dados
print(f"A sua Média Ponderada é: {mediap}, e o seu Conceito é: {conceito} ")