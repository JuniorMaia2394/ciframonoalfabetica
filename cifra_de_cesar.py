# Universidade Estadual do Rio Grande do Norte - UERN
# Curso de Ciências da Computação
# Algoritmo de criptografia - Cifra de cesar
# Alunos: Matheus Diogenes e Francisco Clementino

import sys
ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
ROT = 13

# Esta função é usada para cifrar/decifrar mensagem. 
# Parâmetros: 1° Mensagem para cifrar/decifrar
#             2° Deslocamento - 1 para cifrar || -1 para decifrar
def cipher(message, dir):
    m = ''
    for c in message:
        if c in ALFABETO:
            c_index = ALFABETO.index(c)
            m += ALFABETO[(c_index + (dir * ROT)) % len(ALFABETO)]
        else:
            m += c
    return m

# Chamada quando passa o argumento 'encrypt' via terminal
def encrypt(message):
    return cipher(message, 1)

# Chamada quando passa o argumento 'decrypt' via terminal
def decrypt(message):
    return cipher(message, -1)


def main():
    # Pegar os argumentos da linha de comando
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()

    if command == 'encrypt':
        print(encrypt(message))
    elif command == 'decrypt':
        print(decrypt(message))
    else:
        print(command + ': comando não econtrado')

if __name__ == '__main__':
    main()