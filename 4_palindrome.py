import numpy as np

def palindrome(a):
    a = str(a)
    list_a = list(a)

    central = int(np.floor(len(a)/2))

    forward = list_a[0:central]

    backward = []
    for i in range(-1, -(central+1), -1):
        backward.append(list_a[i])

    count = 0
    for i in range(0, central, 1):
        if forward[i] != backward[i]:
            count+=1

    if count > 0:
        print(a +" is not a palindrom!")
    else:
        print(a + " is a palindrome.")

palindrome('zojkoz')
palindrome('zooz')
palindrome('zokoz')
palindrome('zokkoz')
palindrome(12321)
