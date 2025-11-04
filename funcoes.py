from tabulate import tabulate

tabelalivros = [] 

livros=[]


def adicionar_livro(titulo):
    livro={}
    autor=str(input(f"digite o autor do livro {titulo}: "))
    status="disponivel"
    livro={
        "titulo":titulo,
        "autor":autor,
        "status":status
    }
    tabelalivros.append(livro)
    return "livro cadastrado!"

def emprestar_livro():
    livro=str(input("qual livro deseja adiquirir: "))

    for l in tabelalivros:
        if l["titulo"]==livro:
            l["status"]="emprestado"
            return "livro emprestado! (devolva viu)"
        else:
            return "Houve algum problema.."
            
def devolver_livro():
    livro=str(input("qual livro deseja devolver: "))

    for l in tabelalivros:
        if l["titulo"]==livro:
            l["status"]="disponível"
            return "livro devolvido! (muito bem)"

def exibir_livros():
    return tabulate(tabelalivros, headers = "keys", tablefmt="grid")
