import pandas as pd

def amhSolver(ino,p,d):
    X=[]
    for i in range(0,len(p)):
           X.append({'D': d[i], 'P': p[i], 'index': ino[i]})
           #X.append([D[i],P[i],ino[i]])
    print(X)
    X.sort(key=lambda x: x.get('D'))
    print(X)

    d=[]
    p=[]
    ino=[]
    for i in range(0,len(X)):
           p.append(X[i].get('P'))
           d.append(X[i].get('D'))
           ino.append(X[i].get('index'))

    rt = []
    P=0
    S=[]
    S1=[]
    for i in range(0,len(p)):
        if P+p[i]<=d[i]:
            S1.append(p[i])
            S.append(ino[i])
            P+=p[i]
        else:
            S1.append(p[i])
            S.append(ino[i])
            P+=p[i]
            #P-=p[max(S)]
            P-=max(S1)
            S.remove(S[S1.index(max(S1))])
            rt.append(max(S1))
            S1.remove(max(S1))
    count = 0
    for i in ino:
        if i not in S:
            count += 1
            S.append(i)
    return count, S