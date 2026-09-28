from app import app

def test_hello():
    cliente = app.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200
    assert b"Texto que no existe" in respuesta.data
