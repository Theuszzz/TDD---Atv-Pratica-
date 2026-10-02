import pytest
from carrinho import Carrinho


class TestCarrinho:
    """Testes para a classe Carrinho seguindo TDD."""

    def test_carrinho_vazio_total_zero(self):
        """Carrinho vazio → total igual a 0."""
        carrinho = Carrinho()
        assert carrinho.calcular_total() == 0

    def test_um_produto_total_correto(self):
        """Um produto → Mouse de R$ 100 → total igual a R$ 100."""
        carrinho = Carrinho()
        carrinho.adicionar_produto("Mouse", 100)
        assert carrinho.calcular_total() == 100

    def test_dois_produtos_total_soma(self):
        """Dois produtos → Mouse de R$ 100 + Teclado de R$ 150 → total igual a R$ 250."""
        carrinho = Carrinho()
        carrinho.adicionar_produto("Mouse", 100)
        carrinho.adicionar_produto("Teclado", 150)
        assert carrinho.calcular_total() == 250

    def test_produto_com_quantidade(self):
        """Produto com quantidade → Mouse de R$ 100 × 3 → total igual a R$ 300."""
        carrinho = Carrinho()
        carrinho.adicionar_produto("Mouse", 100, 3)
        assert carrinho.calcular_total() == 300

    def test_desconto_percentual(self):
        """Desconto → total de R$ 500 com 10% de desconto → total igual a R$ 450."""
        carrinho = Carrinho()
        carrinho.adicionar_produto("Produto A", 300)
        carrinho.adicionar_produto("Produto B", 200)
        carrinho.aplicar_desconto(10)
        assert carrinho.calcular_total() == 450

    def test_quantidade_zero_excecao(self):
        """Quantidade inválida → quantidade 0 deverá provocar uma exceção."""
        carrinho = Carrinho()
        with pytest.raises(ValueError, match="Quantidade deve ser maior que zero"):
            carrinho.adicionar_produto("Mouse", 100, 0)

    def test_quantidade_negativa_excecao(self):
        """Quantidade negativa deve lançar ValueError."""
        carrinho = Carrinho()
        with pytest.raises(ValueError, match="Quantidade deve ser maior que zero"):
            carrinho.adicionar_produto("Mouse", 100, -1)

    def test_desconto_negativo_excecao(self):
        """Desconto negativo deve lançar ValueError."""
        carrinho = Carrinho()
        carrinho.adicionar_produto("Produto", 100)
        with pytest.raises(ValueError, match="Desconto não pode ser negativo"):
            carrinho.aplicar_desconto(-10)

    def test_desconto_superior_100_excecao(self):
        """Desconto superior a 100% deve lançar ValueError."""
        carrinho = Carrinho()
        carrinho.adicionar_produto("Produto", 100)
        with pytest.raises(ValueError, match="Desconto não pode ser superior a 100%"):
            carrinho.aplicar_desconto(150)

    def test_preco_negativo_excecao(self):
        """Preço negativo deve lançar ValueError."""
        carrinho = Carrinho()
        with pytest.raises(ValueError, match="Preço não pode ser negativo"):
            carrinho.adicionar_produto("Mouse", -100)

    def test_adicionar_varios_produtos_com_quantidades(self):
        """Adicionar vários produtos com quantidades diferentes."""
        carrinho = Carrinho()
        carrinho.adicionar_produto("Mouse", 100, 2)
        carrinho.adicionar_produto("Teclado", 150, 1)
        carrinho.adicionar_produto("Monitor", 800, 1)
        assert carrinho.calcular_total() == 1150

    def test_aplicar_desconto_multiplas_vezes(self):
        """Aplicar desconto múltiplas vezes deve acumular ou substituir?"""
        carrinho = Carrinho()
        carrinho.adicionar_produto("Produto", 1000)
        carrinho.aplicar_desconto(10)  # 900
        carrinho.aplicar_desconto(10)  # 810 (se acumular) ou 900 (se substituir)
        # O comportamento esperado: substituir o desconto anterior
        assert carrinho.calcular_total() == 900
