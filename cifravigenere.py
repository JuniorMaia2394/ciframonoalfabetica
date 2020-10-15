# Universidade Estadual do Rio Grande do Norte - UERN
# Curso de Ciências da Computação
# Algoritmo de criptografia - Cifra de cesar
# Alunos: Matheus Diogenes e Francisco Clementino

# Esta função é usada para cifrar/decifrar mensagem.

# Alfabeto usado para a cifra de vigenere
alfabeto="\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_` "

# Metodo para cifrar a letra
def cifraLetra(letra, chave):
    l = alfabeto.index(letra.upper())
    c = alfabeto.index(chave.upper())
    return alfabeto[(l+c) % len(alfabeto)]

# Metodo para decifrar a letra
def decifraLetra(letra, chave):
    l = alfabeto.index(letra.upper())
    c = alfabeto.index(chave.upper())
    return alfabeto[(l-c) % len(alfabeto)]

# Metodo para cifrar o texto
def cifraTexto(text, key):
    fechado = ""
    for i, c in enumerate(key):
        cf = cifraLetra(text[i], c)
        fechado += cf

    for i, c in enumerate(text[len(key):]):
        cf = cifraLetra(c, text[i])
        fechado += cf

    return fechado
    
# Metodo para decifrar o texto
def decifraTexto(text, key):
    aberto = ""
    for i, c in enumerate(key):
        ca = decifraLetra(text[i], c)
        aberto += ca

    for i, c in enumerate(text[len(key):]):
        ca = decifraLetra(c, aberto[i])
        aberto += ca
    return aberto

# Chama a função para cifrar o texto ou palavra
cifrar = cifraTexto('teste', '123')
print(cifrar)

# Chama a função para decifrar o texto ou palavra
decifrar = decifraTexto(cifrar, '123')
print(decifrar)