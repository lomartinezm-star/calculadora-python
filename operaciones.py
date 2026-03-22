"""Operaciones de la calculadora"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por 0"
    return a / b

def potencia(base, exp=2):
    return base ** exp

def raiz(n):
    if n < 0:
        return "Error"
    return n ** 0.5