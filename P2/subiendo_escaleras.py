import numpy as np
import itertools

def subir(N):
    if(N==0):
        return 1
    elif N==1:
        return 1
    else:
        return subir(N-1)+subir(N-2)

def arreglo_escaleras(a, b):
    final = []
    for i in range(len(A)):       
        n = a[i] % (2*b[i])
        temp = subir(n)
        final.append(temp)
    return final


print "Para 13 escalones la cantidad de posibilidades es: " + str(subir(13))
print "Para 15 escalones la cantidad de posibilidades es: " + str(subir(15))

A = [4,4,5,5,1]
B = [3,2,4,3,1]

print arreglo_escaleras(A,B)
