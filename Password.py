import random
import string
import time

senhas = []  

print("GERADOR DE SENHAS SEGURAS PARA VOCÊ USAR NA SUAS CONTAS...\n")
time.sleep(1)

while True:

    print("|     GERADOR DE SENHA      |\n"
          "|---------------------------|\n"
          "|     [1] CRIAR SENHA       |\n"
          "|   [2] VISUALIZAR SENHAS   |\n"
          "|        [3] SAIR           |\n")
    
    try:
        opcao = int(input("DIGITE UMA OPÇÃO: "))
        if opcao != 1 and opcao != 2 and opcao != 3:
            print("DIGITE OPÇÃO 1, 2 OU 3")
            time.sleep(1)
        
        if opcao == 1:

            repeticao = int(input("quantas senhas deseja: "))

            for i in range(repeticao):

                def gerar_senha():
                    comprimento = int(input("Quantos caracteres sua senha vai ter? "))
                    time.sleep(1)

                    caracteres = string.ascii_letters + string.digits + string.punctuation
                    senha = [] 

                    for i in range(comprimento):
                        caractere = random.choice(caracteres)
                        senha.append(caractere)

                    return ''.join(senha)

                salvo = gerar_senha()
                senhas.append(salvo)  
                print("Sua senha é:", salvo)

        elif opcao == 2:
            if senhas == []:
                print("não tem senhas")
            else:
                print("Suas senhas são:\n")
                print(senhas)
            

        elif opcao == 3:
            print("Saindo...")
            break
    except:
        print("Digite uma opção valida")
        time.sleep(1)