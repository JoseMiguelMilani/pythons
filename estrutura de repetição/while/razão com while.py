pt = int( input('primeiro termo:'))
repetição = 0
razao = int(input('qual a razão:'))
estancia = -1
termo = 1

while estancia != 9:
    estancia +=1
    soma = pt+(estancia*razao)
    print(soma)

termo = int(input('quer mais quantos termos:\033[32m'))
while termo != 0:

    while termo != 9+termo:
        estancia +=1
        soma = pt+(estancia*razao)
    print('\033[m{}'.format(soma))
    termo = int(input('quer mais quantos termos:\033[32m'))



