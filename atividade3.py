print('Bem vindo ao programa de Serviços de Limpeza do Daniel Pereira Rolim da Silva!')


# Função para calcular valor do metro quadrado
def metragem_limpeza():
    valor = 0
    try:
        # Pergunta a metragem
        metragem = int(input('Qual a metragem do local? (em m²): '))
    except ValueError:
        # Erro caso o valor não seja numérico
        print('Insira um valor numérico, por favor!')
    else:
        if 30 <= metragem < 300:
            valor = 0.3 * metragem + 60
            print('É necessário contratar 1 pessoa.')
        elif 300 <= metragem < 700:
            valor = 0.5 * metragem + 120
            print('É necessário contratar 2 pessoas.')
        else:
            # Erro caso o valor seja fora do trabalhado
            print('São válidos SOMENTE valores entre 30 e 699 m²!')
    finally:
        return valor


# Função que retorna o valor do tipo da limpeza
def tipo_limpeza():
    valor = 0
    # Pergunta o tipo de limpeza desejado
    tipo = input('Escolha o tipo da limpeza (B/C): ').upper()
    if tipo == 'B':
        valor = 1
    elif tipo == 'C':
        valor = 1.3
    else:
        # Erro caso for digitado uma opção inválida
        print('Digite uma opção válida!')
    return valor


# Função que retorna o valor do adicional
def adicional_limpeza():
    try:
        # Pergunta se deseja mais algum adicional
        adicional = int(input('Deseja mais algum adicional? (0/1/2/3): '))
    except ValueError:
        # Erro caso seja digitado um valor não numérico
        print('Digite um opção válida!')
        return 'erro'
    else:
        if adicional == 0:
            return 0
        elif adicional == 1:
            return 10
        elif adicional == 2:
            return 12
        elif adicional == 3:
            return 20
        else:
            # Erro caso seja digitado algum outro valor
            print('Digite um opção válida!')
            return 'erro'


# Programa Principal

totalAdicional = 0  # Variável que acumula o total dos adicionais
valorTotal = 0  # Variável que guardará o valor total da limpeza

print('-'*30 + ' METRAGEM ' + '-'*30)

# Loop que pergunta a metragem
while True:
    valorMetragem = metragem_limpeza()
    if valorMetragem:
        break
    else:
        continue

print('-'*28 + ' TIPO LIMPEZA ' + '-'*28)
print('B - Básica: Indicada para sujeiras semanais ou quinzenais.')
print('C - Completa: Indicada para sujeiras antigas e/ou não rotineiras.\n')

# Loop que pergunta o tipo da limpeza
while True:
    valorTipo = tipo_limpeza()
    if valorTipo:
        break
    else:
        continue

print('-'*29 + ' ADICIONAIS ' + '-'*29)
print('0 - Não desejo mais nada (Finalizar)')
print('1 - Passar 10 peças de roupa       - R$ 10,00')
print('2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00')
print('3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00\n')

# Loop que pergunta se deseja mais algum adicional
while True:
    valorAdicional = adicional_limpeza()
    if valorAdicional == 0:
        break
    elif valorAdicional == 'erro':
        continue
    else:
        totalAdicional += valorAdicional
        continue

# Cálculo do valor total
valorTotal = (valorMetragem * valorTipo) + valorAdicional

# Exibe o valor total e o valor individual de cada etapa
print('-'*31 + ' RESUMO ' + '-'*31)
print('Total: R${:.2f} (Metragem: R${:.2f} * Tipo: {:.2f} + Adicional: R${:.2f})'
      .format(valorTotal, valorMetragem, valorTipo, totalAdicional))
print('-'*70)
