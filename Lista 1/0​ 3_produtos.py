#3) (PUGA & RISSETI, 2016) Uma loja de produtos eletrônicos com vendas regulares opta por
#contratar uma equipe para a organização de um sistema de gerenciamento de vendas. Seu
#desafio será elaborar um algoritmo que, a partir de dados fornecidos pelo usuário, calcule o
#valor da venda de um produto, exibindo uma saída em vídeo contendo o código do produto, o
#nome, quantidade comprada, o valor unitário e o valor total.

produto=input("Digite o nome do produto:")
cod_produto=input("Digite o codigo do produto:")
quant=float(input("Digite a quantidade:"))
valor_unit=float(input("Digite o valor do(a) "+produto+":"))
valor_total=valor_unit*quant
print("Produto:",produto,"\nCod. Produto:",cod_produto,"\nQuant:",quant,"\nvalor Unitário R$",valor_unit,"\nValor Total R$",valor_total)
