
import time, os
from os import system


def novoArquivo():
    for ficheiro in os.listdir():
        if ficheiro.endswith('.txt'):
            print("Os ficheiros existentes no diretório:")
            print(ficheiro)
    nomeArquivo = input("Informe o nome do arquivo: ")
    return nomeArquivo


def abrirArquivo():
    try:
        for ficheiro in os.listdir():
            if ficheiro.endswith('.txt'):
                print("Os ficheiros existentes no diretório:")
                print(ficheiro)
        Arquivo = input("Informe o nome do ficheiro: ")
        with open(Arquivo + ".txt", "r") as file:
            print("Arquivo solicitado:")
            print(file.read())
        system("pause")

    except FileNotFoundError:
        print("Ficheiro não existe.")
        time.sleep(5)

    system("cls")
    menu()


def criarArquivo(Arquivo):
    try:
        for ficheiro in os.listdir():
            if ficheiro.endswith('.txt'):
                print("Os ficheiros existentes no diretório:")
                print(ficheiro)
        with open(Arquivo, "x") as file:
            file.write("")
        print("Ficheiro criado.")
        system("pause")
        with open(Arquivo, "w") as file:
            sair = True
            while sair:
                print("Digite (s)im ou (S)im para sair")
                txt = input("Digite o nome desejado: ")
                if (txt == 's') or (txt == 'S'):
                    sair = False
                else:
                    file.write(txt + "\n")

    except FileExistsError:
        print("Ficheiro já existe.")
        time.sleep(5)

    system("cls")
    menu()

def acrescentarDados():
    try:
        for ficheiro in os.listdir():
            if ficheiro.endswith('.txt'):
                print("Os ficheiros existentes no diretório:")
                print(ficheiro)
        Arquivo = input("Informe o nome do ficheiro: ")
        with open(Arquivo + ".txt", "r") as file:
            print(file.read())
        sair = True
        while sair:
            print("Digite (s)im ou (S)im para sair")
            txt = input("Digite o nome desejado: ")
            if (txt == 's') or (txt == 'S'):
                sair = False
            else:
                with open(Arquivo + ".txt", "a") as file:
                    file.write(txt + "\n")
        system("cls")
        with open(Arquivo + ".txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Ficheiro não existe.")
        time.sleep(5)
        system("cls")
        acrescentarDados()

    system("pause")
    system("cls")
    menu()


def eliminarDados():
    try:
        for ficheiro in os.listdir():
            if ficheiro.endswith('.txt'):
                print("Os ficheiros existentes no diretório:")
                print(ficheiro)
        Arquivo = input("Informe o nome do ficheiro: ")
        with open(Arquivo + ".txt", "r") as file:
            print(file.read())
        with open(Arquivo + ".txt", "r") as file:
            txt = file.readlines()
            nome = input("Informe o nome que deseja remover: ")
        with open(Arquivo + ".txt", "r") as file:
            cont = 0
            for x in txt:
                if x == nome + "\n":
                    cont = 1
            if cont == 0:
                print("O valor informado não existe no arquivo.")
                system("pause")
                eliminarDados()
        with open(Arquivo + ".txt", "w") as file:
            for x in txt:
                if x != nome + "\n":
                    file.write(x)
        with open(Arquivo + ".txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Ficheiro não existe.")
        time.sleep(5)
        eliminarDados()
    system("pause")
    system("cls")
    menu()


def menu():
    while True:
        system("cls")
        print("******************************")
        print("Menu de opções de ficheiros:")
        print("[1] Abrir")
        print("[2] Criar")
        print("[3] Acrescentar dados")
        print("[4] Eliminar dados")
        print("[0] Sair")
        print("******************************")
        opcao = int(input("==> "))

        if opcao == 1:
            abrirArquivo()
        elif opcao == 2:
            Arquivo = novoArquivo()
            criarArquivo(Arquivo + ".txt")
        elif opcao == 3:
            acrescentarDados()
        elif opcao == 4:
            eliminarDados()
        elif opcao == 0:
            exit()
        else:
            print("Opção inválida, tente novamente.")
            time.sleep(5)
            menu()


menu()