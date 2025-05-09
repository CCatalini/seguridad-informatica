from rsa_core import generate_keys, encrypt, decrypt, decrypt_crt

# Parámetros dados en el informe
p = 11
q = 17
e = 59
message = 123

# Generación de claves
n, e, d = generate_keys(p, q, e)
print(f"Clave pública: (n={n}, e={e})")
print(f"Clave privada: d={d}")

# Cifrado
ciphertext = encrypt(message, e, n)
print(f"Mensaje cifrado: {ciphertext}")

# Descifrado estándar
recovered = decrypt(ciphertext, d, n)
print(f"Mensaje recuperado (descifrado): {recovered}")

# Descifrado con CRT
recovered_crt = decrypt_crt(ciphertext, d, p, q)
print(f"Mensaje recuperado (CRT): {recovered_crt}")
