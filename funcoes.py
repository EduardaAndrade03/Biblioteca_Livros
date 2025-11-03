# Parte 1 — Estrutura inicial
# 1. Crie uma pasta chamada “bibliotecaPython”.
# 2. Dentro dela, crie o arquivo funcoes.py.
# o Crie as seguintes funções:
# ▪ adicionar_livro(listaLivros): solicita título, autor e status (por padrão
# “disponível”).
# ▪ emprestar_livro(listaLivros): altera o status de um livro para
# “emprestado”.
# ▪ devolver_livro(listaLivros): altera o status de um livro para “disponível”.
# ▪ exibir_livros(listaLivros): mostra todos os livros e seus status.

livros=[]


def adicionar_livro(titulo):
    livro={}
    autor=str(input(f"digite o autor do {titulo} "))
    status="disponivel"
    livro={
        "titulo":titulo,
        "autor":autor,
        "status":status
    }
    livros.append(livro)
    return "livro cadastrado!"

def emprestar_livro():
    livro=str(input("qual livro deseja adiquirir: "))

    for l in livros:
        if l["titulo"]==livro:
            l["status"]="emprestado"
            return "livro emprestado! (devolva viu)"
            
def devolver_livro():
    livro=str(input("qual livro deseja devolver: "))

    for l in livros:
        if l["titulo"]==livro:
            l["status"]="disponível"
            return "livro devolvido! (muito bem)"

def exibir_livros():
    return livros
