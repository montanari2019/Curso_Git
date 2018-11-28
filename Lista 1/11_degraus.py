'''11) (BACKES, 2012) Receba a altura do degrau de uma escada e a altura que o usuário deseja
alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para
atingir seu objetivo. Salve o projeto com o nome “​ 11_degraus ” ​ .'''

degrau=float(input("Digite o tamanho do degrau:"))
altura=float(input("Digite a altura que desejas subir:"))
print("Serão Nescessarios",int(altura/degrau)," degraus")
