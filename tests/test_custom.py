import pytest

from solution_python import EventSourcer

def test_multiply():
    sourcer = EventSourcer()

    sourcer.add(2)
    sourcer.multiply(2)
    
    assert sourcer.value == 4

def test_multiply_0():
    sourcer = EventSourcer()

    sourcer.multiply(2)
    
    assert sourcer.value == 0

def test_divide_odd():
    sourcer = EventSourcer()

    sourcer.add(5)
    sourcer.divide(2)
    
    assert sourcer.value == 2

def test_divide_even():
    sourcer = EventSourcer()

    sourcer.add(6)
    sourcer.divide(2)
    
    assert sourcer.value == 3

def test_divide_big_divisor():
    sourcer = EventSourcer()

    sourcer.add(2)
    sourcer.divide(3)
    
    assert sourcer.value == 0

def test_pow():
    sourcer = EventSourcer()

    sourcer.add(2)
    sourcer.pow(3)
    
    assert sourcer.value == 8

def test_pow_float():
    sourcer = EventSourcer()

    sourcer.add(4)
    sourcer.pow(0.5)
    
    assert sourcer.value == 2
    assert isinstance(sourcer.value, int)
