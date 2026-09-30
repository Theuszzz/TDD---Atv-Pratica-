import pytest
from calculadora import calcular_desconto


class TestCalcularDesconto:
    """Testes para a função calcular_desconto seguindo TDD."""

    def test_desconto_10_porcento(self):
        """Desconto de 10%: valor = 100; desconto = 10; resultado esperado = 90"""
        assert calcular_desconto(100, 10) == 90

    def test_desconto_20_porcento(self):
        """Desconto de 20%: valor = 250; desconto = 20; resultado esperado = 200"""
        assert calcular_desconto(250, 20) == 200

    def test_sem_desconto(self):
        """Sem desconto: valor = 150; desconto = 0; resultado esperado = 150"""
        assert calcular_desconto(150, 0) == 150

    def test_desconto_100_porcento(self):
        """Desconto de 100%: valor = 80; desconto = 100; resultado esperado = 0"""
        assert calcular_desconto(80, 100) == 0

    def test_valor_negativo_deve_lancar_excecao(self):
        """Valor negativo deve lançar ValueError"""
        with pytest.raises(ValueError, match="Valor não pode ser negativo"):
            calcular_desconto(-100, 10)

    def test_desconto_superior_100_deve_lancar_excecao(self):
        """Desconto superior a 100% deve lançar ValueError"""
        with pytest.raises(ValueError, match="Desconto não pode ser superior a 100%"):
            calcular_desconto(100, 150)

    def test_desconto_negativo_deve_lancar_excecao(self):
        """Desconto negativo deve lançar ValueError"""
        with pytest.raises(ValueError, match="Desconto não pode ser negativo"):
            calcular_desconto(100, -10)
