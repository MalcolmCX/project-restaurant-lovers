n1=input('Qual nome do primeiro produto: ')
n2=input('Qual nome do segundo produto: ')

p1=int(input(f'Digite quantos itens de {n1}:\n'))
p2=int(input(f'Digite quantos itens de {n2}:\n'))

if p1>p2:
   print(f'A quantidade de vendas de {n1} foram maior')
elif p2>p1:
    print(f'A quantidade de vendas de {n2} foram maior')
else:
    print(f'Quantidade de vendas de {n1} e {n2} são iguais')