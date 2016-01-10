#-*-coding:utf8;-*-
#qpy:console
#qpy:2

#Scrambler
from random import choice
import sys

faces = 'UDFRBL'
mods = ['','2', "'"]

oll_scm = ["F U R U' R' F'", "F R U R' U' F'", "f U R U' R' f' F U R U' R' F'"]

def scramble(n):
	lastf = 'X'
	s = ''
	for i in range(n):
		lastf = choice([f for f in faces if f!=lastf])
		s += lastf+choice(mods)+' '
	return s

rp, n = 1, 10

mode_oll = False

if len(sys.argv)==2:
	rp = int(sys.argv[1])
elif len(sys.argv)==3:
	rp = int(sys.argv[1])
	
	if sys.argv[2].lower()=='oll':
		mode_oll = True
	else:
		n = int(sys.argv[2])
			
for i in range(rp):
	if mode_oll:
		print choice(oll_scm)
	else:
		print scramble(n)
	print ''
	raw_input('')

print 'bye bye baby :) '


