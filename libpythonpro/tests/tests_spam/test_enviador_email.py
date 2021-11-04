from libpythonpro.spam.enviador_de_email import Enviador
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['lhm.ambiental@gmail.com', 'clajomar@hotmail.com']
)
def teste_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'alessandramarmiroli@gmail.com',
        'Cursos PythonPro',
        'Primeira Turma'
    )
    assert destinatario in resultado