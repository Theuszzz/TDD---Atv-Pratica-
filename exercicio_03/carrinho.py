class Carrinho:
    """Classe que representa um carrinho de compras."""

    def __init__(self):
        """Cria um carrinho vazio com total inicial 0."""
        self._produtos = []  # Lista de tuplas (nome, preco, quantidade)
        self._desconto = 0   # Percentual de desconto (0 a 100)

    def adicionar_produto(self, nome: str, preco: float, quantidade: int = 1) -> None:
        """
        Adiciona um produto ao carrinho.
        
        Args:
            nome: Nome do produto
            preco: Preço unitário do produto
            quantidade: Quantidade do produto (padrão: 1)
        
        Raises:
            ValueError: Se preço for negativo ou quantidade <= 0
        """
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        
        self._produtos.append((nome, preco, quantidade))

    def aplicar_desconto(self, percentual: float) -> None:
        """
        Aplica um desconto percentual ao total do carrinho.
        
        Args:
            percentual: Percentual de desconto (0 a 100)
        
        Raises:
            ValueError: Se desconto for negativo ou superior a 100%
        """
        if percentual < 0:
            raise ValueError("Desconto não pode ser negativo")
        if percentual > 100:
            raise ValueError("Desconto não pode ser superior a 100%")
        
        self._desconto = percentual

    def calcular_total(self) -> float:
        """
        Calcula o total do carrinho com desconto aplicado.
        
        Returns:
            Valor total após desconto
        """
        subtotal = sum(preco * quantidade for _, preco, quantidade in self._produtos)
        desconto_valor = subtotal * (self._desconto / 100)
        return subtotal - desconto_valor