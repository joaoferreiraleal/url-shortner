from random import choice
import string

def gerarHash(tamanhoMax):
    letters = string.ascii_letters + string.digits
    newHash = ''
    for i in range(tamanhoMax):
        newHash += choice(letters)
    return newHash