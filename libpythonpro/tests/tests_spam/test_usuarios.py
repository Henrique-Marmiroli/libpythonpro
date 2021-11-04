from spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Henrique', email='lhm.ambiental@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Henrique', email='lhm.ambiental@gmail.com'),
                Usuario(nome='Ale', email='lhm.ambiental@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
