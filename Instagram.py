import numpy as np
import pandas as pd
import pymysql
import string
from datetime import datetime

data_hora = datetime.today()

conexao = pymysql.connect(
    host= 'localhost',
    user= 'root',
    passwd= '',
    database= 'insta'
)
cursor = conexao.cursor()

#-----------Funções Para funcionamento do codigo--------------

def login(): #função para login
    global user
    global senha
    global result
    global resultado

    print("Digite seu email ou nome de usario")
    user = str(input())
    #-----------fazendo busca do user no bd-------------------------
    cursor.execute("SELECT idUsuario FROM perfil WHERE idUsuario = %s", (user))
    resultado = cursor.fetchone()
    if resultado == None:
        print("Usuario não Cadastrado\n"
              "Faça seu Cadastro: ")
        cadastro()


    print("Digite sua senha")
    senha = str(input())
    cursor.execute("SELECT senha FROM perfil WHERE senha = %s", (senha))
    result = cursor.fetchone()
    if result == None:
        print("Senha incorreta\n")
        login()
    else:
        main()


def cadastro(): #função para cadastro
    global user
    global email
    global nome
    global senha

    print("digite um email");
    email = str(input());
    print("digite seu nome completo");
    nome = str(input());
    print("digite um nome de usuario");
    user = str(input());
    print("digite uma senha");
    senha = str(input());
    com_sql = "INSERT INTO perfil(idUsuario, email, nomeReal, senha) VALUES(%s,%s,%s,%s)"
    valor = (user, email, nome, senha)
    cursor.execute(com_sql, valor)
    conexao.commit()
    print(cursor.rowcount, "Inserido com sucesso")
    login()


def pesquisa():
    global pesq
    global userPesq
    global topicoPesq
    print("Deseja Fazer uma Busca por Usuario(1) ou Topoico(2)?")
    pesq = int(input())
    if pesq != 1 and pesq != 2:
        print("ERROR")
        main()

    if pesq == 1:
        print("Digite o nome do user a ser buscado: \n")
        userPesq = str(input())
        cursor.execute("SELECT idUsuario FROM perfil WHERE idUsuario = %s", (userPesq))

        resultado = cursor.fetchone()
        if resultado == None:
            print("Usuario não encontrado!")
            main()
        else:
            for linha in resultado:
                print("Resultado: ", linha)
            print("O que deseja fazer com esse usuario: \n"
                  " SEGUIR(1) | BLOQUEAR(2)")
            opcao = int(input())
            if opcao != 1 and opcao != 2:
                print(Erro)
                pesquisa()
            if opcao == 1:
                cursor.execute("UPDATE perfil SET seguidores = concat(seguidores, '\n' %s) WHERE idUsuario = %s", (user,userPesq))
                cursor.execute("UPDATE perfil SET seguidos = concat(seguidos, '\n' %s) WHERE idUsuario = %s", (userPesq, user))
                conexao.commit()
                print("Seguindo")
                main()
            if opcao == 2:
                cursor.execute("UPDATE perfil SET bloqueados = concat(bloqueados, '\n' %s) WHERE idUsuario = %s", (userPesq, user))
                cursor.execute("DELETE FROM perfil WHERE seguidores = %s", (userPesq))
                myresult = cursor.fetchone()
                for x in myresult:
                    print(x)
                conexao.commit()

                print("Usuario Bloqueado")
                main()
    if pesq == 2:
        print("Digite o topico a ser buscado: \n")
        topicoPesq = str(input())
        cursor.execute("SELECT idTopico FROM topico WHERE idTopico = %s", (topicoPesq))





def editaPerfil():
    global nome
    global bio
    global biografia

    print("Para alterar seu nome digite 1: \n")
    alt = int(input())
    if alt != 1:
        print("ERROR")
        main()
    if alt == 1:
        nome = str(input("digite seu novo nome: \n"))
        cursor.execute("UPDATE perfil SET nomeReal = %s WHERE idUsuario = %s", (nome, user))
        print("Nome editado com sucesso")


    print("EDITAR BIO(1) | SAIR (0): \n")
    bio = int(input())
    if bio != 1:
        print("ERROR")
        main()
    if bio == 1:
        biografia = str(input("Digite sua nova biografia: \n"))
        cursor.execute("UPDATE perfil  SET biografia = %s WHERE idUsuario = %s", (biografia, user))
        print(cursor.rowcount, "Inserido com sucesso")
        conexao.commit()
        print("Perfil editado com sucesso")
        main()



def postagem():
    global legenda

    print("Escreva uma legenda: ")
    legenda = str(input())

    cursor.execute("INSERT INTO postagem(texto, datahora, Perfil_idUsuario) VALUES(%s, %s, %s)",
                   (legenda, data_hora, user))
    conexao.commit()
    print("Postagem realizada com sucesso")
    main()


def listaSeg():
    cursor.execute("SELECT seguidores FROM perfil WHERE idUsuario = %s", (user))
    myresult = cursor.fetchone()

    for x in myresult:
        print(x)
    main()

def listaSego():
    cursor.execute("SELECT seguidos FROM perfil WHERE idUsuario = %s", (user))
    myresult = cursor.fetchone()

    for x in myresult:
        print("\n",x,"\n")
    main()
#---------------MAIN---------------------------

def main():


    cursor.execute("SELECT texto FROM postagem WHERE Perfil_idUsuario = %s", (user))
    myresult = cursor.fetchone()
    if myresult == None:
        print("\nFEED VAZIO\n")
    else:
        print("Postagens Recentes: ")
        for x in myresult:
            print("\n", x, "\n")
            print("CURTIR(1) | COMENTAR (2)")

        print("----TELA PRINCIPAL----")
    print("FUNÇÔES:\n"
          "1 - Atualizar a linha do tempo\n"
          "2 - Pesquisar\n"
          "3 - Nova Postagem\n"
          "4 - Ver Notificações\n"
          "5 - Ver seu Perfil\n"
          "6 - Sair")
    funcoes = int(input())

    if funcoes < 1 and funcoes > 5:
        print("Erro opção invalida!")

    if funcoes == 6:
        login()

    if funcoes == 1:
        main()

    if funcoes == 2:
        pesquisa()

    if funcoes == 3:
        postagem()

    #if funcoes == 4:

    if funcoes == 5:
        print("Funções\n"
              "1 - Editar Pefil\n"
              "2 - Listar Seguidores\n"
              "3 - Listar Seguidos\n"
              "4 - Alterar Privacidade\n")
    funcPER = int(input())

    if funcPER == 1:
        editaPerfil()

    if funcPER == 2:
        listaSeg()

    if funcPER == 3:
        listaSego()

#------------TELA APOS O LOGIN OU CADASTRO-------------
print("--------INSTAGRAM CLONE--------")


print("1 - Fazer login")
print("2 - Criar Perfil")

perfil = int(input("O que deseja fazer?\n"))

if perfil != 1 and perfil != 2:
    print("Erro opção invalida!")

if perfil == 1:
    login()

if perfil == 2:
    cadastro()







