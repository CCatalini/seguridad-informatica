
# Algoritmo extendido de Euclides: calcula los coeficientes x-y; y el MCD de a y b
# Sirve para la inversa modular
def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, d = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y, d


# Calcula la inversa modular de e módulo phi
# Es decir, busca un número d tal que (e * d) ≡ 1 (mod phi)
def mod_inverse(e, phi):
    x, _, gcd = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("No existe inversa modular")
    return x % phi


# Exponenciación rápida (modular): calcula base^exp mod mod
# Es eficiente incluso para exponentes grandes
def fast_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result
