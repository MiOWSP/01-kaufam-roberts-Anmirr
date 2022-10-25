V =3
M =2
a = [[0.4, 1],[0.7, 0.7],[1.2, 0.6],[1.6, 0.4],[2,0.2]]
t = [1,2]
def calc_x(V,M,a,t):
    x=[1]*(V+1)
    for n in range(1, V+1):
        sum = 0
        for i in range(0,M):
            if n>=t[i]:
                sum +=a[i]*t[i]*x[n-t[i]]
        x[n]=sum/n
    return x
    
def calc_po(X):
    sum=0
    for item in X:
        sum +=item
    return 1/sum

def calc_pn(X,V,M,a,t):
    P=[1]*(V+1)
    P[0]= calc_po(X)
    
    for n in range(1, V+1):
        sum = 0
        for i in range(0,M):
            if n>=t[i]:
                sum +=a[i]*t[i]*P[n-t[i]]
        P[n]=sum/n
    return P

def calc_b(V,P,t,i=1):
    sum=0
    for n in range(V-t[i-1]+1,V+1):
        sum +=P[n]
    return sum
    

def calc_all(V,M,a,t):
    aa = ';'.join([str(round(cnt, 3)) for cnt in a])
    x= calc_x(V,M,a,t)
    xx = ';'.join([str(round(cnt, 3)) for cnt in x])
    pn= calc_pn(x,V,M,a,t)
    pp = ';'.join([str(round(cnt, 3)) for cnt in pn])
    b1= round(calc_b(V,pn,t,i=1),2)
    b2= round(calc_b(V,pn,t,i=2),2)
    print('{};{};{};{};{}'.format(aa, xx, pp, b1, b2))    
    
    
    #print('x: ',x)
    #print('p: ',pn)
    #print('b1: ',b1)
    #print('b2: ',b2)

aa = ';'.join(['a'+str(cnt) for cnt in range(1, len(a[0])+1)])
xx = ';'.join(['x'+str(cnt) for cnt in range(0, V+1)])
pp = ';'.join(['p'+str(cnt) for cnt in range(0, V+1)])
print('{};{};{};b1;b2'.format(aa, xx, pp))  
for item in a:

    calc_all(V,M,item,t)
