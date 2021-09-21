#Generator  Function

def gensq(x,y):
    while (x<=y):
        yield x*x
        x = x+1

g = gensq(1,10)

for i in g:
    print(i,end = '   ' )
    
