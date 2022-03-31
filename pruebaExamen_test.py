import pytest
from PruebaExamen import PruebaExamen

def test_nombre():
    pe = PruebaExamen('Adan', 'Aguilar')
    assert pe.nombre == "Adan"

def test_apellidoAccess():
    pe = PruebaExamen('Adan', 'Aguilar')
    with pytest.raises(AttributeError):
        pe.__apellido

def test_nombreConcatenado():
    pe = PruebaExamen('Adan', 'Aguilar')
    assert pe.__str__() == "Adan Aguilar"
