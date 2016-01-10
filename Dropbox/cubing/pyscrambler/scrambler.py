#-*-coding:utf8;-*-
#qpy:console
#qpy:2

#Scrambler
from random import choice
import sys
import glob

faces = 'UDFRBL'
mods = ['','2', "'"]
opposites = {'R':'L', 'L':'R', 'U':'D', 'D':'U', 'F':'B', 'B':'F' ,'X':'X'}

oll_scm = ["F U R U' R' F'", "F R U R' U' F'", "f U R U' R' f' F U R U' R' F'"]

def scramble(n):
	lastf = 'X'
	s = ''
	for i in range(n):
		lastf = choice([f for f in faces if f!=lastf and f!=opposites[lastf]])
		s += lastf+choice(mods)+' '
	return s

def getMoveList(smb):
        res = []
        mv = ''
        for ch in smb:
                if ch in faces+faces.lower()+'Mxyz':
                        if mv: res.append(mv)
                        mv = ch
                elif ch in "'2":
                        mv += ch
        if mv: res.append(mv)
        return res

def getRevMove(mv):
        if len(mv)==1:
                return mv+"'"
        elif mv[1]=="'":
                return mv[0]
        return mv

def getRevScramble(smb):
        res = ''
        smbl = getMoveList(smb)
        for mv in smbl:
                res = getRevMove(mv) + ' ' + res
        return res.strip()
        
######

rp, n = 1, 10

modeCollection = False
fname = False

if len(sys.argv)==2 and sys.argv[1]=='c':
        fileColls = ['EdgePerms', ]
        fileColls = glob.glob('./collections/*.txt')
        print fileColls
        fileColls = [f for f in fileColls if f.split   ]
        for i, fn in enumerate(fileColls):
                print str(i+1)+'. '+(fn.split('.')[1]).split('/')[2]
        fcnm = fileColls[int(raw_input('choose scramble collection:'))-1]
        rp = int(raw_input('number of scrambles:'))
        fin = open(fcnm, 'r')
        smbList = fin.readlines()
        smbList = [getRevScramble(smb) for smb in smbList]
        smbList = [smb for smb in smbList  if smb]
        modeCollection = True
elif len(sys.argv)==1 or (len(sys.argv)==2 and sys.argv[1] in ('list', 'file')):
	rp = int(raw_input('number of scrambles:'))
	n = int(raw_input('scramble level:'))
	if len(sys.argv)>=2 and sys.argv[1]=='file':
		fname = raw_input('file name:')
elif len(sys.argv)==2:
	rp = int(sys.argv[1])
elif len(sys.argv)==3:
	rp = int(sys.argv[1])
	
	if sys.argv[2].lower()=='oll':
		mode_oll = True
	else:
		n = int(sys.argv[2])

if fname:
        fl = open(fname, 'w')
        
for i in range(rp):
	print str(i+1)+'. ',
	if modeCollection:
                smb = choice(smbList)
                print smb
                #print getMoveList(smb)
                #print getRevScramble(smb)
	else:
		smb = scramble(n)
		print smb
		if fname: fl.write(str(i+1)+'. '+str(smb)+'\n')
	if (len(sys.argv)>1 and sys.argv[1]=='list') or fname: continue
	print ''
	raw_input('')
if fname: fl.close()
print 'bye bye baby :) '

