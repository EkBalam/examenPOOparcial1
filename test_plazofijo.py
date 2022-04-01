from PlazoFijo import PlazoFijo

def test_titular():
    c = PlazoFijo('Juan', 300.0, '1mes', 0.15)
    assert c.titular == 'Juan'

def test_obtener_importe_interes():
    c = PlazoFijo('Juan', 300.0, '1mes', 0.15)
    assert c.obtener_importe_interes() == 45

def test_string():
    c = PlazoFijo('Juan', 300.0, '1mes', 0.15)
    assert c.__str__() == 'Titular: Juan. Plazo: 1mes. Interés: 0.15. Total de interés: 45.0'
