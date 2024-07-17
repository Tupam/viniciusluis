# Usuario tem uma parede para revetir com placas em 3D, 
# Objetivo do aplicativo é saber a quantidade necessaria para revetir a parede

from time import sleep

def linha():
    print('-='*20)

def caculo(altura, largura):
    return altura * largura

def obter_valor(descricao):
    while True:
        try:
            valor_str = input(f"{descricao}: ").strip()
            valor_str = valor_str.replace(',', '.')
            valor = float(valor_str)
            return valor
        except ValueError:
            print(f"Valor incorreto! Por favor, digite um número válido para {descricao}.")
linha()

altura_placa = obter_valor("Qual a altura da placa")
largura_placa = obter_valor("Qual a largura da placa")

linha()

while True:
    resp = input(f'A placa tem as dimenções {altura_placa}X{largura_placa} correto? [S/N] ').strip().upper()[0]
    if resp in 'S':
        break
    elif resp != 'N':
        print('Resposta errada digite S ou N para processeguir!')
        sleep(2)    
linha()

sleep(1)
print('Agora preciso das medidas da parede')

altura_parede = obter_valor("Qual a altura da parede")
largura_parede = obter_valor("Qual a largura da parede")

linha()

area_parede = caculo(altura_parede, largura_parede)
area_placa = caculo(altura_placa, largura_placa)
quantidade_minima_placa = area_parede / area_placa

print(f'Para revestir uma parede de {area_parede:.2f}m² com placas de {area_placa:.2f}m², é preciso comprar no minimo {quantidade_minima_placa:.0f}m².')
print(f'Observação: Bom comprar quantidade a mais para alguns casos de acabamento.')
linha()
print('FIM!')