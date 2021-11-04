from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido
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


@pytest.mark.parametrize(
    'remetente',
    ['', 'clajomar.com']
)
def teste_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'alessandramarmiroli@gmail.com',
            'Cursos PythonPro',
            'Primeira Turma'
        )
