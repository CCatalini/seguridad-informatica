from rsa_utils import mod_inverse, fast_exp


# Genera las claves RSA a partir de dos primos p y q, y un exponente e
# Devuelve n, e (clave pública) y d (clave privada)
def generate_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return n, e, d


# Cifra el mensaje usando la clave pública (e, n)
def encrypt(message, e, n):
    return fast_exp(message, e, n)


# Descifra el mensaje cifrado usando la clave privada d
def decrypt(ciphertext, d, n):
    return fast_exp(ciphertext, d, n)


# Descifra usando el Teorema de los Restos Chinos (CRT) para mayor eficiencia
# Solo posible si se conoce la factorización de n = p * q
def decrypt_crt(ciphertext, d, p, q):
    dp = d % (p - 1)  # Exponente reducido mod p-1
    dq = d % (q - 1)  # Exponente reducido mod q-1
    q_inv = mod_inverse(q, p)  # Inversa modular de q mod p

    # Se descifra por separado mod p y mod q
    m1 = fast_exp(ciphertext, dp, p)
    m2 = fast_exp(ciphertext, dq, q)

    # Combinamos los resultados con el CRT
    h = (q_inv * (m1 - m2)) % p
    return (m2 + h * q) % (p * q)