def calcular_combustivel(preco_alcool: float, preco_gasolina: float) -> str:
    if preco_alcool / preco_gasolina < 0.7:
        return "Álcool é mais vantajoso"
    else:
        return "Gasolina é mais vantajosa"
    
def calcular_custo_viagem(distancia: float, consumo: float, preco_combustivel: float, pedagio: float = 0.0) -> float:
    custo_combustivel = (distancia / consumo) * preco_combustivel
    custo_total = custo_combustivel + pedagio
    return custo_total

