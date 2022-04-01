from CajaAhorro import CajaAhorro

def test_titular():
    c = CajaAhorro('Juan', 300.0)
    assert c.titular == 'Juan'

def test_porcentajeAhorro():
    c = CajaAhorro('Juan', 300.0)
    assert c.porcentajeAhorro(1000) == '30.0%'

def test_string():
    c = CajaAhorro('Juan', 300.0)
    assert c.__str__() == 'Titular de la cuenta: Juan. Cantidad: 300.0'