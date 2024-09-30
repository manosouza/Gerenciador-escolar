# Inicialização
alunos = {}  # Dicionário para armazenar informações dos alunos

print("Gerenciador Escolar")

print("Menu de opçoes")
opcao = input("Criar turma [1] \nAcessar uma turma [2] \nExcluir uma turma [3]\n")

match opcao:
    case '1':
        print("Criando turma...")
        turma = input("Qual turma você deseja criar?\n")
        arquivo_txt = (turma + ".txt")
        print(f"Acessando turma {turma}...")
        with open (arquivo_txt , 'w') as arquivo:
            arquivo.write(f"turma {turma} criada")
            print(f"turma {turma} criada.")
    case '2':
        acesso_turma = input("Qual turma você deseja acessar?\n")
        arquivo1_txt = (acesso_turma + ".txt")
        print(f"Acessando turma {acesso_turma}...")
        print(f"Turma {acesso_turma} acessada.")
        while True:
            opc = input("Exibir dados da turma [1] \nAdicionar Aluno [2] \nEditar notas [3]\n")
            match opc:
                case '1':
                    print("Exibindo dados da turma...")
                    if not alunos:
                        print("Nenhum aluno cadastrado.")
                    else:
                        for nome, info in alunos.items():
                                notas = info.get('notas', [])
                                media = sum(notas) / len(notas) if notas else 0
                                print(f"Aluno: {nome}, Notas: {notas}, Média: {media:.2f}")
                    
                    
                    
                    with open (arquivo1_txt , 'r') as arquivo:
                        conteudo = arquivo.read()
                        print(conteudo)
                    break
                case '2':
                    print("Adicionando aluno...")
                    break
                case '3':
                    print("Editando notas...")
                    break
                case x if x != 1 and '2' and '3':
                    print("Opcao invalida")
            
            
    case '3':
        print("excluindo turma...")
    case x if x != '1' and '2' and '3':
        print("Valor inválido!")







