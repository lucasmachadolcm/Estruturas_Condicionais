def calcular_reajuste(salario_atual):
    if salario_atual <= 280:
        percentual_aumento = 20
    elif 280 < salario_atual <= 700:
        percentual_aumento = 15
    elif 700 < salario_atual <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    aumento = salario_atual * (percentual_aumento / 100)
    novo_salario = salario_atual + aumento
    inflacao = 3.8 / 100
    aumento_real = aumento - (novo_salario * inflacao)

    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")
    print(f"Valor do aumento real, descontado a inflação: R$ {aumento_real:.2f}")

# Entrada do usuário
salario = float(input("Digite o salário atual do colaborador: R$ "))
calcular_reajuste(salario)
