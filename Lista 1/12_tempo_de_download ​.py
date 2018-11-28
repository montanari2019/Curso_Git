'''12) (Python.org.br) Faça um programa que peça o tamanho de um arquivo para download (em
MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos). Salve o projeto com o nome
“​ 12_tempo_de_download ​ ”.'''

arquivo = float(input("Digite o tamanho do Arquivo em MB:"))
velocidade = float(input("Digite a velocidade da internet em Mbps:"))
tempo=(arquivo * 1024 * 8) / (velocidade*1000) / 60

print("Tempo:",tempo)
