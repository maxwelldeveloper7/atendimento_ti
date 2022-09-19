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

    pc = "\u001b[32m\U0001f5a5\u001b[m"# emoji de um pc

    print(pc * (largura_titulo))#desenha borda superior
    print(pc, titulo, pc)#desenha titulo e bordas laterais
    print(pc, (centro_titulo - centro_subtitulo - 3) * " ", subtitulo, " " * (centro_titulo - centro_subtitulo -3), pc)#posiciona o subtitulo ao centro do titulo e desenha bordas laterais
    print(pc * (largura_titulo),"\n")#desenha borda inferior

    #print("\u001b[32m\U0001f5a5\u001b[m")