import tela;


if (__name__=="__main__"):

    titulo = "PREFEITURA MUNICIPAL DE NANUQUE - INFRAESTRUTURA DE TI"
    subtitulo = "CONTROLE DE ATENDIMENTOS"

    tela.limpar_console()
    tela.escreve_titulo(titulo, subtitulo)
    print("01 --> Cadastros")
    print("02 --> Chamados")
    print("03 --> Relatórios")
    print("04 --> Sair")
    print("")
    opcao = int(input("Opção: "))
    print(opcao)