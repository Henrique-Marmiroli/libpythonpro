import pytest
from unittest.mock import Mock
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Henrique', email='lhm.ambiental@gmail.com'),
            Usuario(nome='Ale', email='lhm.ambiental@gmail.com')
        ],
        [
            Usuario(nome='Henrique', email='lhm.ambiental@gmail.com')
        ]
    ]
)
def test_qde_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_spam = EnviadorDeSpam(sessao, enviador)
    enviador_spam.enviar_emails(
        'lhm.ambiental@gmail.com',
        'Curso PythonPro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_spam(sessao):
    usuario = Usuario(nome='Henrique', email='lhm.ambiental@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_spam = EnviadorDeSpam(sessao, enviador)
    enviador_spam.enviar_emails(
        'alessandramarmiroli@gmail.com',
        'Curso PythonPro',
        'Confira os módulos'
    )
    enviador.enviar.assert_called_once_with(
        'alessandramarmiroli@gmail.com',
        'lhm.ambiental@gmail.com',
        'Curso PythonPro',
        'Confira os módulos'
    )