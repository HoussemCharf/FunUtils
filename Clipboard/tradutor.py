import sys
from googletrans import Translator
import clipboard
import keyboard
import time

"""
Requerimentos:
pip install googletrans
pip install clipboard
pip install keyboard

"""


"""Abre um arquivo"""
def abrirArquivo():
    try:
        caminho = sys.argv[1]
    except:
        print("Passe o arquivo como arguemento na chamada do programa!" )
        exit()
    try:
        f = open(caminho, 'r', encoding='utf-8')
    except:
        print("Arquivo não encontrado!!")
        exit()
    string = f.read()
    f.close
    return string

"""Trata a string tirando \n indesejados"""
def tratarString(string):
    string = string.replace("-\n", "")
    string = string.replace("\n", " ")
    string = string.replace("\r\n", " ")
    string = string.replace("\r", "")
    return string

"""Grava o que foi passado como parâmetro no arquivo especificado como agumento na chamada do programa"""
def gravaArquivo(string):
    caminho = sys.argv[1]
    f = open(caminho, 'w', encoding='utf-8')
    f.write(string)
    f.close

"""Traduz o texto requerido"""
def traduzir(string):
    translator = Translator(service_urls=['translate.google.com.br',])
    string = translator.translate(string, dest='pt').text
    return string

"""Copia o conteúdo da área de transferência"""
def areaTransferencia():
    string = clipboard.paste()
    return string

"""Cola o conteúdo traduzido na área de trasnferência"""
def colarAreaTransf(string):
    clipboard.copy(string)

"""Fica esperando a area de trasnferencia mudar"""
def listener(string):
    while clipboard.paste() == string:
        time.sleep(1)

if __name__ == "__main__":
    
    while True:
        """Descomente caso queira usar a tecla de atalho"""
        #keyboard.wait('ctrl+x')

        string = areaTransferencia()

        """Descomente caso queria ler de um arquivo"""
        #string = abrirArquivo()

        string = tratarString(string)
        string = traduzir(string)
        colarAreaTransf(string)

        """" Descomente para gravar num arquivo"""
        #gravaArquivo(string)
        print("Pronto!")
        """Comente caso queira usar telcas de atalho"""
        listener(string)