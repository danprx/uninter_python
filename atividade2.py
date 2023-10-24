print('Bem vindo a sorveteria do Daniel Pereira Rolim da Silva!')
print('#-------------------------------------------Cardápio------------------------------------------#')
print('| Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |')
print('#---------------------------------------------------------------------------------------------#')

total = 0  # Acumula o valor total da venda

while True:
    # Variável do tipo de sorvete
    cod = input('Digite o código do sorvete desejado (TR/ES/PR): ').upper()

    # Variável do tamanho do pote do sorvete
    tam = input('Escolha o tamanho do pote do sorvete (P/M/G): ').upper()

    # Sorvete Tradicional e seus tamanhos
    if cod == 'TR' and tam == 'P':
        print('Você pediu um sorvete TRADICIONAL PEQUENO de R$6,00!')
        total += 6  # Adiciona o valor ao total
    elif cod == 'TR' and tam == 'M':
        print('Você pediu um sorvete TRADICIONAL MÉDIO de R$10,00!')
        total += 10  # Adiciona o valor ao total
    elif cod == 'TR' and tam == 'G':
        print('Você pediu um sorvete TRADICIONAL GRANDE de R$18,00!')
        total += 18  # Adiciona o valor ao total

    # Sorvete Especial e seus tamanhos
    elif cod == 'ES' and tam == 'P':
        print('Você pediu um sorvete ESPECIAL PEQUENO de R$7,00!')
        total += 7  # Adiciona o valor ao total
    elif cod == 'ES' and tam == 'M':
        print('Você pediu um sorvete ESPECIAL MÉDIO de R$12,00!')
        total += 12  # Adiciona o valor ao total
    elif cod == 'ES' and tam == 'G':
        print('Você pediu um sorvete ESPECIAL GRANDE de R$21,00!')
        total += 21  # Adiciona o valor ao total

    # Sorvete Premium e seus tamanhos
    elif cod == 'PR' and tam == 'P':
        print('Você pediu um sorvete PREMIUM PEQUENO de R$8,00!')
        total += 8  # Adiciona o valor ao total
    elif cod == 'PR' and tam == 'M':
        print('Você pediu um sorvete PREMIUM MÉDIO de R$14,00!')
        total += 14  # Adiciona o valor ao total
    elif cod == 'PR' and tam == 'G':
        print('Você pediu um sorvete PREMIUM GRANDE de R$24,00!')
        total += 24  # Adiciona o valor ao total

    # Se digitar tamanho ou código inválido, exibe erro e retorna ao inicio do programa
    else:
        print('TAMANHO ou CÓDIGO INVÁLIDO(S)!')
        print('--------------------------------------------------')
        continue

    print('--------------------------------------------------')

    # Pergunta se o cliente deseja mais alguma coisa
    repetir = input('Deseja mais alguma coisa? (S/N): ').upper()

    if repetir == 'S':
        continue  # Se sim, retorna ao início do programa
    else:
        print('O total a ser pago é de R$ {:.2f}!'.format(total))
        print('Agradecemos seu pedido e volte sempre!')
        break  # Se não, exibe o total a ser pago e encerra o programa
