import sys
import numpy as np
from ceasar import ceasar, deceasar
from vigenere import vigenere, devigenere
from transposicao import transposicao, detransposicao
from substituicao import substituicao, desubstituicao

from os import listdir
from os.path import isfile, join

def readbytes(file):
	return np.array([b for b in open(file, 'rb').read()])

total = 0

ceasar_ok = 0
ceasar_total = 0

vig_ok = 0
vig_total = 0

transp_ok = 0
transp_total = 0

subs_ok = 0
subs_total = 0

testfiles = listdir('testcases/outputs')


for ofile in testfiles:
	total += 1
	print('\rTestando: ', ofile, ' ' * 30, '\t' * 3, total, '/', len(testfiles), ' '*20, end="")
	N, name, cipher, key = ofile.split('.')
	if key == 'X' or key == 'Y':
		continue
	elif key.startswith('key'):
		key = open('testcases/' + key, 'rb').read()
	
	inputfile = readbytes('testcases/inputs/' + N + '.' + name)
	outputfile = readbytes('testcases/outputs/' + ofile)
	
	if cipher == 'ceasar':
			ceasar_total += 1
			enc = ceasar(inputfile, int(key))
			ceasar_ok += (np.array(enc == outputfile).mean() == 1)

	elif cipher == 'vig':
		vig_total += 1
		enc = vigenere(inputfile, key.encode('ascii'))
		vig_ok += (np.array(enc == outputfile).mean() == 1)

	elif cipher == 'transp':
		transp_total += 1
		enc = transposicao(inputfile, int(key))
		transp_ok += (np.array(enc == outputfile).mean() == 1)

	elif cipher == 'subs':
		subs_total += 1
		enc = substituicao(inputfile, key)
		subs_ok += (np.array(enc == outputfile).mean() == 1)
		if (np.array(enc == outputfile).mean() != 1):
			print('\nFalha na substituição: ', ofile, '\n')



print('\r',' '*100,'\r', end="")
print('Sucesso Ceasar:\t\t', ceasar_ok, '\t/', ceasar_total)
print('Sucesso Vigenere:\t', vig_ok, '\t/', vig_total)
print('Sucesso Transposição:\t', transp_ok, '\t/', transp_total)
print('Sucesso Substituição:\t', subs_ok, '\t/', subs_total)

'''

if len(sys.argv) < 3:
	print('USE: python main.py file.txt N')
	exit(0)

k = sys.argv[2]
textBytes = np.array([b for b in open(sys.argv[1], 'rb').read()])
print('-- Ceasar:')
c = ceasar(textBytes, int(k))
dc = deceasar(c, int(k))
print('' . join(chr(i) for i in c))
print('' . join(chr(i) for i in dc))


print('\n-- Vigenere:')
v = vigenere(textBytes, k.encode('ascii'))
dv = devigenere(v, k.encode('ascii'))
print('' . join(chr(i) for i in v))
print('' . join(chr(i) for i in dv))


print('\n-- Transposição:')
t = transposicao(textBytes, int(k))
dt = detransposicao(t, k)
print('' . join(chr(i) for i in t))
print('' . join(chr(i) for i in dt))


# O k passado aqui é a seed do np.random, usado para gerar
# o alfabeto para a substituição
print('\n-- Substituição:')
s = substituicao(textBytes, k)
ds = desubstituicao(s, k)
print('' . join(chr(i) for i in s))
print('' . join(chr(i) for i in ds))
'''