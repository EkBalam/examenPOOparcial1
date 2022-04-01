from Cuenta import Cuenta

def test_titular():
    c = Cuenta('Juan', 300.0)
    assert c.titular == 'Juan'

def test_monto():
    c = Cuenta('Juan', 300.0)
    assert c.cantidad == 300.0

def test_string():
    c = Cuenta('Juan', 300.0)
    assert c.__str__() == 'Titular de la cuenta: Juan. Cantidad: 300.0'