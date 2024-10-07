# Inicialização
alunos = {}  # Dicionário para armazenar informações dos alunos
caminho_pasta = 'turma'
import time
import os
import pygame

pygame.mixer.init()

# Carregar a música (substitua pelo caminho correto do seu arquivo de música)
print("Escolha uma música para tocar enquanto trabalha")
musica = input("Digite um número de 1 a 3 para ouvir uma música enquanto trabalha!")

match musica:
    case '1':
         pygame.mixer.music.load("musica_de_elevador.mp3")
    case '2': 
        pygame.mixer.music.load("Canon_in_D.mp3")
    case '3': 
        pygame.mixer.music.load("The_Way_Home.mp3")
    case '4': 
        pygame.mixer.music.load("musica_do_mine.mp3")
    case x if x != '1' and '2' and '3':
        print('Valor inserido inválido')


pygame.mixer.music.play(-1)  # -1 para repetir a música indefinidamente

print("\n##Gerenciador Escolar##\n")

print("  *Menu de opçoes*\n")
print(" - Criar turma       [1] \n - Acessar uma turma [2] \n - Excluir uma turma [3]\n")

if os.path.exists(caminho_pasta): #printa turmas existentes caso exista alguma
    arquivos = os.listdir(caminho_pasta)
    if arquivos:
        print('Turmas existentes:')
        for arquivo in arquivos:
            print(f'-{arquivo}')
    else:
        print("Nenhuma turma existente")

opcao = input()

match opcao:
    case '1': #para criar uma turma
        print("Criando turma...")
        turma = input("Qual turma você deseja criar?\n")
        pasta_turmas = "turma"
        if not os.path.exists(pasta_turmas):
            os.makedirs(pasta_turmas)
        arquivo_txt  = os.path.join(turma + ".txt")
        if os.path.exists(arquivo_txt):
            print("Esta turma já existe")
        else:
            with open (pasta_turmas + '/' + arquivo_txt , 'w', encoding='utf-8') as arquivo:
                print(f"turma {turma} criada.") #cria a turma caso exista
                                
    case '2': #para acessar turma 
        
        acesso_turma = input("Qual turma você deseja acessar?\n")
        arquivo1_txt = ('turma/' + acesso_turma + ".txt")
        print(f"Acessando turma {acesso_turma}...\n")
        time.sleep(2)

        if os.path.exists(arquivo1_txt):
            print(f"*Turma {acesso_turma} acessada.*\n")
            print("O que deseja fazer?\n")
            while True:
                opc = input("\nExibir dados da turma [1] \nAdicionar Aluno [2] \nEditar notas [3] \nExcluir Aluno [4] \nSair [5]\n")
                match opc:
                    case '1':
                        print("Exibindo dados da turma...")
                        time.sleep(1)
                        with open (arquivo1_txt , 'r', encoding='utf-8') as arquivo:
                            conteudo = arquivo.read()
                            print(conteudo)
                        
                    case '2':
                        print("Adicionando aluno...")
                        time.sleep(1)
                        nome_aluno = input("Digite o nome do aluno:\n")
                        notas = input("Digite as notas separadas por espaço (ex: 8.0 7.5 9.0):\n").split()
                        notas = [float(nota) for nota in notas]  # Converte as notas para float
                        media = sum(notas) / len(notas)

                        # Adiciona o aluno ao dicionário
                        alunos[nome_aluno] = {'notas': notas, 'média': media}

                        # Escreve o aluno e suas informações no arquivo
                        with open(arquivo1_txt, 'a', encoding='utf-8') as arquivo:
                            arquivo.write(f"\nAluno: {nome_aluno}, Notas: {notas}, Média: {media:.2f}\n")
                        
                    case '3':  # Editar notas
                        print('Editando notas...')
                        time.sleep(1)

                        with open(arquivo1_txt, 'r', encoding='utf-8') as arquivo:
                            conteudo = arquivo.readlines()  # Lê todas as linhas do arquivo

                        aluno_para_editar = input("Digite o nome do aluno que você deseja editar as notas:\n")

                        # Verifica se o aluno existe
                        aluno_existe = any(aluno_para_editar in linha for linha in conteudo)

                        if aluno_existe:
                            novas_notas_str = input("Digite as novas notas separadas por espaço (ex: 8.0 7.5 9.0):\n").split()
                            novas_notas = [float(nota) for nota in novas_notas_str]  # Converte as notas para float
                            media_nova = sum(novas_notas) / len(novas_notas) if novas_notas else 0  # Calcula a nova média

                            linhas_atualizadas = []

                            for linha in conteudo:
                                if aluno_para_editar in linha:
                                    # Atualiza a linha com as novas notas e média
                                    nova_linha = f"Aluno: {aluno_para_editar}, Notas: {novas_notas}, Média: {media_nova:.2f}\n"
                                    linhas_atualizadas.append(nova_linha)
                                else:
                                    linhas_atualizadas.append(linha)  # Mantém as outras linhas inalteradas

                            with open(arquivo1_txt, 'w', encoding='utf-8') as arquivo:
                                arquivo.writelines(linhas_atualizadas)  # Reescreve o arquivo com as alterações

                            print(f"As notas do aluno {aluno_para_editar} foram atualizadas.")
                        else:
                            print("Aluno não encontrado.")  # Se o aluno não existir, exibe uma mensagem de erro

                                                                                        
                    case '4':
                        print('Excluindo aluno...')
                        time.sleep(1)
                        
                        # Abre o arquivo da turma em modo de leitura
                        with open(arquivo1_txt, 'r', encoding='utf-8') as arquivo:
                            conteudo = arquivo.readlines()  # Lê todas as linhas do arquivo

                        alunos = {}
                        
                        # Processa cada linha do arquivo
                        for linha in conteudo:
                            if "Aluno:" in linha:  # Verifica se a linha contém informações de um aluno
                                partes = linha.split(', Notas: ')
                                nome_aluno = partes[0].split(': ')[1]  # Extrai o nome do aluno
                                notas_str = partes[1].split(', Média: ')[0].strip('[]')  # Extrai as notas corretamente
                                
                                # Converte as notas para uma lista de floats, removendo vírgulas e outros caracteres indesejados
                                notas = [float(nota.strip(',; ')) for nota in notas_str.split()] if notas_str else []  # Remove vírgulas, pontos e espaços
                                media = sum(notas) / len(notas) if notas else 0  # Calcula a média das notas
                                alunos[nome_aluno] = {'notas': notas, 'média': media}  # Armazena as informações do aluno no dicionário

                        excluir = input("Digite o nome do aluno que você deseja excluir:\n")  # Solicita o nome do aluno a ser excluído

                        if excluir in alunos:  # Verifica se o aluno existe no dicionário
                            del alunos[excluir]  # Remove o aluno do dicionário
                            print(f"O aluno {excluir} foi excluído.")  # Exibe mensagem de confirmação

                            # Abre o arquivo da turma em modo de escrita para reescrever as informações
                            with open(arquivo1_txt, 'w', encoding='utf-8') as arquivo:
                                for aluno, dados in alunos.items():
                                    # Reescreve apenas as informações dos alunos que não foram excluídos
                                    arquivo.write(f"Aluno: {aluno}, Notas: {dados['notas']}, Média: {dados['média']:.2f}\n")
                        else:
                            print("Aluno não encontrado.")  # Exibe mensagem de erro se o aluno não for encontrado



                                                                        
                    case '5':
                        print("Progrma finalizado!")
                        break
                    
                    case x if x != 1 and '2' and '3' and '4' and '5':
                        print("Opcao invalida")
                    
        else:
            print("Turma não encontrada!")
    
                    
                
    case '3': #para excluir turma
        turma = input('Qual turma você deseja excluir? ')
        print("excluindo turma...")
        time.sleep(1)
        arquivo = ("turma/" + turma + '.txt')
        os.remove(arquivo)
        print("Turma excluida com sucesso!")

    case x if x != '1' and '2' and '3': #caso nao digite 1, 2 ou 3 print('valor inválido')
        print("Valor inválido!")

