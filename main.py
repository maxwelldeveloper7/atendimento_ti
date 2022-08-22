import os
os.system('clear')

def limpar_console():
    command = 'clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)


def escreve_titulo(titulo, subtitulo):
    
    largura_titulo = int(len(titulo))#pega a largura do titulo
    largura_subtitulo = int(len(subtitulo))#pega a largura do subtitulo
    centro_titulo = int(largura_titulo/2)#calcula o centro do titulo
    centro_subtitulo = int(largura_subtitulo/2)#calcula o centro do subtitulo

    print(titulo)
    print((centro_titulo - centro_subtitulo - 2)*" ",subtitulo)#posiciona o subtitulo ao centro do titulo


titulo = "PREFEITURA MUNICIPAL DE NANUQUE - CONTROLE DE ATENDIMENTOS"
subtitulo = "INFRAESTRUTURA DE TI"

limpar_console()
escreve_titulo(titulo, subtitulo)



if (__name__=="__main__"):
    print('fim')