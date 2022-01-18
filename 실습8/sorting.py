def insertionSort(d):
    n=len(d)
    for i in range(1,n):
        key=d[i]
        j=i-1
        while j>=0 and d[j]>key:
            d[j+1]=d[j]
            j-=1
        d[j+1]=key
        #print(d,i)



def selectionSort(d):
    n=len(d)
    for i in range(n-1):
        least=i
        for j in range(i+1, n):
            if (d[j]<d[least]):
                least=j
        d[i],d[least]=d[least],d[i]
        #print(d, i+1)


def bubbleSort(d):
    n=len(d)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if d[j-1]>d[j]:
                d[j-1],d[j]=d[j],d[j-1]

        #print("Pass", i+1 , ":", d)