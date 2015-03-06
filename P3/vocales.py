
from os import system

def numVocales(word):
    vowels = ['\xa1', '\xa9', '\xad', '\xb3', '\xba', 'a', 'e', 'i', 'o', 'u',
              '\x81', '\x89', '\x8d', '\x93', '\x9a', 'A', 'E', 'I', 'O', 'U']
    i = 0
    cont = 0 
    while i < len(word): 
        cont += vowels.count(word[i]) 
        i += 1 
    return cont


n = raw_input('Por favor dijite el numero de lineas de su interes: ')
infile = open('Sainte-Beuve.txt', 'r')
i=0
tot=0
system('clear')
for line in infile:
    if(i <= int(n)):
        num = numVocales(line)
        tot += num
        i=i+1
    else:
        break
print 'El numero de vocales es: ' + str(tot)
infile.close()
