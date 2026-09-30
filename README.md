# 1. Na pasta do seu projeto, crie o ambiente virtual (vamos chamá-lo de 'venv')
python -m venv venv

# 2. Ative o ambiente virtual
source venv/bin/activate

# 3. Com o ambiente ativo, instale o pytest
pip install pytest

# 4. Rode seus testes normalmente
pytest test_calculadora.py -v
