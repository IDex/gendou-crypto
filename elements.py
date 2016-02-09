from collections import defaultdict
msg = """74-8-37-19, 3-8-8-19 9-8-37 15-63-13-6-63 13-7-66 6-13-3-12 53-7 74-8-37-19: 39-8-92 74-53-3-3 9-53-7-66 53-22 7-8-74-1-63-37-63 63-3-16-63. 15-3-63-13-16-92-37-63-16 9-3-53-22 5-39 22-1-63-39 13-37-63 8-7-3-39 9-8-37 39-8-92-37-16-63-3-9; 74-8-37-19 3-63-13-23-63-16 13 12-13-37-19 8-9 3-8-7-31-3-13-16-22-53-7-31 0-8-39, 74-8-37-19 53-16 9-8-37 8-22-1-63-37-16."""
table = """1,H;2,He;3,Li;4,Be;5,B;6,C;7,N;8,O;9,F;10,Ne;11,Na;12,Mg;13,Al;14,Si;15,P;16,S;17,Cl;18,Ar;19,K;20,Ca;21,Sc;22,Ti;23,V;24,Cr;25,Mn;26,Fe;27,Co;28,Ni;29,Cu;30,Zn;31,Ga;32,Ge;33,As;34,Se;35,Br;36,Kr;37,Rb;38,Sr;39,Y;40,Zr;41,Nb;42,Mo;43,Tc;44,Ru;45,Rh;46,Pd;47,Ag;48,Cd;49,In;50,Sn;51,Sb;52,Te;53,I;54,Xe;55,Cs;56,Ba;57,La;58,Ce;59,Pr;60,Nd;61,Pm;62,Sm;63,Eu;64,Gd;65,Tb;66,Dy;67,Ho;68,Er;69,Tm;70,Yb;71,Lu;72,Hf;73,Ta;74,W;75,Re;76,Os;77,Ir;78,Pt;79,Au;80,Hg;81,Tl;82,Pb;83,Bi;84,Po;85,At;86,Rn;87,Fr;88,Ra;89,Ac;90,Th;91,Pa;92,U;93,Np;94,Pu;95,Am;96,Cm;97,Bk;98,Cf;99,Es;100,Fm;101,Md;102,No;103,Lr;"""

di = defaultdict(lambda: '')
di['0'] = 'J'
for x in table.split(';'):
    try:
        di[x.split(',')[0]] = x.split(',')[1]
    except IndexError:
        print(x)

words = ''.join([x for x in msg if x.isdigit()
                 or x == '-' or x == ' ']).split(' ')
for x in words:
    print(''.join([di[i][0] for i in x.split('-')]), end=' ')
