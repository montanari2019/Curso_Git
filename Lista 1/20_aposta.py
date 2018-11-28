'''20) (BACKES, 2012) Tres amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser
repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um
programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada
um ganharia do prêmio com base no valor investido. Salve o projeto com o nome “​ 20_aposta ” ​ .'''

n1=float(input("Digite o o valor que o 1 apostador investiu:"))
n2=float(input("Digite o o valor que o 1 apostador investiu:"))
n3=float(input("Digite o o valor que o 1 apostador investiu:"))
premio=float(input("Digite o premio:"))

aposta=n1+n2+n3

print("1 Apostador:",round(premio/aposta*n1,2))
print("2 Apostador:",round(premio/aposta*n3,2))
print("3 Apostador:",round(premio/aposta*n2,2))