def classificar_nota(nota: float) -> str:
    """
    Classifica uma nota de 0 a 10.
    
    Args:
        nota: Nota entre 0 e 10
    
    Returns:
        Classificação: "Reprovado", "Recuperação" ou "Aprovado"
    
    Raises:
        ValueError: Se nota for menor que 0 ou maior que 10
    """
    if nota < 0 or nota > 10:
        raise ValueError("Nota inválida: deve estar entre 0 e 10")
    
    if nota < 5:
        return "Reprovado"
    elif nota < 7:
        return "Recuperação"
    else:
        return "Aprovado"