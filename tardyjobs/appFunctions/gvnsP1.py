import random as rd
import time
import copy

def f(tasks, P, D):
  sum = 0
  count = 0
  for i in tasks:
    sum += P[i-1]
    if sum > D[i-1]:
      count += 1
  return count

def swap(l,i,j):
    tmp=l[i]
    l[i]=l[j]
    l[j]=tmp
    return l

def insertion_before(x, lb, ub):  #lb>0 
    bound = len(x)
    xc = None
    if (lb < bound and ub < bound):
        xc = x.copy()
        xc.insert(lb, x[ub]) 
        xc.pop(ub+1)
    return xc


def two_opt(tasks, i, k):
    new_tasks = []
    for index in range(0, i):
        new_tasks.append(tasks[index])
    for index in range(k, i-1, -1):
        new_tasks.append(tasks[index])
    for index in range(k+1, len(tasks)):
        new_tasks.append(tasks[index])
    return new_tasks


def neighbrehood(x, k):
    bound = len(x)
    N=[]
    if(k==3):
        for i in range(0,bound):
            for j in range(i+1,bound):
                N.append(swap(x,i,j))
    elif(k==2):
        for i in range(0,bound):
            for j in range(i+1,bound):
                N.append(insertion_before(x,i,j))
    elif(k==1):
        for i in range(0,bound):
            for j in range(i+1,bound):
                N.append(two_opt(x,i,j))
    return N

global voisins
def shake(x, k):
    N=neighbrehood(x,k)
    xp=rd.choice(N)
    return xp

def change_neighborhood(x, P, D, xp, k):
    if f(xp, P, D) < f(x, P, D):
        x = xp
    else:
        k += 1
    return x,k

k_max = 3
def RVNS(x, P, D, k_max, t = 5):
    start_time = time.time() 
    while time.time() - start_time < t:
        k=1
        while k <= k_max:
            xp = shake(x,k)  
            x, k = change_neighborhood(x, P, D, xp, k) 
    return x

# first improvement : 
def first_improvement(x, P, D, l): 
    N=neighbrehood(x,l)
    for i in range(0,len(N)):
        if f(N[i], P, D) < f(x, P, D):
            x=N[i]
            break
    return x

l_max=2
def VND(x, P, D, l_max, start_time, t):
    l = 1
    while l <= l_max:
        xp = shake(x, l) 
        xp = first_improvement(x, P, D, l) 
        x,l = change_neighborhood(x, P, D, xp, l)
        if time.time() - start_time > t:
              return x
    return x

def GVNS(x, P, D, t=5, k_max=3, l_max=2):
    start_time = time.time() 
    x=RVNS(x, P, D, k_max,0.2)
    while time.time() - start_time < t:
        k=1
        while k <= k_max:
            x1 = shake(x,k)  
            x2 = VND(x1, P, D, l_max, start_time, t)
            x, k = change_neighborhood(x, P, D, x2, k)
            if time.time() - start_time > t:
              return f(x, P, D), x
    return f(x, P, D), x