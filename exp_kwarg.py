# Salvar variáveis em um arquivo separado por nomes
def salvar_variaveis(arquivo, **kwargs):
    with open(arquivo, 'w') as f:
        for nome, valor in kwargs.items():
            f.write(f"{nome}: {valor}\n")

# Carregar variáveis de um arquivo
def carregar_variaveis(arquivo):
    variaveis = {}
    with open(arquivo, 'r') as f:
        for line in f:
            nome, valor = line.strip().split(': ')
            variaveis[nome] = valor
    return variaveis

# Exemplo de uso
nome = "Alice"
idade = 30
cidade = "Rio de Janeiro"

# Salvar as variáveis em um arquivo chamado "variaveis.txt"
salvar_variaveis('variaveis.txt', nome=nome, idade=idade, cidade=cidade)

# Carregar as variáveis de volta do arquivo
variaveis_carregadas = carregar_variaveis('variaveis.txt')

print(variaveis_carregadas)  # Saída: {'nome': 'Alice', 'idade': '30', 'cidade': 'Rio de Janeiro'}


#Este exemplo salva as variáveis nome, idade e cidade em um arquivo chamado "variaveis.txt", onde cada variável é identificada pelo seu nome e associada ao seu valor. Depois, as variáveis são carregadas de volta do arquivo.

