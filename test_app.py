from app import app

def test_hello():
    cliente = app.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200
    assert b"Hola desde Docker" in respuesta.data

