# Inicialização
alunos = {}  # Dicionário para armazenar informações dos alunos

import os  # Biblioteca usada para manipulação de arquivos, como exclusão

print("Gerenciador Escolar")  # Exibe o título do programa

# Exibe o menu de opções para o usuário
print("Menu de opçoes")
opcao = input("Criar turma [1] \nAcessar uma turma [2] \nExcluir uma turma [3]\n")  # Solicita a escolha do usuário

# Match para verificar qual opção o usuário escolheu
match opcao:
    case '1':  # Se o usuário escolheu criar uma turma
        print("Criando turma...")
        turma = input("Qual turma você deseja criar?\n")  # Solicita o nome da turma
        arquivo_txt = (turma + ".txt")  # Cria o nome do arquivo baseado no nome da turma
        with open(arquivo_txt, 'w') as arquivo:  # Abre o arquivo da turma em modo de escrita ('w')
            print(f"turma {turma} criada.")  # Exibe a mensagem de confirmação para o usuário
                               
    case '2':  # Se o usuário escolheu acessar uma turma existente
        acesso_turma = input("Qual turma você deseja acessar?\n")  # Solicita o nome da turma a ser acessada
        arquivo1_txt = (acesso_turma + ".txt")  # Nome do arquivo da turma
        print(f"Acessando turma {acesso_turma}...")  # Exibe a mensagem de acesso
        print(f"Turma {acesso_turma} acessada.")  # Confirma o acesso à turma
        
        # Loop para interagir com o usuário dentro do menu da turma
        while True:
            opc = input("Exibir dados da turma [1] \nAdicionar Aluno [2] \nEditar notas [3] \nSair [5]\n")  # Menu de opções dentro da turma
            match opc:
                case '1':  # Se o usuário escolheu exibir os dados da turma
                    print("Exibindo dados da turma...")
                    with open(arquivo1_txt, 'r', encoding='utf-8') as arquivo:  # Abre o arquivo da turma em modo de leitura ('r')
                        conteudo = arquivo.read()  # Lê o conteúdo do arquivo
                        print(conteudo)  # Exibe o conteúdo do arquivo para o usuário
                    
                case '2':  # Se o usuário escolheu adicionar um aluno
                    print("Adicionando aluno...")
                    nome_aluno = input("Digite o nome do aluno:\n")  # Solicita o nome do aluno
                    notas = input("Digite as notas separadas por espaço (ex: 8.0 7.5 9.0):\n").split()  # Solicita as notas do aluno separadas por espaço
                    notas = [float(nota) for nota in notas]  # Converte as notas de string para float
                    media = sum(notas) / len(notas)  # Calcula a média das notas

                    # Adiciona o aluno e suas notas ao dicionário
                    alunos[nome_aluno] = {'notas': notas, 'média': media}

                    # Abre o arquivo da turma em modo de adicionar ('a')
                    with open(arquivo1_txt, 'a', encoding='utf-8') as arquivo:
                        arquivo.write(f"\nAluno: {nome_aluno}, Notas: {notas}, Média: {media:.2f}\n")  # Escreve o aluno e suas notas no arquivo
                    
                case '3':  # Se o usuário escolheu editar as notas de um aluno
                    print('Editando notas')

                    # Abre o arquivo da turma em modo de leitura ('r')
                    with open(arquivo1_txt, 'r', encoding='utf-8') as arquivo:
                        conteudo = arquivo.readlines()  # Lê todas as linhas do arquivo

                    alunos = {}  # Limpa o dicionário de alunos
                    # Processa cada linha do arquivo para reconstruir o dicionário de alunos
                    for linha in conteudo:
                        if "Aluno:" in linha:  # Verifica se a linha contém informações de um aluno
                            partes = linha.split(',')  # Divide a linha em partes usando vírgula como separador
                            nome_aluno = partes[0].split(': ')[1]  # Extrai o nome do aluno
                            notas_str = partes[1].split(': ')[1].strip().strip('[]')  # Extrai as notas em string e remove colchetes
                            
                            # Converte as notas de string para float
                            notas = []
                            for nota in notas_str.split():
                                notas.append(float(nota))  # Adiciona as notas convertidas à lista
                            
                            media = sum(notas) / len(notas) if notas else 0  # Calcula a média das notas
                            alunos[nome_aluno] = {'notas': notas, 'média': media}  # Adiciona o aluno ao dicionário

                    aluno_para_editar = input("Digite o nome do aluno que você deseja editar as notas:\n")  # Solicita o nome do aluno a ser editado

                    if aluno_para_editar in alunos:  # Verifica se o aluno existe no dicionário
                        novas_notas_str = input("Digite as novas notas separadas por espaço (ex: 8.0 7.5 9.0):\n").split()  # Solicita as novas notas
                        novas_notas = [float(nota) for nota in novas_notas_str]  # Converte as novas notas de string para float
                        
                        media_nova = sum(novas_notas) / len(novas_notas) if novas_notas else 0  # Calcula a nova média

                        # Atualiza as informações do aluno no dicionário
                        alunos[aluno_para_editar]['notas'] = novas_notas
                        alunos[aluno_para_editar]['média'] = media_nova

                        # Reescreve todo o arquivo com as novas informações dos alunos
                        with open(arquivo1_txt, 'w', encoding='utf-8') as arquivo:
                            for aluno, dados in alunos.items():
                                arquivo.write(f"Aluno: {aluno}, Notas: {dados['notas']}, Média: {dados['média']:.2f}\n")

                        print(f"As notas do aluno {aluno_para_editar} foram atualizadas.")
                    else:
                        print("Aluno não encontrado.")  # Exibe mensagem de erro se o aluno não for encontrado
                    
                case '4':  # Se o usuário escolheu excluir um aluno
                    print('Excluindo aluno...')
                    with open(arquivo1_txt, 'r', encoding='utf-8') as arquivo:  # Abre o arquivo da turma em modo de leitura ('r')
                        conteudo = arquivo.readlines()  # Lê todas as linhas do arquivo

                    alunos = {}  # Limpa o dicionário de alunos
                    # Processa cada linha do arquivo para reconstruir o dicionário de alunos
                    for linha in conteudo:
                        if "Aluno:" in linha:  # Verifica se a linha contém informações de um aluno
                            partes = linha.split(',')
                            nome_aluno = partes[0].split(': ')[1]  # Extrai o nome do aluno
                            notas_str = partes[1].split(': ')[1].strip().strip('[]')  # Extrai as notas em string e remove colchetes
                            
                            # Converte as notas de string para float
                            notas = []
                            for nota in notas_str.split():
                                notas.append(float(nota))  # Adiciona as notas convertidas à lista
                            
                            media = sum(notas) / len(notas) if notas else 0  # Calcula a média das notas
                            alunos[nome_aluno] = {'notas': notas, 'média': media}  # Adiciona o aluno ao dicionário

                    excluir = input("Digite o nome do aluno que você deseja excluir:\n")  # Solicita o nome do aluno a ser excluído

                    if excluir in alunos:  # Verifica se o aluno existe no dicionário
                        del alunos[excluir]  # Remove o aluno do dicionário
                        print(f"O aluno {excluir} foi excluído.")  # Exibe mensagem de confirmação
                        
                        # Reescreve o arquivo sem o aluno excluído
                        with open(arquivo1_txt, 'w', encoding='utf-8') as arquivo:
                            for aluno, dados in alunos.items():
                                arquivo.write(f"Aluno: {aluno}, Notas: {dados['notas']}, Média: {dados['média']:.2f}\n")
                    else:
                        print("Aluno não encontrado.")  # Exibe mensagem de erro se o aluno não for encontrado

                                    
                case '5':  # Se o usuário escolheu sair do menu da turma
                    print("Programa finalizado!")  # Exibe mensagem de encerramento
                    break  # Encerra o loop do menu
                
                case x if x != 1 and '2' and '3' and '4':  # Verifica se o usuário inseriu uma opção inválida
                    print("Opcao invalida")  # Exibe mensagem de erro
                
            
    case '3':  # Se o usuário escolheu excluir uma turma
        turma = input('Qual turma você deseja excluir? ')  # Solicita o nome da turma a ser excluída
        print("excluindo turma...")
        arquivo_txt = (turma + '.txt')  # Cria o nome do arquivo da turma a ser excluído
        os.remove(arquivo_txt)  # Remove o arquivo da turma
        print("Turma excluida com sucesso!")  # Exibe mensagem de confirmação

    case x if x != '1' and '2' and '3':  # Verifica se o usuário inseriu uma opção inválida no menu principal
        print("Valor inválido!")  # Exibe mensagem de erro
