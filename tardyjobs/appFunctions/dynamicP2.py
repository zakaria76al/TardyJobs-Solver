import copy
import itertools
import pandas as pd

T={}
TTT={}

def ff(L,P,G):
    if  L==[]:
        return 0
    elif len(L)==1 :
        G[tuple(L)]=P[L[-1]-1]
        return P[L[-1]-1]
    elif tuple(L[0:-1]) in G:
        G[tuple(L)]=P[L[-1]-1]+G[tuple(L[0:-1])]
        return P[L[-1]-1]+G[tuple(L[0:-1])]

def f(J,P,D,a,b):
    G={}
    for k in range(1,len(P)+1):
     S=list(itertools.combinations(J,k))
     for i in range(0,len(S)):
       S[i]=list(S[i])
     for i in range(0,len(S)):
        TT=S[i]
        if len(TT)==1:
          if ff(TT,P,G)==D[TT[-1]-1]:
            T[tuple(TT)]=0
          elif  ff(TT,P,G)<D[TT[-1]-1]:
            T[tuple(TT)]=(D[TT[-1]-1]-ff(TT,P,G))*a[TT[-1]-1]
          elif  ff(TT,P,G)>D[TT[-1]-1]:
            T[tuple(TT)]=(ff(TT,P,G)-D[TT[-1]-1])*b[TT[-1]-1]
          TTT[tuple(TT)]=tuple(TT)
        elif len(TT)>1:
          fff={}
          for i in range(0,len(TT)):   
            JJ=copy.deepcopy(TT)
            JJ.remove(TT[i])
            JJJ=copy.deepcopy(JJ)
            if  ff(TT,P,G)==D[TT[i]-1]:
                 JJJ.append(TT[i])
                 T[tuple(TT)]=T[tuple(JJ)]+0
                 fff[tuple(JJJ)]=T[tuple(JJ)]+0
            elif ff(TT,P,G)<D[TT[i]-1]: 
                 JJJ.append(TT[i])
                 T[tuple(TT)]=T[tuple(JJ)]+(D[TT[i]-1]-ff(TT,P,G))*a[TT[i]-1]  
                 fff[tuple(JJJ)]=T[tuple(JJ)]+(D[TT[i]-1]-ff(TT,P,G))*a[TT[i]-1] 
            elif ff(TT,P,G)>D[TT[i]-1]:
                 JJJ.append(TT[i])
                 T[tuple(TT)]=T[tuple(JJ)]+(ff(TT,P,G)-D[TT[i]-1])*b[TT[i]-1]
                 fff[tuple(JJJ)]=T[tuple(JJ)]+(ff(TT,P,G)-D[TT[i]-1])*b[TT[i]-1]
            z=min(fff.items(), key=lambda x: x[1])
            T[tuple(TT)]=fff[z[0]]
            x1=list(z[0])
            x=(x1.pop(-1))
            X=[x]
            y=(copy.deepcopy(TTT[tuple(x1)]))
            y=list(y)
            y.extend(X)
            TTT[tuple(TT)]=tuple(y)
    return T[tuple(J)], list(TTT[tuple(J)])