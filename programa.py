from funcoes import *

livros=[]


while True:
    print("BEM-VINDO(A) A BIBLIOTECA DE LIVROS")
    print("1 - Adicionar livro")
    print("2 - Exibir todos os livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("0 - Sair")

    op=int(input("Digite sua escolha: "))
    print("-------------------------------------------------------")



    if op==1:
        livro=str(input("Qual livro deseja adicionar: "))
        print(adicionar_livro(livro))
        print("-------------------------------------------------------")


    elif op==2:
        print(exibir_livros())
        print("-------------------------------------------------------")

    elif op==3:
        print(emprestar_livro())
        print("-------------------------------------------------------")

    elif op==4:
        print(devolver_livro())
        print("-------------------------------------------------------")

    elif op==0:
        print("saindo da Biblioteca...")
        break