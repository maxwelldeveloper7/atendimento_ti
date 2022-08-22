import os
os.system('clear')

def limpar_console():
    command = 'clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)


def escreve_titulo(titulo, subtitulo):
    
    largura_titulo = int(len(titulo))+4#pega a largura do titulo
    largura_subtitulo = int(len(subtitulo))#pega a largura do subtitulo
    centro_titulo = int(largura_titulo/2)#calcula o centro do titulo
    centro_subtitulo = int(largura_subtitulo/2)#calcula o centro do subtitulo

    print("*" * (largura_titulo))
    print("*", titulo, "*")
    print("*", (centro_titulo - centro_subtitulo - 3) * " ", subtitulo, " " * (centro_titulo - centro_subtitulo -3), "*")#posiciona o subtitulo ao centro do titulo
    print("*" * (largura_titulo))