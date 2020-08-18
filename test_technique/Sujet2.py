def divisibilite (X):

    while (len(str(X)) > 1):
        sum = 0
        ch = str(X)
        for i in range(len(ch)):
            sum = sum + int(ch[i])
        X=sum
    if sum in [3,6,9]:
        return (True)
    else:
        return (False)
X = input()
print(divisibilite(X))