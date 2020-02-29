'''Ler largura e e altura de uma parede em metrosm calcular a area da parede
 e a quantidade de tinta necessária para pintá-la. sabendo que 1L de tinta pinta 2m² da parede '''

#Uso do conceito de expressões lambda

largura = float(input('Largura: '))
altura = float(input('Altura: '))


def calcArea(larg, altu):
    return larg * altu
   
#area = lambda larg, altu: larg*altu
area = calcArea(largura, altura)
litros = (area / 2)

print(
    f'''Sua parede tem a dimensão de {largura}m X {altura}m e a sua área é de {area}m²\n
        Litros de tinta necessários: {litros}''')