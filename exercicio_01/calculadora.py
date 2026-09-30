def calcular_desconto(valor: float, percentual: float) -> float:
    """
    Calcula o valor final de um produto após aplicação de desconto.
    
    Args:
        valor: Valor original do produto
        percentual: Percentual de desconto (0 a 100)
    
    Returns:
        Valor final após o desconto
    
    Raises:
        ValueError: Se valor for negativo, desconto for negativo ou superior a 100%
    """
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")
    if percentual < 0:
        raise ValueError("Desconto não pode ser negativo")
    if percentual > 100:
        raise ValueError("Desconto não pode ser superior a 100%")
    
    desconto = valor * (percentual / 100)
    return valor - desconto