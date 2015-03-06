import csv


fc = open('Notas.csv')
fd = open('Notas.dat', 'w')
lns = csv.reader(fc)
i=0
for line in lns:
    for i in range(len(line)):
        if i < (len(line)-1):    
            open('Notas.dat','a+b').write(line[i] + '+') 
        elif i == (len(line)-1):
            open('Notas.dat', 'a+b').write(line[i] + '\n') 
