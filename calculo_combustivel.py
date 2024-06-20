from time import sleep

# Apresentação

print('---'*20)
print ('Olá! Bem vindo ao meu primeiro projeto de programação!')
print('---'*20)
sleep(1)

#Guardando o nome do Usuario

nome = str(input('Qual é o seu nome? ')).strip()

sleep(1)
print (f'Muito prazer em te conhecer \033[0;34m"{nome}"\033[m')
sleep(1)
print ('Agora vou fazer o calculo para saber qual combustivel escolher!')
sleep(1)

# contadores com loop para forçar usuario por corretamente

while True:
    try:
        alcool_str = input('Qual é o valor do litro do Álcool? ').strip()
        alcool_str = alcool_str.replace(',', '.')   # Substitui vírgula por ponto
        alcool = float(alcool_str)                  # Transforma o valor string para decimal
        break                                       # Sai do loop se o valor for válido

        # Se não for possivel converter as string em decimal vai dar o erro:
        
    except ValueError:                              
        print("Valor inválido! Por favor, digite um número válido para o preço do Álcool.")

while True:
    try:
        gasolina_str = input('E qual é o Valor do litro da Gasolina? ').strip()
        gasolina_str = gasolina_str.replace(',', '.')
        gasolina = float(gasolina_str)
        break  
    except ValueError:
        print("Valor inválido! Por favor, digite um número válido para o preço da Gasolina.")
sleep(1)

# Divisão

resultado = alcool / gasolina

sleep(1)
print (f'Vejamos... O alcool \033[0;32mR${alcool}\033[m dividido pelo preço da gasolina \033[0;31mR${gasolina}\033[m é igual a \033[0;33mR${resultado:.2f}\033[m')
sleep(1)

#Verificação de calculo para decisão do combustivel

if resultado <= 0.70:
    print(f'Então {nome} está compensando por \033[0;32mAlcool\033[m')
else:
    print(f'Então {nome} está compensando por \033[0;31mGasolina\033[m')
sleep(1)
print(f'Obrigado por participar \033[0;34m"{nome}"\033[m')
sleep(1)
print('Se desejar continuar posso fazer o calculo da quantidade necessaria para uma viagem!')
sleep(1)

# Loop para forçar a escolha correta aceitando somente 1 letra

escolha = ' '
valor = 0

while True:
    escolha = str(input('Deseja continuar ou posso encerrar o programa S/N?: ')).strip().lower()[0]

    if escolha == 'n':
        break

    elif escolha == 's':
        distancia = float(input('Digite a dinstancia em KM: '))
        KmPorLitro = float(input('Quantos KM seu veiculo faz por litro? '))
        sleep(1)

        litros = distancia / KmPorLitro

        if resultado <= 0.70:
            combustivel = 'Alcool'
            valorComb = alcool

        else:
            combustivel = 'Gasolina'
            valorComb = gasolina

        # Calculo de gasto de litros vezes o preço do combustivel

        valor = litros * valorComb

        #Resultados

        print(f'Você precisa de \033[4;36m{litros:.2f}\033[m litros de \033[4;36m{combustivel}\033[m para percorrer o seu destino')
        sleep(1)

        print(f'Que vai dar um total de \033[4;33mR${valor:.2f}\033[m')
        break
    else:
        print('Escolha errada, por favor digite novamente')
    
    # Encerramento

sleep(1)
print(f'Espero ter ajudado \033[0;34m"{nome}"\033[m, foi um prazer até a proxima!')
sleep(2)
print('Esse programa irá fechar em 5 segundos...')
sleep(5)
print('FIM')