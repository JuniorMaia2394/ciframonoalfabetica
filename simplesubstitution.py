# Universidade Estadual do Rio Grande do Norte - UERN
# Curso de Ciências da Computação
# Algoritmo de criptografia - Cifra de cesar
# Alunos: Matheus Diogenes e Francisco Clementino


# Esta função é usada para cifrar/decifrar mensagem. 

class SimpleSubstitution:
    def __init__(self):
        self.p_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.decrypting = False
 
    def cipher_alphabet(self, password):
        ''' (str) -> str
        Retorna um alfabeto cifrado iniciado com
        o texto da palavra chave password
        '''
        c_alphabet = []
        password = password.upper()
        for ch in password:
            if ch not in c_alphabet:
                c_alphabet.append(ch)
                idx = self.p_alphabet.find(ch)
        p_alphabet = self.p_alphabet[idx:] + self.p_alphabet[:idx]
        for ch in p_alphabet:
            if ch not in c_alphabet:
                c_alphabet.append(ch)
        return ''.join(c_alphabet)

# metodo encrypt usado para encriptar a mensagem digitada 
    def encrypt(self, plaintext, password):
        '''(str, str) -> str
        Retorna o texto plano cifrado com a cifra de
        substituicao com a palavra chave password
        '''
        txt = ''
        p_alphabet = self.p_alphabet
        text = plaintext.replace(' ', '').upper()
        cipher = self.cipher_alphabet(password)
        if self.decrypting:
            p_alphabet, cipher = cipher, p_alphabet
            self.decrypting = False
        for ch in text:
            txt += cipher[p_alphabet.find(ch)]
        return txt
# metodo encrypt usado para encriptar a mensagem digitada 
    def decrypt(self, ciphertext,  password):
        '''(str, str) -> str
        Retorna o texto cifrado decifrado com a cifra de
        substituicao com a palavra chave password
        '''
        self.decrypting = True
        return self.encrypt(ciphertext, password)


# funçao para encriptar a mensagem
encriptar = SimpleSubstitution().encrypt('mensagem', 'senha')
print(encriptar)

# função para descriptografar a mensagem
descriptografar = SimpleSubstitution().decrypt(encriptar, 'senha')
print(descriptografar)