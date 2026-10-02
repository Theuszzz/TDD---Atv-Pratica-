import pytest
from notas import classificar_nota


class TestClassificarNota:
    """Testes para a função classificar_nota seguindo TDD."""

    def test_nota_4_reprovado(self):
        """Nota 4 → Reprovado"""
        assert classificar_nota(4) == "Reprovado"

    def test_nota_5_recuperacao(self):
        """Nota 5 → Recuperação"""
        assert classificar_nota(5) == "Recuperação"

    def test_nota_6_9_recuperacao(self):
        """Nota 6,9 → Recuperação"""
        assert classificar_nota(6.9) == "Recuperação"

    def test_nota_7_aprovado(self):
        """Nota 7 → Aprovado"""
        assert classificar_nota(7) == "Aprovado"

    def test_nota_10_aprovado(self):
        """Nota 10 → Aprovado"""
        assert classificar_nota(10) == "Aprovado"

    def test_nota_negativa_excecao(self):
        """Nota menor que 0 deve lançar ValueError"""
        with pytest.raises(ValueError, match="Nota inválida"):
            classificar_nota(-1)

    def test_nota_maior_que_10_excecao(self):
        """Nota maior que 10 deve lançar ValueError"""
        with pytest.raises(ValueError, match="Nota inválida"):
            classificar_nota(11)

    def test_nota_4_9_reprovado(self):
        """Nota 4,9 → Reprovado (limite superior do Reprovado)"""
        assert classificar_nota(4.9) == "Reprovado"

    def test_nota_6_9_limite_recuperacao(self):
        """Nota 6,9 → Recuperação (limite superior da Recuperação)"""
        assert classificar_nota(6.9) == "Recuperação"

    def test_nota_7_limite_aprovado(self):
        """Nota 7 → Aprovado (limite inferior do Aprovado)"""
        assert classificar_nota(7) == "Aprovado"
