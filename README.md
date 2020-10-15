# Algoritmos de Criptografia
[...]
## Execução dos Algoritmos

#### Cifra de Cesar
1. Abra o  Terminal/Bash
2. Entre no diretório **cifras**
3. Para __cifrar__ dê o seguinte comando:
> python cifra_de_cesar.py encrypt "Sua menssagem"
4. Para __decifrar__ dê o seguinte comando:
> python cifra_de_cesar.py decrypt "Menssagem Criptografada"

#### Cifra de Tranposição
1. Abra o  Terminal/Bash
2. Entre no diretório **cifras**
3. Para __cifrar__ dê o seguinte comando:
> python transposicao.py -c "mensagem" 12
* Caso a palavra ou texto possua um número de caracteres não divisível pelo tamanho da chave, espaços vazios serão adicionados para compor a matriz de colunas.
4. Para __decifrar__ dê o seguinte comando:
> python transposicao.py -d "msg_cifrada" 12
* A entrada (texto_cifrado) para decifrar precisa ter um número divisível de caracteres pelo tamanho da chave.

## Créditos
Cifra de Cesar - Baseado [nesse repositorio](https://github.com/radAragon/algoritmo_transposicao).
Cifra de Transposição - Baseado [nesse repositorio](https://github.com/guilhermeRey/yarquen).
