
def fibonacci(n):
    if n == 0:
        list = []
        list.append(1)
    elif n == 1:
        list = []
        list.append(1)
        list.append(1)
    else:
        list = []
        list.append(1)
        list.append(1)
        i = 2
        while i <= n:
            
            list.append(list[i-2]+list[i-1])
            i=i+1
    print(list)   

fibonacci(100)