'''9) (BACKES, 2012) Faça um programa para ler as dimensões de um terreno (comprimento (C)
e largura (L)), bem como o preço do metro de tela (P). Imprima o custo para cercar este mesmo
terreno com tela. Salve o projeto com o nome “0​ 9_cerca ” ​ .'''

comprimento=float(input("Digite o comprimento do terreno:"))
largura=float(input("Digite a largura do terreno:"))
preco =float(input("Digite o Preço do metro:"))
valor_total=(comprimento*2+largura*2)*preco

print("O preço Total da Cerca: R$",valor_total)