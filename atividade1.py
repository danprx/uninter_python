print('Seja bem-vindo a loja do Daniel Pereira Rolim da Silva!\n')

custoEmbalagem = 0  # Recebe o  valor do custo da embalagem para o frete
total = 0  # Recebe o valor total da venda

# Recebe o valor unitário de cada produto
valorProduto = float(input('Qual o valor unitário do seu produto? \n'
                           '>> '))

# Recebe a quantidade de produtos
qtdProduto = float(input('Qual a quantidade do seu produto? \n'
                         '>> '))
# Verificação do custo de embalagem baseado na quantidade do produto
if 0 <= qtdProduto < 11:
    custoEmbalagem = 30
elif 11 <= qtdProduto < 101:
    custoEmbalagem = 60
elif 101 <= qtdProduto < 1001:
    custoEmbalagem = 120
else:
    custoEmbalagem = 240

# Multiplica o valor unitário pela quantidade do produto
total = valorProduto * qtdProduto

# Exibe total SEM frete
print('O valor total SEM o frete foi de: R${:.2f}.'.format(total))

# Exibe total COM frete
print('O valor total COM o frete foi de: R${:.2f}. (Valor do frete R${:.2f})'.format(
    total+custoEmbalagem, custoEmbalagem))
