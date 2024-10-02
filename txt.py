#open ('caminho', 'r')
# r = leitura
# a = append
# w = escrita/mas apaga tudo
# x = criar arquivo
# r+ = leitura + escrita

arquivo = 'aula13.py/frutas.txt'

arquivo = open(arquivo,'r')
linha = arquivo.readline()
while linha:
    linhavazia = linha.strip()
    print(linhavazia)
    linha = arquivo.readline()
arquivo.close