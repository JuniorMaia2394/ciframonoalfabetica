# Importando as classes
from playfair import Playfair
 
# Metodos para encriptografar e descriptografar a mensagem 
cifra = Playfair()
cifrado = cifra.encrypt('mensagem', 'senha')
print(cifrado)
print(cifra.decrypt(cifrado, 'senha'))